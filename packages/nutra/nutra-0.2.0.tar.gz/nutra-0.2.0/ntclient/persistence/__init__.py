# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:09:07 2019

@author: shane
"""

import os
import json

from .. import NUTRA_DIR

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

# TODO: init, handle when it doesn't exist yet
# TODO: prompt to create profile if copying default `prefs.json` with PROFILE_ID: -1 (non-existent)
PREFS_FILE = f"{NUTRA_DIR}/prefs.json"
if os.path.isfile(PREFS_FILE):
    PREFS = json.load(open(PREFS_FILE))
else:
    PREFS = dict()

# TODO: move to utils/__init__.py or main __init__.py
REMOTE_HOST = "https://nutra-server.herokuapp.com"
SERVER_HOST = PREFS.get("NUTRA_CLI_OVERRIDE_LOCAL_SERVER_HOST", REMOTE_HOST)

TESTING = PREFS.get("NUTRA_CLI_NO_ARGS_INJECT_MOCKS", False)
VERBOSITY = PREFS.get("VERBOSITY", 1)

PROFILE_ID = PREFS.get("current_user")  # guid retrieved by __init__ in .sqlfuncs
EMAIL = PREFS.get("email")
LOGIN_TOKEN = PREFS.get("token")
