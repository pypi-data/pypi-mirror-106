# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:02:19 2020

@author: shane

This file is part of nutra, a nutrient analysis program.
    https://github.com/nutratech/cli
    https://pypi.org/project/nutra/

nutra is an extensible nutrient analysis and composition application.
Copyright (C) 2018-2021  Shane Jaroch

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys

import argparse
import argcomplete
from colorama import init as colorama_init

from . import (
    __db_target_nt__,
    __db_target_usda__,
    __title__,
    __version__,
)

from .parsers import (
    analyze,
    bio,
    bio_log,
    bio_log_add,
    day,
    init,
    nutrients,
    recipe,
    recipe_add,
    recipe_edit,
    search,
    sort,
)
from .persistence import TESTING

colorama_init()


# TODO:
# self.init function and state flow
# - display full food name in results
# - display refuse
# - function to list out nutrients and info on them
# - sort function
# - nested nutrient tree, like: http://www.whfoods.com/genpage.php?tname=nutrientprofile&dbid=132
# - attempt to record errors in failed try/catch block (bottom of __main__.py)
# - don't use sys.exit() .. create custom exceptions, handle them


def build_argparser():
    """Adds all subparsers and parsing logic"""

    arg_parser = argparse.ArgumentParser(prog=__title__)
    arg_parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{__title__} cli version {__version__} "
        f"[DB usda v{__db_target_usda__}, nt v{__db_target_nt__}]",
    )

    # --------------------------
    # Sub-command parsers
    # --------------------------
    subparsers = arg_parser.add_subparsers(title="nutra subcommands")

    # --------------------------
    # Init subcommand
    # --------------------------
    init_parser = subparsers.add_parser(
        "init", help="setup profiles, USDA and NT database"
    )
    init_parser.set_defaults(func=init)

    # --------------------------
    # Search subcommand
    # --------------------------
    search_parser = subparsers.add_parser(
        "search", help="search foods by name, list overview info"
    )
    search_parser.add_argument(
        "terms",
        type=str,
        nargs="+",
        help='search query, e.g. "grass fed beef" or "ultraviolet mushrooms"',
    )
    search_parser.set_defaults(func=search)

    # --------------------------
    # Sort subcommand
    # --------------------------
    sort_parser = subparsers.add_parser("sort", help="sort foods by nutrient ID")
    sort_parser.add_argument(
        "--kcal",
        "-c",
        action="store_true",
        help="sort by value per 200 kcal, instead of per 100 g",
    )
    sort_parser.add_argument("nutr_id", type=int)
    sort_parser.set_defaults(func=sort)

    # --------------------------
    # Analyze subcommand
    # --------------------------
    analyze_parser = subparsers.add_parser("anl", help="analyze food(s)")
    analyze_parser.add_argument(
        "-g",
        dest="grams",
        type=float,
        help="analyze for custom number of grams (default is 100g)",
    )
    analyze_parser.add_argument("food_id", type=int, nargs="+")
    analyze_parser.set_defaults(func=analyze)

    # --------------------------
    # Day (analyze-day) subcommand
    # --------------------------
    day_parser = subparsers.add_parser(
        "day", help="analyze a DAY.csv file, RDAs optional"
    )
    day_parser.add_argument(
        "food_log",
        metavar="food_log.csv",
        type=str,
        nargs="+",
        help="path to CSV file of food log",
    )
    day_parser.add_argument(
        "--rda",
        "-r",
        metavar="RDA.csv",
        help="provide a custom RDA file in csv format",
    )
    day_parser.set_defaults(func=day)

    # --------------------------
    # Recipe subcommand
    # --------------------------
    recipe_parser = subparsers.add_parser("recipe", help="list and analyze recipes")
    recipe_parser.add_argument(
        "-n",
        dest="recipe_id",
        type=int,
        help="analyze recipe by ID",
    )
    recipe_parser.set_defaults(func=recipe)
    recipe_subparsers = recipe_parser.add_subparsers(title="recipe subcommands")

    recipe_add_parser = recipe_subparsers.add_parser("add", help="add a recipe")
    recipe_add_parser.add_argument("name")
    recipe_add_parser.add_argument(
        "food_amt", nargs="+", help="food_id,grams e.g. 1001,15 for 15 grams butter"
    )
    recipe_add_parser.set_defaults(func=recipe_add)

    recipe_edit_parser = recipe_subparsers.add_parser("edit", help="edit a recipe")
    recipe_edit_parser.add_argument("recipe_id", type=int, help="edit recipe by ID")
    recipe_edit_parser.set_defaults(func=recipe_edit)

    # --------------------------
    # Biometric subcommand
    # --------------------------
    bio_parser = subparsers.add_parser("bio", help="view, add, remove biometric logs")
    bio_subparsers = bio_parser.add_subparsers(title="biometric subcommands")

    # Log
    bio_log_parser = bio_subparsers.add_parser("log", help="manage biometric logs")
    bio_log_subparsers = bio_log_parser.add_subparsers(
        title="biometric log subcommands"
    )
    bio_log_parser.set_defaults(func=bio_log)

    bio_log_add_parser = bio_log_subparsers.add_parser(
        "add", help="add a biometric log"
    )
    bio_log_add_parser.add_argument(
        "biometric_val", help="id,value pairs, e.g. 22,59 23,110 24,65 ", nargs="+"
    )
    bio_log_add_parser.set_defaults(func=bio_log_add)

    # default case
    bio_parser.set_defaults(func=bio)

    # --------------------------
    # Nutrient subcommand
    # --------------------------
    nutrient_parser = subparsers.add_parser(
        "nt", help="list out nutrients and their info"
    )
    nutrient_parser.set_defaults(func=nutrients)

    return arg_parser


def main():
    """Main method for CLI"""
    arg_parser = build_argparser()
    # Used for testing
    if TESTING and len(sys.argv) < 2:
        # --------------------------------
        # sys.argv = [
        #     "./nutra",
        #     "day",
        #     "~/.nutra/rocky.csv",
        #     # "~/.nutra/rocky-mom.csv",
        #     "-r",
        #     "~/.nutra/dog-rdas-18lbs.csv",
        # ]
        # --------------------------------
        # sys.argv = [
        #     "./nutra",
        #     "day",
        #     "~/.nutra/rocky.csv",
        # ]
        # --------------------------------
        # sys.argv = [
        #     "./nutra",
        #     "day",
        #     "resources/dog-simple.csv",
        #     "-r",
        #     "resources/dog-rdas-18lbs.csv",
        # ]
        # --------------------------------
        # sys.argv = ["./nutra"]
        # sys.argv = ["./nutra" "-h"]
        # sys.argv = ["./nutra" "-v"]
        # sys.argv = ["./nutra", "init"]
        # sys.argv = ["./nutra", "sort"]
        # sys.argv = ["./nutra", "sort", "789"]
        # sys.argv = ["./nutra", "sort", "-c", "789"]
        # sys.argv = ["./nutra", "anl", "9050", "9052"]
        # sys.argv = ["./nutra", "anl", "-g", "85", "23294"]
        # sys.argv = ["./nutra", "recipe"]
        # sys.argv = ["./nutra", "recipe", "-n", "1"]
        # sys.argv = ["./nutra", "recipe", "add", "Test", "1001,15"]
        # sys.argv = ["./nutra", "bio"]
        # sys.argv = ["./nutra", "bio", "log", "add", "22,59", "23,110", "24,65"]
        # sys.argv = ["./nutra", "nt"]
        # sys.argv = ["./nutra", "search", "grass"]
        sys.argv = ["./nutra", "search", "grass", "fed", "beef"]
    try:
        argcomplete.autocomplete(arg_parser)
        args = arg_parser.parse_args()
        if hasattr(args, "func"):
            if len(args.__dict__) > 1:
                args.func(args=args)
            else:
                args.func()
        else:
            arg_parser.print_help()
    except Exception as exception:
        print(f"There was an unforeseen error: {repr(exception)}")
        raise
