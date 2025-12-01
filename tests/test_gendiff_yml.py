import os
from gendiff.scripts.gendiff_engine import generate_diff

cur_dir = os.path.dirname(os.path.abspath(__file__))

def get_fixtures_path(file_name):
    return os.path.join(cur_dir, 'fixtures', file_name)

def read_fixtures(file_name):
    with open(get_fixtures_path(file_name),'r') as f:
        return f.read().strip()
    
    
def test_gendiff_yaml():
    
    expected = read_fixtures('expected_diff.txt')
    result = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')

    assert expected == result.strip()


