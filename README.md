# MemFiller
A script that can be used to intentionally fill the ram of a system that can run python scripts.

This script can be used to test different things such as stress testing, system stability, memory leaks handler, behaviour monitoring, etc...

# Arguments:

### Required:

-a, --amount : Amount of RAM that you would like to fill

-t, --type : Type of storage to fille (GB/MB)

### Optional:

-h, --help : Show the help message

-p, --process : Number of instances as process

# Example:

MemFiller.py -a 4 -t GB -p 2

This will create 2 process that takes 4gb of ram each. 8gb in total of ram will be filled (amount*process)
