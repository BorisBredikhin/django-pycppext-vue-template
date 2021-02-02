import argparse
import cppcheckers
from readconfig import load_config

from database.database import database, init

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, help="path to configuration file")

args = parser.parse_args()

config = load_config(open(args.config, 'r'))

init()

database[0].Base.metadata.create_all(bind=database[0].engine)


if __name__ == '__main__':
    cppcheckers.printMessage("kkk")