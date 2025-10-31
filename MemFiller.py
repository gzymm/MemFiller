import argparse
import multiprocessing
import os
import time

W = "\033[0m"  # white/reset
R = "\033[91m" # red
G = "\033[92m" # green
Y = "\033[93m" # yellow
B = "\033[94m" # blue

def mf(size,is_done,process,lock,single_proc=True):
    b=[]
    current=0
    while current<amount:
        current+=1
        b.append(bytearray(size))
        print(Y+f"[{os.getpid()}]{W} {current}/{amount} {unit}")
    if single_proc:
        print(G+f"✅ Successfully filled {current} {unit}"+W)
    elif not single_proc:
        with lock:
            is_done.value += 1
        if is_done.value == process:
            print(G+f"✅ Successfully filled {current} {unit} for {process} process ({amount*process} {unit} in total)"+W)
    try:
        while True:
            time.sleep(9)
    except KeyboardInterrupt:
        print(Y+f"[{os.getpid()}]{G} Process terminated"+W)
        exit()

def conv(u:str)->int:
    size=1
    if u.lower() == "mb":
        return size*(1024**2)
    elif u.lower() == "gb":
        return size*(1024**3)
    else:
        print(R+f"❌ Incorrect specified unit \"{u}\""+W)
        exit()

parser = argparse.ArgumentParser(description=B+"MemFiller - Help"+W,epilog=Y+"Example:\n-a 4 -t GB [-p 2]"+W)
parser.add_argument("-a","--amount",type=int,help="Amount of RAM that you would like to fill",required=True)
parser.add_argument("-u","--unit",type=str,help="Unit of storage (GB/MB)",required=True)
parser.add_argument("-p","--process",type=int,help="Number of instances as process",default=1)

args = parser.parse_args()
amount=args.amount
unit=args.unit
process=int(args.process)

if __name__ == "__main__":
    p=[]
    size=conv(unit)
    if process>1:
        print(Y+f"MemFiller will automatically create {process} process and fill your ram up to {amount} {unit} each ({amount*process} {unit} in total)"+
        "\nPress ^C to cancel and terminate all process.\n"+W)
        is_done=multiprocessing.Value("i",0)
        lock=multiprocessing.Lock()
        for i in range(process-1):
            proc=multiprocessing.Process(target=mf,args=(size,is_done,process,lock,False))
            proc.start()
            p.append(proc)
        mf(size,is_done,process,lock,False)
    else:
        print(Y+f"MemFiller will automatically fill your ram up to {amount} {unit}"+
        "\nPress ^C to cancel and terminate all process.\n"+W)
        mf(size,None,process,None)
