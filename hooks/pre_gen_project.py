import re
import sys


slug = '{{ cookiecutter.project_slug }}'
package = '{{ cookiecutter.package_name }}'


if not re.match(r'^[a-z0-9-]+$', slug):
    sys.stderr.write('project_slug must be lowercase letters, numbers, and dashes\n')
    sys.exit(1)


if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', package):
    sys.stderr.write('package_name must be a valid Python identifier (PEP 8: lowercase_with_underscores recommended)\n')
    sys.exit(1)
