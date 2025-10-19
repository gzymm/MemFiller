import argparse

b=[]
n=0
ok=False
type=""
size=1
amount=0
current=0

W = "\033[0m"  # white/reset
R = "\033[91m" # red
G = "\033[92m" # green
Y = "\033[93m" # yellow
B = "\033[94m" # blue

parser = argparse.ArgumentParser(description=B+"MemLeaker - Help"+W,epilog=Y+"Example:\n-a 4 -t GB [-sw]"+W)
parser.add_argument("-a","--amount",type=int,help="Amount of RAM that you would like to fill",required=True)
parser.add_argument("-t","--type",type=str,help="Type of storage (GB/MB)",required=True)
parser.add_argument("-sw","--skip-warning",action="store_true",help="Skip warning")

args = parser.parse_args()
type=args.type
amount=args.amount

if not args.skip_warning:
    input(
        R+"WARNING!\n"
        +R+"Using MemFiller could result in a system crash or hanging!\n"+
        "Press Enter to continue. "+W
        )

if type.lower() == "mb":
    size=size*(1024**2)
    ok=True
elif type.lower() == "gb":
    size=size*(1024**3)
    ok=True

if ok:
    print(Y+f"MemFiller will automatically fill your ram up to {amount} {type}"+
          "\nPress ^C to cancel and terminate the process.\n"+W)

try:
    while ok:
        if current >= amount:
            ok=False
            print(G+f"Successfully filled {current} {type}"+W)
            input(G+"Press Enter to terminate"+W)
            exit()
        current+=1
        b.append(bytearray(size))
        print(f"{current}/{amount} {type}")
except KeyboardInterrupt:
    print(G+"\nScript canceled and terminated."+W)
    exit()
