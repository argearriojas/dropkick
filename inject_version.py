import versioneer
import re

# Get the current version from Versioneer
version = versioneer.get_version()

# Read the file content
with open("pyproject.toml", "r") as f:
    content = f.read()

# Replace only the version in the [project] section
# Look for version after [project] section and before the next section
pattern = r'(\[project\][^\[]*version\s*=\s*)["\'].*?["\']'
replacement = f'\\1"{version}"'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back to file
with open("pyproject.toml", "w") as f:
    f.write(new_content)

print(f"Updated pyproject.toml with version: {version}")
