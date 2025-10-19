# MemFiller
A script that can be used to intentionally fill the ram of a system that can run python scripts.

This script can be used to test different things such as stress testing, system stability, memory leaks handler, behaviour monitoring, etc...

# Arguments:

### Required:

-a, --amount : Amount of RAM that you would like to fill

-t, --type : Type of storage to fille (GB/MB)

### Optional:

-h, --help : Show the help message

-s, --skip-warning : Skip the warning message that requires confirmation

# Example:

MemFiller.py -a 4 -t GB

This will fill the ram up to 4gb
