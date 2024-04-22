def map_nested(func, lst):
    return [map_nested(func, item) if isinstance(item, list) else func(item) for item in lst]
