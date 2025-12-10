import os

from gendiff.gendiff_engine import generate_diff

cur_dir = os.path.dirname(os.path.abspath(__file__))


def get_fixtures_path(file_name):
    return os.path.join(cur_dir, 'fixtures', file_name)


def read_fixtures(file_name):
    with open(get_fixtures_path(file_name), 'r') as f:
        return f.read().strip()
    
    
def test_gendiff_yaml():

    file1 = 'tests/fixtures/file1.yml'
    file2 = 'tests/fixtures/file2.yml'
    
    expected = read_fixtures('expected_diff.txt')
    result = generate_diff(file1, file2)

    assert expected == result.strip()


