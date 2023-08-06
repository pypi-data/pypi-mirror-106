"""USDA DB specific sqlite module"""
import os
import sqlite3
import sys
import tarfile
import time
import urllib.request

from .... import USDA_DB_NAME, __db_target_usda__
from ... import NUTRA_DIR
from .. import sql_entries

START_TIME = None


# On-boarding function
def usda_init():
    """Downloads and initializes the USDA database sqlite file"""
    # TODO: validate version against __db_target_usda__, return <True or False>
    # TODO: handle resource moved on Bitbucket or version mismatch due to manual overwrite?
    if USDA_DB_NAME not in os.listdir(NUTRA_DIR):
        # Downloads and unpacks the nt-sqlite3 db

        def reporthook(count, block_size, total_size):
            """Shows download progress"""
            global START_TIME
            if count == 0:
                START_TIME = time.time()
                time.sleep(0.01)
                return
            duration = time.time() - START_TIME
            progress_size = int(count * block_size)
            speed = int(progress_size / (1024 * duration))
            percent = int(count * block_size * 100 / total_size)
            sys.stdout.write(
                "\r...%d%%, %d MB, %d KB/s, %d seconds passed"
                % (percent, progress_size / (1024 * 1024), speed, duration)
            )
            sys.stdout.flush()

        # Download usda.sqlite.tar.xz
        url = (
            "https://bitbucket.org/dasheenster/nutra-utils/downloads"
            f"/{USDA_DB_NAME}-{__db_target_usda__}.tar.xz"
        )
        print(f"curl -L {url} -o {USDA_DB_NAME}.tar.xz")
        urllib.request.urlretrieve(
            url,
            f"{NUTRA_DIR}/{USDA_DB_NAME}.tar.xz",
            reporthook,
        )
        print()

        # Extract the archive
        # NOTE: in sql.__init__() we verify version == __db_target_usda__
        #  and if needed invoke this method with force_install=True
        with tarfile.open(
            f"{NUTRA_DIR}/{USDA_DB_NAME}.tar.xz", mode="r:xz"
        ) as usda_sqlite_file:
            try:
                print(f"tar xvf {USDA_DB_NAME}.tar.xz")
                usda_sqlite_file.extractall(NUTRA_DIR)
            except Exception as exception:
                print(repr(exception))
                print("ERROR: corrupt tarball, removing. Please try init again")
                print("rm -rf ~/.nutra/usda")
                # shutil.rmtree(NUTRA_DIR)
                raise
        print(f"==> done downloading {USDA_DB_NAME}")


# verify_usda(__db_target_usda__)


CON = None


def usda_ver():
    """Gets version string for usda.sqlite database"""
    query = "SELECT * FROM version;"
    if CON is None:
        usda_sqlite_connect()
    cur = CON.cursor()
    rows = cur.execute(query).fetchall()
    cur.close()
    return rows[-1][1]


def usda_sqlite_connect():
    """Connects to the usda.sqlite file, or throws an exception"""
    # TODO: support as customizable env var ?
    global CON
    db_path = os.path.join(NUTRA_DIR, USDA_DB_NAME)
    if os.path.isfile(db_path):
        CON = sqlite3.connect(db_path)
        # con.row_factory = sqlite3.Row  # see: https://chrisostrouchov.com/post/python_sqlite/

        # Verify version
        if usda_ver() != __db_target_usda__:
            print(
                f"ERROR: usda target [{__db_target_usda__}] mismatch actual [{usda_ver()}]"
            )
            sys.exit(1)
        return CON
    print("ERROR: usda database doesn't exist, please run `nutra init`")
    sys.exit(1)


def _sql(query, headers=False):
    """Executes a SQL command to usda.sqlite"""
    global CON
    # TODO: DEBUG flag or VERBOSITY level in prefs.json ... Print off all queries
    if CON is None:
        usda_sqlite_connect()
    cur = CON.cursor()
    result = cur.execute(query)
    return sql_entries(result, headers=headers)
