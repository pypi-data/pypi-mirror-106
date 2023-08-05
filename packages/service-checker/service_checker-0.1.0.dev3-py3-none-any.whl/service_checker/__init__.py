import re
import yaml
from datetime import timedelta
import os
import glob
from pprint import pprint
import time
import subprocess
from prometheus_client import Gauge
from prometheus_client import start_http_server

TIMEDELTA_REGEX = (
    r"((?P<days>-?\d+)d)?"
    r"((?P<hours>-?\d+)h)?"
    r"((?P<minutes>-?\d+)m)?"
    r"((?P<seconds>-?\d+)s?)?"
)
TIMEDELTA_PATTERN = re.compile(TIMEDELTA_REGEX, re.IGNORECASE)


CONFDIR = os.getenv("SC_CONFDIR", "/etc/service_checker/conf.d/")


def parse_delta(delta):
    """Parses a human readable timedelta (3d5h19m) into a datetime.timedelta.
    Delta includes:
    * Xd days
    * Xh hours
    * Xm minutes
    Values can be negative following timedelta's rules. Eg: -5h-30m
    """
    match = TIMEDELTA_PATTERN.match(delta)
    if match:
        parts = {k: int(v) for k, v in match.groupdict().items() if v}
        return timedelta(**parts).total_seconds()

def run():
    start_http_server(9301)

    history_gauge = Gauge("service_checker_failures_in_history", "desc", ["service_name"])
    max_gauge = Gauge("service_checker_failure_count_to_trigger", "desc", ["service_name"])
    length_gauge = Gauge(
        "service_checker_failures_history_length", "desc", ["service_name"]
    )

    conffiles = sorted(glob.glob("{}/*.yaml".format(CONFDIR)))

    triggers = []

    for conffile in conffiles:
        with open(conffile, "r") as fp:
            for trigger in yaml.load(fp, yaml.Loader).get("trigger", []):
                trigger["check_cmd"] = (
                    trigger["check_cmd"]
                    if isinstance(trigger["check_cmd"], list)
                    else [trigger["check_cmd"]]
                )
                trigger["trigger_cmd"] = (
                    trigger["trigger_cmd"]
                    if isinstance(trigger["trigger_cmd"], list)
                    else [trigger["trigger_cmd"]]
                )
                trigger["check_interval"] = str(trigger.get("check_interval", "1m"))
                trigger["trigger_cooldown"] = str(trigger.get("trigger_cooldown", "1m"))
                trigger["trigger_after_failure_count"] = trigger.get(
                    "trigger_after_failure_count", "1"
                )

                trigger["trigger_after_failure_count"] = trigger[
                    "trigger_after_failure_count"
                ].split("/")

                if len(trigger["trigger_after_failure_count"]) < 2:
                    trigger["trigger_after_failure_count"].append(
                        trigger["trigger_after_failure_count"][0]
                    )
                trigger["trigger_after_failure_count"][0] = int(
                    trigger["trigger_after_failure_count"][0]
                )
                trigger["trigger_after_failure_count"][1] = int(
                    trigger["trigger_after_failure_count"][1]
                )

                for time_conf_key in ["check_interval", "trigger_cooldown"]:
                    trigger[time_conf_key] = min(15, parse_delta(trigger[time_conf_key]))

                trigger["state_history"] = []
                trigger["last_restart"] = 0
                trigger["last_check"] = 0

                triggers.append(trigger)

                max_gauge.labels(service_name=trigger["name"]).set(
                    trigger["trigger_after_failure_count"][0]
                )
                length_gauge.labels(service_name=trigger["name"]).set(
                    trigger["trigger_after_failure_count"][1]
                )


    while True:
        did_run = False
        for trigger in triggers:
            if (
                trigger["last_check"] + trigger["check_interval"] > time.time()
                or trigger["last_restart"] + trigger["trigger_cooldown"] > time.time()
            ):
                continue
            did_run = True
            check_ok = True
            for cmd in trigger["check_cmd"]:
                proc = subprocess.run(cmd, shell=True)
                if proc.returncode > 0:
                    check_ok = False
                    break

            trigger["last_check"] = time.time()
            trigger["state_history"].append(check_ok)
            while len(trigger["state_history"]) > trigger["trigger_after_failure_count"][1]:
                trigger["state_history"].pop(0)
            history_gauge.labels(service_name=trigger["name"]).set(
                len([s for s in trigger["state_history"] if not s])
            )

            if (
                len([s for s in trigger["state_history"] if not s])
                < trigger["trigger_after_failure_count"][0]
            ):
                continue

            for cmd in trigger["trigger_cmd"]:
                subprocess.run(cmd, shell=True)

            trigger["last_restart"] = time.time()
            trigger["state_history"] = []

        if not did_run:
            time.sleep(1)
