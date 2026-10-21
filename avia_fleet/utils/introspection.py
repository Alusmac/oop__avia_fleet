def analyze_object(obj: object) -> dict:
    """Analyze an object using Python introspection."""
    return {
        "class": obj.__class__.__name__,
        "attributes": list(vars(obj).keys()),
        "methods": [
            name for name in dir(obj)
            if callable(getattr(obj, name)) and not name.startswith("__")
        ],
    }


def dynamic_call(obj: object, method_name: str, *args, **kwargs):
    """Call an object's method dynamically by its name."""
    method = getattr(obj, method_name, None)

    if method is None or not callable(method):
        raise AttributeError(
            f"Method '{method_name}' does not exist or is not callable."
        )

    return method(*args, **kwargs)
