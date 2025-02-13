#!/bin/bash

VERSION=v${RUN_NUMBER}-${MATRIX_VERSION}-${MATRIX_TYPE}
MODULES=$(ls modules/ | grep -v '^\.' | tr '\n' ',' | sed 's/,$//')

echo "version: \"$VERSION\"" > config.yaml
echo "modules:" >> config.yaml

if [ -n "$MODULES" ] && [ "${MATRIX_VERSION}" != "minimal" ]; then
    IFS=',' read -ra MODULE_LIST <<< "$MODULES"
    for MODULE in "${MODULE_LIST[@]}"; do
        if [ $MODULE != "__init__.py" ]; then
            echo "  - $MODULE" >> config.yaml
        fi
    done
else
    echo "  - No modules" >> config.yaml
fi

cat config.yaml

# Read the config.yaml file
CONFIG_FILE="config.yaml"

# Extract the version from the config.yaml
VERSION=$(grep -m 1 "version" "$CONFIG_FILE" | sed 's/version: "\(.*\)"/\1/')

# Determine if the build is minimal or full based on the version
if [[ "$VERSION" == *"minimal"* ]]; then
    BUILD_MODE="minimal"
else
    BUILD_MODE="full"
fi

# Start the base pyinstaller command
PYINSTALLER_CMD="pyinstaller --log-level=DEBUG --add-data \"config.yaml:.\" --onefile --name tools"

# If it's a full build, add the entire modules/ directory
if [[ "$BUILD_MODE" != "minimal" ]]; then
    PYINSTALLER_CMD+=" --add-data \"modules:modules\""
fi
PYINSTALLER_CMD+=" --static --hidden-import=json"
# Always add the main.py to the pyinstaller command
PYINSTALLER_CMD+=" main.py"

# Run the pyinstaller command
echo "Running command: $PYINSTALLER_CMD"
eval "$PYINSTALLER_CMD"

# Check if pyinstaller ran successfully

if [ $? -eq 0 ]; then
    echo "✅ Build completed successfully!"
else
    echo "❌ Error during build!"
    exit 1
fi