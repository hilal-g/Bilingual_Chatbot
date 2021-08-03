import argparse 

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument('--use-database', type=bool, default=False)

    return parser.parse_args()

args = parse_args()