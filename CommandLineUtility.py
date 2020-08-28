# Command line Utility in Python
import argparse
import sys


def calc(args):
    if args.O == 'add':
        return args.X + args.Y

    elif args.O == 'mull':
        return args.X * args.Y

    elif args.O == 'sub':
        return args.X - args.Y

    elif args.O == 'div':
        return args.X / args.Y
    else:
        return 'Something went wrong'






if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--X', type=float, default=1.0,
                        help='Enter1st no,This is the utility for calculation')

    parser.add_argument('--Y', type=float, default=3.0,
                        help='Enter 2nd no,This is the utility for calculation')

    parser.add_argument('--O', type=float, default='add',
                        help='This is the utility for calculation')

    args=parser.parse_args()

    sys.stdout.write(str(calc(args)))
