#!/usr/bin/env python3

import click # type: ignore
import sys
import os
import requests

# URLs for different Minecraft server types
SERVER_URLS = {
    "vanilla": "https://launcher.mojang.com/v1/objects/{version_hash}/server.jar",
    "paper": "https://api.papermc.io/v2/projects/paper/versions/{version}/builds/{build}/downloads/paper-{version}-{build}.jar",
    "bungeecord": "https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar",
    "forge": "https://maven.minecraftforge.net/net/minecraftforge/forge/{version}/forge-{version}-installer.jar"
}

def download_file(url, output_path):
    """Download a file from a given URL and save it"""
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"✅ Downloaded: {output_path}")
    else:
        print(f"❌ Failed to download: {url}")

def download_minecraft_server(server_type, version=None, build=None):
    """Download Minecraft server based on type, version, and build (auto-detects latest if missing)"""

    if server_type == "vanilla":
        if not version or version == "latest":
            version = get_latest_vanilla_version()
        version_hash = get_vanilla_version_hash(version)
        if not version_hash:
            print(f"❌ Could not find Vanilla version: {version}. Using latest available version.")
            version = get_latest_vanilla_version()
            version_hash = get_vanilla_version_hash(version)
        url = SERVER_URLS["vanilla"].format(version_hash=version_hash)
        output_file = "/home/container/server.jar"

    elif server_type == "paper":
        if not version or version == "latest":
            version = get_latest_paper_version()
        if not build or build == "latest" or not is_valid_paper_build(version, build):
            build = get_latest_paper_build(version)
        if not build:
            print(f"❌ Could not find PaperMC build for version {version}. Using latest available build.")
            build = get_latest_paper_build(version)
        url = SERVER_URLS["paper"].format(version=version, build=build)
        output_file = "/home/container/server.jar"

    elif server_type == "bungeecord":
        url = SERVER_URLS["bungeecord"]
        output_file = "/home/container/server.jar"

    elif server_type == "forge":
        if not version or version == "latest":
            version = get_latest_forge_version()
        url = SERVER_URLS["forge"].format(version=version)
        output_file = "/home/container/server.jar"

    else:
        print("❌ Unsupported server type!")
        return

    download_file(url, output_file)

def get_latest_vanilla_version():
    """Fetch the latest stable Vanilla Minecraft version"""
    response = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
    if response.status_code == 200:
        return response.json()["latest"]["release"]
    return None

def get_vanilla_version_hash(version):
    """Fetch the version hash for vanilla Minecraft"""
    response = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json")
    if response.status_code == 200:
        data = response.json()
        for entry in data["versions"]:
            if entry["id"] == version:
                version_data = requests.get(entry["url"]).json()
                return version_data["downloads"]["server"]["sha1"]
    return None

def get_latest_paper_version():
    """Fetch the latest PaperMC version"""
    response = requests.get("https://api.papermc.io/v2/projects/paper")
    if response.status_code == 200:
        return response.json()["versions"][-1]
    return None

def get_latest_paper_build(version):
    """Fetch the latest PaperMC build for a given version"""
    response = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/{version}")
    if response.status_code == 200:
        builds = response.json().get("builds", [])
        return builds[-1] if builds else None
    return None

def is_valid_paper_build(version, build):
    """Check if a given PaperMC build exists for a version"""
    response = requests.get(f"https://api.papermc.io/v2/projects/paper/versions/{version}")
    if response.status_code == 200:
        return build in response.json().get("builds", [])
    return False

def get_latest_forge_version():
    """Fetch the latest Forge version"""
    response = requests.get("https://files.minecraftforge.net/net/minecraftforge/forge/promotions_slim.json")
    if response.status_code == 200:
        return response.json()["promos"]["latest"]
    return None

# Example usage (will auto-detect latest if version/build is missing)
#download_minecraft_server("vanilla")
#download_minecraft_server("paper")  # Latest Paper version & build
#download_minecraft_server("paper", "1.20.1")  # Latest build for 1.20.1
#download_minecraft_server("paper", "1.20.1", 250)  # Specific build 250
#download_minecraft_server("bungeecord")
#download_minecraft_server("forge")


@click.group()
def minecraft():
    """Node.js utilities."""
    pass

@minecraft.command()
@click.argument('project', type=click.Choice(['vanilla', 'paper', 'bungeecord', 'forge']))
@click.option('--version', default="latest", help="Minecraft version to download")
@click.option('--build', default="latest", help="Build number (only for PaperMC)")
@click.option('--clean/--no-clean', default=False, help="Clean directory before downloading")
def get_version(project, version, build, clean):
    """Download a Minecraft server"""
    if version != "latest" and not version.startswith("1.7"):
        click.echo("❌ Version must be 1.7.x or later!")
        sys.exit(1)

    if clean:
        click.echo("🧹 Cleaning server directory...")
        os.system("rm -rf /home/container/*")

    download_minecraft_server(project, version, build)

    click.echo(f"✅ Downloaded {project} version {version} (Build {build})")

cli = minecraft

