import click # type: ignore
import psutil
import os
import time
import toml
import logging

logger = logging.getLogger("nodejs")
@click.group()
def telemetry():
    pass

# basic things i wanna have here so i can also add it to the scripts

@telemetry.command()
@click.argument("type",default=None)
def gen_data(type):
    info = {
        "name": os.getenv("P_SERVER_UUID"),
        "cpu_cores": os.cpu_count(),
        "memory_total": os.getenv("SERVER_MEMORY"),
        "hostname": os.uname().nodename
    }
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory()._asdict(),
        "io_counters": psutil.disk_io_counters()._asdict(),
        "net_io_counters": psutil.net_io_counters()._asdict(),
        "uptime": time.time() - psutil.boot_time()
    }
    data = {
        "info": info,
        "metrics": metrics,
    }
    with open("/data.toml", "w") as f:
        toml.dump(data, f)
        logger.debug("Telemetry data generated successfully.")

    # Generate file which will contain CPU usage, memory usage, io and network usage,
    # aswell as info about the docker itself, like ram size, cpu cores, etc..
    # Also collect uptime, latest logs (if possible/needed) and if possible
    # check if any warnings/errors on entrypoint
    # Would love toml format if possible, or json
    pass

@telemetry.command()
def gen_crash_report():
    # Generate file containing latest logs, aswell as the error and some useful data like spikes
    pass

@telemetry.command()
def send_data():
    # Send data to the telemetry server of discord bot
    pass


@telemetry.command()
def collect_start():
    # A loop that will periodicaly collect data, run with &
    gen_data()
    send_data("/data.toml")


cli = telemetry