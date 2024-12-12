import versioneer
import toml

# Get the current version from Versioneer
version = versioneer.get_version()

# Load the pyproject.toml file
with open("pyproject.toml", "r") as f:
    pyproject = toml.load(f)

# Update the version in the [project] section
pyproject["project"]["version"] = version

# Write the updated pyproject.toml file
with open("pyproject.toml", "w") as f:
    toml.dump(pyproject, f)

print(f"Updated pyproject.toml with version: {version}")
