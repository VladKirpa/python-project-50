import os

from gendiff.scripts.gendiff_engine import generate_diff

cur_dir = os.path.dirname(os.path.abspath(__file__))


def get_fixture_path(file_name):
    return os.path.join(cur_dir, file_name)


def read_fixture(file_name):
    with open(get_fixture_path(file_name), 'r') as f:
        return f.read().strip()
    

def test_recurs():

    file1 = 'tests/fixtures/file1_rec.json'
    file2 = 'tests/fixtures/file2_rec.json'

    result = generate_diff(file1, file2)
    expected = read_fixture('expected_rec.txt')

    assert expected == result