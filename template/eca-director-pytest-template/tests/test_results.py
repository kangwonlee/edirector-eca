# begin tests/test_results.py
#
# TEMPLATE: Replace this file with assignment-specific tests.
# The generated exercise.py is in STUDENT_CODE_FOLDER (CONTAINER_OUTPUT).
#
# Example for a bisection method assignment:
#
#   import exercise
#   def test__bisection_step(f, root, epsilon):
#       result = exercise.bisection_step(f, x_lower, x_upper, epsilon)
#       assert isinstance(result, dict)
#       ...

import os
import pathlib
import sys

import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = pathlib.Path(os.getenv('STUDENT_CODE_FOLDER', test_folder.parent.absolute()))


sys.path.insert(
    0,
    str(proj_folder)
)


def test__exercise_importable():
    """Verify that the generated exercise.py can be imported."""
    import exercise  # noqa: F401


if __name__ == "__main__":
    pytest.main([__file__])

# end tests/test_results.py
