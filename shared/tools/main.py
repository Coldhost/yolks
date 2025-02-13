import os
import importlib
import click # type: ignore
import logging
import yaml # type: ignore
import sys

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

class CustomFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno == logging.INFO:
            return record.getMessage()  # No prefix for INFO
        return f"[{record.levelname}] {record.getMessage()}"  # Prefix for others

with open(config_path, "r") as f:
    config = yaml.safe_load(f)
    log_level = logging.DEBUG if "debug" in config.get("version", "").lower() else logging.INFO

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

for handler in logger.handlers:
    handler.setFormatter(CustomFormatter())

# Initialize the main CLI group
@click.group()
def cli():
    """Main CLI entry point."""
    pass

if os.path.exists(modules_dir) and os.path.isdir(modules_dir):
    sys.path.insert(0, modules_dir)  # Add to sys.path so importlib can find modules
    
    for module_name in os.listdir(modules_dir):
        # Check if it's a Python file (module)
        if module_name.endswith('.py') and module_name != '__init__.py':
            module_name_without_extension = module_name[:-3]  # Remove '.py' extension
            try:
                importlib.import_module(module_name_without_extension)
                logger.debug(f"Loaded module: {module_name_without_extension}")
            except Exception as e:
                logger.warning(f"Failed to load module {module_name_without_extension}: {e}")

# Add a basic command as a placeholder if needed
@cli.command()
def dumpconfig():
    """Start the main tool."""
    logger.info(config)

@cli.command()
def version():
    logger.info(f"Running version: {config.get('version', 'Unknown version')}")

if __name__ == "__main__":
    cli()