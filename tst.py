from argparse import ArgumentParser
import configparser

def parse_config():
    parser = ArgumentParser()
    parser.add_argument("--config", dest="config")

    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    return config

