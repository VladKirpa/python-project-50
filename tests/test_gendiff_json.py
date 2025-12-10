import os

from gendiff.gendiff_engine import generate_diff

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_fixture_path(file_name):
    return os.path.join(CURRENT_DIR, 'fixtures', file_name)


def read_fixture(file_name):
    with open(get_fixture_path(file_name), 'r') as f:
        return f.read().strip()
    

def test_gendiff_json():

    expected = read_fixture('expected_diff.txt')

    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')

    result = generate_diff(file1, file2)

    assert result.strip() == expected


