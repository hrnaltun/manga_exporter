from model import *
import json

def print_logo():
    print(f"""
┳┳┓┏┓┳┓┏┓┏┓  ┏┓┏┓┏┓┏┓┏┓┳┓┏┳┓┏┓┳┓
┃┃┃┣┫┃┃┃┓┣┫  ┣  ┃┃ ┃┃┃┃┣┫ ┃ ┣ ┣┫
┛ ┗┛┗┛┗┗┛┛┗  ┗┛┗┛┗┛┣┛┗┛┛┗ ┻ ┗┛┛┗
                     {Colors.GRAY}for Houdoku{Colors.ENDC}
""")

def show_menu(series):
    choice = ''
    while choice != '0':
        print(f"""    
Options:

{Colors.BOLD}1 - EXPORT CHAPTERS TO PDF{Colors.ENDC}
    {Colors.GRAY}collects all images from each chapter folder and
    exports them to separate pdf files{Colors.ENDC}

{Colors.BOLD}2 - EXPORT VOLUMES TO PDF{Colors.ENDC}
    {Colors.GRAY}collects all chapters from  each volume based on
    the dictionary and exports them to separate  pdf 
    files{Colors.ENDC}
    
{Colors.BOLD}3 - EXPORT EVERYTHING{Colors.ENDC}
    {Colors.GRAY}does both of the above{Colors.ENDC}
""")
        choice = input("\n-> ")
        if choice == '1':
            series.export_chapters()
            Colors.job_done()
        if choice == '2':
            series.generate_volumes()
            series.export_volumes()
            Colors.job_done()
        if choice == '3':
            series.export_chapters()
            series.generate_volumes()
            series.export_volumes()
            Colors.job_done()
            choice = '0'


class Main:
    import os
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    NAME = config["NAME"]
    AUTHOR = config["AUTHOR"]
    ROOT = config["ROOT"]
    VOLUME_FILENAME_TEMPLATE = config["VOLUME_FILENAME_TEMPLATE"]
    DICTIONARY = config["DICTIONARY"]

    series: Series = Series(
        name=NAME,
        author=AUTHOR,
        root=ROOT,
        volumes_filename_template=VOLUME_FILENAME_TEMPLATE,
        dictionary=DICTIONARY,
    )

    print_logo()
    show_menu(series)

