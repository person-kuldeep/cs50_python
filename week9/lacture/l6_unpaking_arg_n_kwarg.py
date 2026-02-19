"""
Mini lesson: *args, **kwargs, and unpacking
Goal: learn this for real projects and data engineering style code.
Run: python week9/lacture/l6_unpaking.py
"""


def total_knuts(s: int, g: int, k: int) -> int:
    """Convert wizarding coins to knuts."""
    return (s * 17 + g) * 29 + k


def sum_metrics(*values: float) -> float:
    """
    *values collects positional arguments into a tuple.
    Useful when number of inputs is not fixed.
    """
    return sum(values)


def format_row(**fields: object) -> str:
    """
    **fields collects keyword arguments into a dict.
    Useful for flexible records (logs/events/rows).
    """
    parts = [f"{k}={v}" for k, v in fields.items()]
    return ", ".join(parts)


def ingest_batch(source: str, *records: dict, **options: object) -> None:
    """
    Example similar to a data pipeline function:
    - source: required positional argument
    - *records: zero or more event dictionaries
    - **options: keyword configs (mode, validate, partition, etc.)
    """
    print(f"\nIngesting from: {source}")
    print(f"records={len(records)} options={options}")
    for record in records:
        print(f"  row -> {record}")


def main() -> None:
    # 1) Unpacking list/tuple with *
    coins_list = [100, 50, 25]
    print(f"list unpacking: {total_knuts(*coins_list)} knuts")

    # 2) Unpacking dict with ** (matches by parameter names, not order)
    coins_dict = {"s": 384, "k": 47, "g": 3}
    print(f"dict unpacking: {total_knuts(**coins_dict)} knuts")

    # 3) *args example
    print("sum_metrics:", sum_metrics(1.2, 3.4, 5.0))

    # 4) **kwargs example
    print("format_row:", format_row(id=101, status="ok", retries=2))

    # 5) Data-engineering style use
    event1 = {"id": 1, "event": "click", "user": "u1"}
    event2 = {"id": 2, "event": "purchase", "user": "u2"}
    ingest_options = {"mode": "append", "validate": True}
    ingest_batch("events_api", event1, event2, **ingest_options)

    # 6) Assignment unpacking
    first, *middle, last = [10, 20, 30, 40, 50]
    print(f"assignment unpacking -> first={first}, middle={middle}, last={last}")


def main2():
    avg_list = [32,4.4,24,67,5.7]
    print("avg:",avg_metrics(*avg_list))
    dict_config = {"retries":2, "timeout":40, "mode": "read"}
    print(build_config(**dict_config))
    print(build_config())

# 3) Create a list of 3 rows and call ingest_batch using *rows and **config.
    rows =[
        {"id": 1, "event": "click", "user": "u1"},
        {"id": 2, "event": "purchase", "user": "u2"},
        {"id": 3, "event": "click", "user": "u3"}
    ]
    config  = {"mode": "write" ,"validate": True, "timeout":2}

    ingest_batch(102, *rows, **config)

# Exercises (do these next):
# 1) Write avg_metrics(*values) that returns average.
def avg_metrics(*values):
    return round(sum(values)/len(values),2) # error if no inputs

# 2) Write build_config(**kwargs) that sets defaults:
#    retries=3, timeout=30, mode="append", then overrides from kwargs.
def build_config(retries=3, timeout=30, mode="append"):
    return f"config:- \nretries; {retries}\ntimeout: {timeout}\nmode: {mode}" # not done as asked and have bottleneck



if __name__ == "__main__":
    main2()