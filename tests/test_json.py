import os

from gendiff.scripts.gendiff_engine import generate_diff

cur_dir = os.path.dirname(os.path.abspath(__file__))


def get_fixture(filename):

    return os.path.join(cur_dir, filename)


def read_file(filename):

    with open(get_fixture(filename), 'r') as f:
        return f.read().strip()
    

def tests():

    expected = read_file('fixtures/expected_json.txt')

    file1 = get_fixture('fixtures/file1_rec.json')
    file2 = get_fixture('fixtures/file2_rec.json')

    assert expected == generate_diff(file1, file2, 'json')


