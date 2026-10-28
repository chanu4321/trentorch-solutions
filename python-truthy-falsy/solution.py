def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    if value is None:
        return False
    elif value == 0:
        return False
    elif value == "":
        return False
    elif value == [] or value == () or value == {}:
        return False
    elif value == set():
        return False
    else: return True


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for value in values:
        if value is None:
            continue
        elif value == 0:
            continue
        elif value == "":
            continue
        elif value == [] or value == () or value == {}:
            continue
        elif value == set():
            continue
        else: return value
    return None
