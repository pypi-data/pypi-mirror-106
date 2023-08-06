"""Nutratracker DB specific sqlite module"""
import os
import sqlite3
import sys

from .... import NT_DB_NAME, NUTRA_DIR, __db_target_nt__
from .. import sql_entries

CON = None


def nt_ver():
    """Gets version string for nt.sqlite database"""
    query = "SELECT * FROM version;"
    if CON is None:
        nt_sqlite_connect()
    cur = CON.cursor()
    result = cur.execute(query).fetchall()
    cur.close()
    return result[-1][1]


def nt_sqlite_connect():
    """Connects to the nt.sqlite file, or throws an exception"""
    global CON
    db_path = os.path.join(NUTRA_DIR, NT_DB_NAME)
    if os.path.isfile(db_path):
        CON = sqlite3.connect(db_path)
        CON.row_factory = sqlite3.Row

        # Verify version
        if nt_ver() != __db_target_nt__:
            print(
                f"ERROR: usda target [{__db_target_nt__}] mismatch actual [{nt_ver()}]"
            )
            sys.exit(1)
        return CON
    # Else it failed
    print("ERROR: nt database doesn't exist, please run `nutra init`")
    sys.exit(1)


def _sql(query, values=None, headers=False):
    """Executes a SQL command to nt.sqlite"""
    global CON
    if CON is None:
        CON = nt_sqlite_connect()
    cur = CON.cursor()

    # TODO: DEBUG flag in prefs.json ... Print off all queries
    if values:
        # TODO: separate `entry` & `entries` entity for single vs. bulk insert?
        if isinstance(values, list):
            result = cur.executemany(query, values)
        else:  # tuple
            result = cur.execute(query, values)
    else:
        result = cur.execute(query)
    return sql_entries(result, headers=headers)
