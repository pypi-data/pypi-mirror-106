"""nt.sqlite functions module"""
from . import CON, _sql
from ... import PROFILE_ID


# ----------------------
# Recipe functions
# ----------------------


def recipe_add():
    """TODO: method for adding recipe"""
    query = """
"""
    return _sql(query)


def recipes():
    """Show recipes with selected details"""
    query = """
SELECT
  id,
  name,
  COUNT(recipe_id) AS n_foods,
  SUM(grams) AS grams,
  guid,
  created
FROM
  recipes
  LEFT JOIN recipe_dat ON recipe_id = id
GROUP BY
  id;
"""
    return _sql(query, headers=True)


def analyze_recipe(recipe_id):
    """Output (nutrient) analysis columns for a given recipe_id"""
    query = """
SELECT
  id,
  name,
  food_id,
  grams
FROM
  recipes
  INNER JOIN recipe_dat ON recipe_id = id
    AND id = ?;
"""
    return _sql(query, values=(recipe_id,))


def recipe(recipe_id):
    """Selects columns for recipe_id"""
    query = "SELECT * FROM recipes WHERE id=?;"
    return _sql(query, values=(recipe_id,))


# ----------------------
# Biometric functions
# ----------------------


def sql_biometrics():
    """Selects biometrics"""
    query = "SELECT * FROM biometrics;"
    return _sql(query, headers=True)


def sql_biometric_logs(profile_id):
    """Selects biometric logs"""
    query = "SELECT * FROM biometric_log WHERE profile_id=?"
    return _sql(query, values=(profile_id,), headers=True)


def sql_biometric_add(bio_vals):
    """Insert biometric log item"""
    cur = CON.cursor()

    # TODO: finish up
    query1 = "INSERT INTO biometric_log(profile_id, tags, notes) VALUES (?, ?, ?)"
    _sql(query1, (PROFILE_ID, "", ""))
    log_id = cur.lastrowid
    print(log_id)
    query2 = "INSERT INTO bio_log_entry(log_id, biometric_id, value) VALUES (?, ? , ?)"
    records = [
        (log_id, biometric_id, value) for biometric_id, value in bio_vals.items()
    ]
    cur.executemany(query2, records)
    return log_id
