import sys

import pytest

from gendiff.scripts.gendiff import main


def test_gendiff():
    sys.argv = ['gendiff', '-h']

    with pytest.raises(SystemExit) as e:
        main()
    
    assert e.value.code == 0