"""Current home to subparsers and service-level logic"""
import os

from .services import _init
from .services.analyze import day_analyze, foods_analyze
from .services.biometrics import biometric_add, biometric_logs, biometrics
from .services.recipe import recipe_add as _recipe_add
from .services.recipe import recipe_edit as _recipe_edit
from .services.recipe import recipe_overview, recipes_overview
from .services.usda import (
    list_nutrients,
    search_results,
    sort_foods_by_kcal_nutrient_id,
    sort_foods_by_nutrient_id,
)


# TODO: rethink arg_parse=None argument, and hasattr() approach (bottom of __main__.py)
# Getting help from subparsers['NAME'].print_help() doesn't work recursively in nested commands


def init():
    """Wrapper init method for persistence stuff"""
    _init()


# --------------------------
# Nutrients, search and sort
# --------------------------
def nutrients():
    """List nutrients"""
    return list_nutrients()


def search(**kwargs):
    """Searches all dbs, foods, recipes, recents and favorites."""
    return search_results(words=kwargs["args"].terms)


def sort(**kwargs):
    """Sorts based on nutrient id"""
    if kwargs["args"].kcal:
        return sort_foods_by_kcal_nutrient_id(kwargs["args"].nutr_id)
    return sort_foods_by_nutrient_id(kwargs["args"].nutr_id)


# --------------------------
# Analysis and Day scoring
# --------------------------
def analyze(**kwargs):
    """Analyze a food"""
    food_ids = kwargs["args"].food_id
    grams = kwargs["args"].grams

    return foods_analyze(food_ids, grams)


def day(**kwargs):
    """Analyze a day's worth of meals"""
    day_csv_paths = kwargs["args"].food_log
    day_csv_paths = [os.path.expanduser(x) for x in day_csv_paths]
    if kwargs["args"].rda:
        rda_csv_path = os.path.expanduser(kwargs["args"].rda)
        return day_analyze(day_csv_paths, rda_csv_path=rda_csv_path)
    return day_analyze(day_csv_paths)


# --------------------------
# Biometrics
# --------------------------
def bio():
    """List biometrics"""
    return biometrics()


def bio_log():
    """List biometric logs"""
    return biometric_logs()


def bio_log_add(**kwargs):
    """Add a biometric log entry"""
    bio_vals = {
        int(x.split(",")[0]): float(x.split(",")[1])
        for x in kwargs["args"].biometric_val
    }

    return biometric_add(bio_vals)


# --------------------------
# Recipes
# --------------------------
def recipe(**kwargs):
    """Return recipe(s)"""
    if kwargs["args"].recipe_id:
        return recipe_overview(kwargs["args"].recipe_id)
    return recipes_overview()


def recipe_add(**kwargs):
    """Add a recipe"""
    food_amts = {
        int(x.split(",")[0]): float(x.split(",")[1]) for x in kwargs["args"].food_amt
    }
    return _recipe_add(kwargs["args"].name, food_amts)


def recipe_edit(**kwargs):
    """Edit a recipe"""
    return _recipe_edit(kwargs["args"].recipe_id)
