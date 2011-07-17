#!/usr/bin/env python
#
# authfas.py: Askbot plugin to facilitate Fedora Account System(FAS) user
# authentication.
#
# Author: P J P <pj.pandit@yahoo.co.in>
#
# This program is a free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the license, or(at your option)
# any later version. See http://www.gnu.org/copyleft/gpl.html for the full
# text of the license.
#

import os
import sys
import getpass
import fedora.client

NAME = 'FAS'
TYPE = 'password'
DISPLAY_NAME = 'Fedora Account System'
EXTRA_TOKEN_NAME = 'FAS username and password'
ICON_MEDIA_PATH = '/images/fedora.png'

ORDER_NUMBER = 1        # > 0, at which position to insert the button
BIG_BUTTON = True       # if true - goes to the row of big buttons

# For password-type login systems only
#CREATE_PASSWORD_PROMPT = 'Create a Fedora account'
#CHANGE_PASSWORD_PROMPT = 'Change your Fedora password'

# optional
TOOLTIP_TEXT = 'Sign in via FAS'


#for password login systems only - define function check_password
def check_password(username, password):

    url = 'https://admin.fedoraproject.org/accounts/'
    fas = fedora.client.AccountSystem(base_url=url)

    return fas.verify_password(username, password)


if __name__ == "__main__":

    if (len(sys.argv) < 2):
        print "Usage: %s <USERNAME>" % sys.argv[0]
        sys.exit(1)

    username = sys.argv[1]
    userpass = getpass.getpass()
    if (check_password(username, userpass)):
        print sys.argv[0] + ":", "authentication successful!"
    else:
        print sys.argv[0] + ":", "authentication failed."

    sys.exit(0)
