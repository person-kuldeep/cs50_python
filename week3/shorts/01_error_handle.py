"""
Error handling (try / except) primer and practical examples.

This file shows common patterns:
- basic try/except
- catching specific exceptions
- using `else` and `finally`
- re-raising exceptions
- real-world usage: input parsing, file I/O, JSON parsing

Run examples by executing this file.
"""

import json
from typing import Any


def basic_example():
    """Simple try/except: converting user input to int."""
    s = input("Enter an integer: ")
    try:
        n = int(s)
    except ValueError:
        print(f"'{s}' is not a valid integer.")
    else:
        print(f"Good — your number times two is {n * 2}.")


def lookup_spacecraft():
    """Example showing catching KeyError and ValueError together.

    Some dictionary values have the suffix ' AU' (astronomical units).
    This function demonstrates cleaning and handling conversion errors.
    """
    d = {
        "Voyager 1": "163",
        "Voyager 2": "136",
        "Pioneer 10": "80 AU",
        "New Horizons": "58",
        "Pioneer 11": "44 AU",
    }

    sc = input("Enter spacecraft name: ")
    try:
        raw = d[sc]
        # remove optional 'AU' suffix and whitespace
        au_str = raw.replace("AU", "").strip()
        au = float(au_str)
    except KeyError:
        print(f"'{sc}' not found in dictionary.")
    except ValueError:
        print(f"Couldn't convert '{raw}' to a number.")
    else:
        meters = convert_au_to_meters(au)
        print(f"{sc}: {au} AU = {meters:.0f} m")


def convert_au_to_meters(au: float) -> float:
    return au * 149_597_870_700.0


def file_read_example(path: str):
    """Real-world: safe file reading with try/except/finally.

    Use a context manager (`with`) in production. Here we show explicit
    handling to demonstrate `finally` (commonly used for cleanup).
    """
    f = None
    try:
        f = open(path, "r", encoding="utf-8")
        data = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    except OSError as e:
        print(f"OS error while reading file: {e}")
        return None
    else:
        print(f"Successfully read {len(data)} bytes from {path}.")
        return data
    finally:
        if f is not None:
            f.close()


def json_parse_example(s: str) -> Any:
    """Parse JSON safely and return the object or None on failure."""
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e.msg}")
        return None


def network_like_example():
    """Simulated network response parsing.

    Instead of making an actual HTTP request (which needs external
    dependencies and network), we simulate a response body.
    """
    # Simulated response bodies
    good = '{"status": "ok", "data": [1,2,3]}'
    bad = '{status: ok, data: [1,2,3]}'  # invalid JSON

    for body in (good, bad):
        parsed = json_parse_example(body)
        if parsed is None:
            # handle the error path (retry, fallback, alert, etc.)
            print("Skipping invalid response.")
        else:
            print("Parsed response:", parsed)


def demonstrate_re_raise():
    """Show catching an exception, adding context, then re-raising it."""
    try:
        int("nope")
    except ValueError as e:
        # Add context, then re-raise so callers can also handle it
        raise ValueError("Failed to convert user input to int") from e


def main():
    # print("=== Basic Example ===")
    # Uncomment to run interactive example
    # basic_example()

    # print("=== Spacecraft Lookup Example ===")
    # Uncomment to run interactive example
    # lookup_spacecraft()

    # print("=== File Read Example (trying a missing file) ===")
    # file_read_example("nonexistent_file.txt")

    # print("=== JSON / Network-like Example ===")
    # network_like_example()

    print("=== Re-raise Example ===")
    demonstrate_re_raise()


if __name__ == "__main__":
    main()
