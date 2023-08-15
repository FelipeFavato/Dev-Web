import time

import pytest


@pytest.mark.slow
def test_slow_marker():
    time.sleep(4)


# pytest -m MARKEXPR
# pytest -m 'not slow' -vv
