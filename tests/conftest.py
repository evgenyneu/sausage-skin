import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import src.generate.tests.is_testing as is_testing_module

is_testing_module.is_testing = True
