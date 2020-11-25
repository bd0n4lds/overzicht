# Overzicht
# @bd0nd4lds
# See LICENSE for details

import re
import argparse

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

def parseData(log_file_path, export_file, regex, read_line=True, reparse=False):
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

    if reparse == True:
        match_list = reparseData(match_list, '(property name="(.{1,50})">(Enabled)<\/property>)')