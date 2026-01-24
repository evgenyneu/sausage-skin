from src.generate.tests.is_testing import is_testing


def log(message: str) -> None:
    if not is_testing:
        print(message)


def log_dot() -> None:
    if not is_testing:
        print(".", end="", flush=True)
