# Overzicht
# @bd0nd4lds
# See LICENSE for details

import re
import argparse
import sys
import logging
import argparse
from termcolor import colored

class SmartFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

def _parse_line(line):
    """Do a regex search against all defined regexes and
    return the key and match result of the first matching regex"""
    patterns = ['TCP OUT', 'TCP IN']

    for pattern in patterns:
        match = re.search(pattern, line)
        if match:
            return match
    # if there are no matches
    return None

def _parse_data(log_file_path, export_file, regex, read_line=True, reparse=False):
    """
    Parse text at given filepath

    Parameters
    ----------

    Returns
    -------

    """
    with open(log_file_path, "r") as file:
        match_list = []
        if read_line == True:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
        else:
            data = file.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group()
                match_list.append(match_text)
    file.close()

    # if reparse == True:
     # match_list = reparseData(match_list, '(property name="(.{1,50})">(Enabled)<\/property>)')
        
def run():
    parser = argparse.ArgumentParser(description="Overzicht execution with CLI options")
    
    parser.add_argument("--version", action="version", version='%(prog)s 1.0', help="Version Informaton")
    
    parser.add_argument("-d", "--debug", dest='debug', action='store_true', help="Run with log level set to debug.")
    
    parser.add_argument("-f", "--file", help="Mulit or Dg Log File to Overview.")
    
    parser.add_argument('-p', '--pinpad', action="store_true", help="Provide PINpad Model")

    args = parser.parse_args()

    # Set logging level
    level = logging.DEBUG if args.debug else logging.INFO

    # Print help
    if not args.debug or args.version:
        import sys
        parser.print_help()
        sys.exit(0)
        
    # Print version
    if args.version:
        import sys
        print(__version__)
        sys.exit(0)

    # Log to file
    if args.file:
        logging.basicConfig(filename=args.file, filemode='a', level=level)


def opening():
    title = """
            Overzicht                                                
            """
    creds = "                                                       #Coded by @bd0nd4lds"

    print(colored(title, 'magenta'))
    print(colored(creds, 'red'))
    print()
    print()
    
if __name__ == '__main__':
        opening()
        run()