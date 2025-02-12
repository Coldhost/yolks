import os
import importlib
import click
import logging
logger = logging.Logger("main",logging.INFO)

# Initialize the main CLI group
@click.group()
def cli():
    """Main CLI entry point."""
    pass

# Try to dynamically load all modules in the 'modules/' directory
modules_dir = 'modules'

if os.path.exists(modules_dir) and os.path.isdir(modules_dir):
    # Load each module in the modules directory
    for module_name in os.listdir(modules_dir):
        # Check if it's a Python file (module)
        if module_name.endswith('.py') and module_name != '__init__.py':
            module_name_without_extension = module_name[:-3]  # Remove '.py' extension
            try:
                # Dynamically import the module
                importlib.import_module(f"{modules_dir}.{module_name_without_extension}")
                logger.debug(f"Loaded module: {module_name_without_extension}")
            except Exception as e:
                logger.warning(f"Failed to load module {module_name_without_extension}: {e}")

# Add a basic command as a placeholder if needed
@cli.command()
def start():
    """Start the main tool."""
    print("main is working")

if __name__ == "__main__":
    cli()