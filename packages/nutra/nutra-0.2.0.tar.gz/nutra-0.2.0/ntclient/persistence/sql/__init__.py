"""Main SQL persistence module, need to rethink circular imports and shared code"""


def sql_entries(sql_result, headers=False):
    """Formats and returns an sql_result for console digestion and output"""
    rows = sql_result.fetchall()
    if headers:
        headers = [x[0] for x in sql_result.description]
        return headers, rows
    return rows
