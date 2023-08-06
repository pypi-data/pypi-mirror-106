import json
import re
import traceback


def safeint(value):
    try:
        return int(float(value))
    except:
        return None


def safeintorzero(value):
    try:
        return int(value)
    except:
        return 0


def safeintorbignumber(value):
    try:
        return int(value)
    except:
        return 10000000


def safefloat(value):
    try:
        return float(value)
    except:
        return None


def jsonb_date_to_str(value):
    result = value
    if value:
        result = str(value)
    return result


def pretty_json(value):
    return json.dumps(value, indent=4)


def onewhite(query):
    _RE_COMBINE_WHITESPACE = re.compile(r"\s+")

    query = _RE_COMBINE_WHITESPACE.sub(" ", query).strip()

    return query


def join_strings_if_not_null(*nameparts, seperator=" "):
    non_null_parts = [namepart.strip() for namepart in nameparts if namepart is not None and len(namepart) > 0]
    return seperator.join(non_null_parts)


def get_full_name(*nameparts):
    return join_strings_if_not_null(*nameparts, " ")


def get_exception_traceback(e):
    return ''.join(traceback.format_tb(e.__traceback__))
