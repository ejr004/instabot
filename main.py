from instapy import InstaPy
from instapy import set_workspace
from features import light_interaction
import configparser
import argparse

# Argument parser
arg_p = argparse.ArgumentParser()
arg_p.add_argument('-s', action='store', dest='file', required=True, help='config file')
arguments = arg_p.parse_args()
print(arguments.file)

# Config Parser
c_parser = configparser.ConfigParser()
c_parser.read(arguments.file)

# workspace local
set_workspace(path=None)

# Login
mysession = InstaPy(username=c_parser['USERPASS']['username'],
                    password=c_parser['USERPASS']['password'],
                    headless_browser=True,
                    multi_logs=True)

# light_interaction
light_interaction.light_interaction(mysession,
                                    c_parser['SETTINGS']['photo_comments'],
                                    c_parser['SETTINGS']['u_followers'],
                                    c_parser['SETTINGS']['f_likers'],
                                    c_parser['SETTINGS']['f_tags'])

