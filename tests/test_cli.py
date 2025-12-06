import os


def test():

    result = os.system('uv run gendiff -h')
    assert (result == 0) 