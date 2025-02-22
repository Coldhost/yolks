import asyncio
import click  # type: ignore
import psutil
import os
import time
import toml

# Hardcoded host and port
HOST = "node.coldhost.eu"
PORT = 26024
INTERVAL = 10  # Send data every 10 seconds

@click.group()
def telemetry():
    """Send system telemetry data to a server."""
    pass

def generate_telemetry_data(place):
    """Generate system telemetry data and save it as a TOML file."""
    info = {
        "name": os.getenv("P_SERVER_UUID", "unknown"),
        "cpu_cores": os.cpu_count(),
        "memory_total": os.getenv("SERVER_MEMORY", "unknown"),
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

    # Save the collected data to a TOML file
    toml_data = toml.dumps(data).encode('utf-8')
    with open(place, 'wb') as f:
        f.write(toml_data)

async def send_telemetry(reader, writer):
    """Send telemetry data over an existing connection."""
    try:
        # Read the generated telemetry data file
        with open('data.toml', 'rb') as f:
            file_data = f.read()
        
        # Send the file data
        writer.write(file_data)
        await writer.drain()

        print('Sent telemetry data from data.toml')

    except Exception as e:
        print(f"Error sending data: {e}")
        raise e  # Signal to reconnect

async def periodic_send():
    """Keep connection open and send telemetry periodically."""
    while True:
        try:
            print(f"Connecting to {HOST}:{PORT}...")
            reader, writer = await asyncio.open_connection(HOST, PORT)
            print("Connection established.")

            while True:
                # Generate telemetry data
                generate_telemetry_data('data.toml')

                # Send telemetry data
                await send_telemetry(reader, writer)

                # Wait before sending again
                await asyncio.sleep(INTERVAL)

        except Exception as e:
            print(f"Connection failed: {e}")
            print("Retrying in 5 seconds...")
            await asyncio.sleep(5)  # Wait before reconnecting

@telemetry.command()
def start_telemetry():
    """Start the periodic telemetry sender."""
    asyncio.run(periodic_send())

cli = telemetry
