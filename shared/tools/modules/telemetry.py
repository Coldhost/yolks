import click # type: ignore

@click.group()
def telemetry():
    pass

# basic things i wanna have here so i can also add it to the scripts

@telemetry.command()
@click.argument("type",default=None)
def gen_data(type):

    # Generate file which will contain CPU usage, memory usage, io and network usage,
    # aswell as info about the docker itself, like ram size, cpu cores, etc..
    # Also collect uptime, latest logs (if possible/needed) and if possible
    # check if any warnings/errors on entrypoint

    pass

@telemetry.command()
def gen_crash_report():
    # Generate file containing latest logs, aswell as the error and some useful data like spikes
    pass

@telemetry.command()
def send_data():
    pass

@telemetry.command()
def collect_start():
    # A loop that will periodicaly collect data, run with &
    pass


cli = telemetry