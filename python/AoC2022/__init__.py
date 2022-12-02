import os
import pkgutil

# Find all packages in this current directory
this_file = os.path.abspath(__file__)
this_dir = os.path.dirname(this_file)
days = pkgutil.iter_modules([this_dir])

# Parse all packages that are days
__all__ = []
for day in days:
    # Skip this module if it is not a day
    if not day.name.startswith('day'):
        continue

    # Append this day to __all__ for importing with *
    __all__.append(day.name)

    # Import day into this namespace
    cmd = f"from .{day.name} import {day.name}"
    exec(cmd)
