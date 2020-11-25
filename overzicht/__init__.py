# Overzicht
# @bd0nd4lds
# See LICENSE for details

import sys
import logging
from termcolor import colored

logger = logging.getLogger(__name__)

assert sys.version_info[0] == 3, "Overzicht requires Python3."

__author__ = '@bd0nd4lds'
__url__ = 'https://github.com/bd0n4lds/overzicht'
__description__ = 'Overzicht'
__license__ = 'MIT'
__version__ = '0.0.1'

def run():
    import argparse
    parser = argparse.ArgumentParser(description='Overzicht execution with CLI options')
    parser.add_argument("-d", "--debug", dest='debug', action='store_true', help="Run with log level set to debug.")
    parser.add_argument("-f", "--file", help="Mulit or Dg Log File to Overview.")
    parser.add_argument('-p', '--pinpad', action="store_true", help="Provide PINpad Model")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    parser.set_defaults(debug=False, file=None, version=None)
    args = parser.parse_args()

    # Set logging level
    level = logging.DEBUG if args.debug else logging.INFO

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