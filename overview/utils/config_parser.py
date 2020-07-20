from argparse import ArgumentParser
import configparser

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--config", dest="config")

    args = parser.parse_args()

    return args

def parse_config(config_path):

    config = configparser.ConfigParser()
    config.read(config_path)
  
    return config._sections
