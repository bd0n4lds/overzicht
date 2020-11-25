# Overzicht
# @bd0nd4lds
# See LICENSE for details

import logging

logger = logging.getLogger(__name__)

def sanitize_filename(f):
    keepchars = (" ", ".", "_")
    return "".join(c for c in f if c.isalnum() or c in keepchars).rstrip()
