import sys
import argparse         #Just need import argparse without sys

if len (sys.argv) == 1:
    print("meaw")
elif len (sys.argv) == 3 and sys.argv[1] == "-n":
    x = int(sys.argv[2])
    for _ in range (x):
        print("meaw")
else:
    print("Invalid arguments")

parser = argparse.ArgumentParser(description="Check the number of arguments.")          #Creating a parser object
parser.add_argument("-n", default=1, type=int, help="Number of times to print")         #Add -n argument to the parser, if without -n default is 1
parser.add_argument("--n", default=1, type=int, help="Number of times per line")        #-n and --n = args.n
parser.add_argument("-w", default="meaw", help="What to print")                         #Add -w argument to the parser
args = parser.parse_args()                                                              #Read the arguments and store them in args

for _ in range (args.n):                    #Without int(args.n) cuz type=int
    print(f"{args.w} "* args.n)

#Description and help for mantioning arguments in terninal
#Can use each argument one by one or all together
#python ... .py -h      #Help message