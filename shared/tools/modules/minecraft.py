#!/usr/bin/env python3

import click # type: ignore
import sys
import os

@click.group()
def minecraft():
    """Node.js utilities."""
    pass

@minecraft.command()
@click.argument('project', type=click.Choice(['vanilla', 'paper', 'bungee', 'spigot', 'forge']))
@click.argument('version')
@click.argument('build')
@click.option('--clean/--no-clean', default=True, help="Clean build directory before building.")
def get_version(project, version, build, clean):
    if not version.startswith('1.7.') and not version >= '1.7.0':
        click.echo("Version must be any Minecraft version from 1.7.x to the latest.")
        sys.exit(1)
    if clean:
        click.echo("Cleaning root directory...")
        os.system("rm -rf /home/container/*")
    if project == "vanilla":
        click.echo("downloading vanilla")
    elif project == "paper":
        click.echo("downloading paper")
    elif project == "bungee":
        click.echo("downloading bungee")
    elif project == "spigot":
        click.echo("downloading spigot")
    elif project == "forge":
        click.echo("downloading forge")
    # Add your logic here to handle the version and build
    click.echo(f"Project: {project}, Version: {version}, Build: {build}")


cli = minecraft
