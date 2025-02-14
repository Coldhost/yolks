#!/usr/bin/env python3

import json
import click # type: ignore
import sys

@click.group()
def nodejs():
    """Node.js utilities."""
    pass

@nodejs.command()
@click.argument("file", type=click.Path(exists=True, dir_okay=False), default="package.json")
def check_npm_startup(file):
    """Ensure package.json has a 'main' entry and a 'start' script."""
    
    # Load package.json
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        click.echo(f"Error: {file} is empty or invalid JSON!", err=True)
        sys.exit(1)

    changed = False

    # Ensure "main" exists, default to "index.js"
    if "main" not in data:
        data["main"] = "index.js"
        changed = True

    # Ensure "scripts" exists
    if "scripts" not in data or not isinstance(data["scripts"], dict):
        data["scripts"] = {}
        changed = True

    # Ensure "start" script exists inside "scripts"
    if "start" not in data["scripts"]:
        data["scripts"]["start"] = f"node {data['main']}"
        changed = True

    # Write only if changes were made
    if changed:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        click.echo(f"✅ Updated {file} successfully!")
    else:
        click.echo(f"✔ No changes needed in {file}.")

cli = nodejs