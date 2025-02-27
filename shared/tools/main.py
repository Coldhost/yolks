import os
import importlib
import click # type: ignore
import logging
import yaml # type: ignore
import sys
import requests  # noqa: F401
import psutil  # noqa: F401

def resource_path(relative_path):
    """ Get the resource path inside the bundled executable or from the source. """
    try:
        # PyInstaller stores resources in the _MEIPASS folder for bundled apps
        base_path = sys._MEIPASS
    except Exception:
        # If running normally (outside of the bundle), use the current directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

config_path = resource_path("config.yaml")
modules_dir = resource_path("modules")
log_level = logging.INFO
# Initialize the main CLI group
@click.group()
@click.option('--config', 'config_path', default=resource_path("config.yaml"), type=click.Path(exists=True, dir_okay=False), help="Path to the configuration file.")
def cli(config_path):
    """Main CLI entry point."""
    global config
    global log_level
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        log_level = logging.DEBUG if "debug" in config.get("version", "").lower() else logging.INFO

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.INFO:
            return record.getMessage()  # No prefix for INFO
        return f"[{record.levelname}] {record.getMessage()}"  # Prefix for others

logging.basicConfig(level=log_level)

logger = logging.getLogger("main")

for handler in logger.handlers:
    handler.setFormatter(CustomFormatter())

if os.path.exists(modules_dir) and os.path.isdir(modules_dir):
    sys.path.insert(0, modules_dir)  # Add to sys.path so importlib can find modules
    
    for module_name in os.listdir(modules_dir):
        if module_name.endswith('.py') and module_name != '__init__.py':
            module_name_without_extension = module_name[:-3]  # Remove '.py' extension
            try:
                # Dynamically import the module
                module = importlib.import_module(module_name_without_extension)
                logger.debug(f"Loaded module: {module_name_without_extension}")
                
                # Register the CLI group (if it exists) from the module to the parent `cli`
                if hasattr(module, 'cli'):
                    cli.add_command(module.cli)
            except Exception as e:
                logger.warning(f"Failed to load module {module_name_without_extension}: {e}")

@cli.command()
def commands():
    """Log all registered commands."""
    logger.info(f"Registered commands: {', '.join([command.name for command in cli.commands.values()])}")

# Add a basic command as a placeholder if needed
@cli.command()
def dumpconfig():
    """Start the main tool."""
    logger.info(config)

@cli.command()
def version():
    logger.info(f"Running tools version: {config.get('version', 'Unknown version')}")

if __name__ == "__main__":
    cli()