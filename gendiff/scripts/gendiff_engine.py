import os

from gendiff.scripts.Format.plain_format import plain
from gendiff.scripts.Format.stylish_format import stylish
from gendiff.scripts.parser import parse_format


def data_from_file(file_path):
    
    _, type = os.path.splitext(file_path)

    format = type[1:]
    
    with open(file_path, 'r') as f:
        inside = f.read()

    return parse_format(inside, format)


def get_data_diff(data1, data2):

    data = sorted(set(list(data1.keys()) + list(data2.keys())))

    result = []

    for key in data:
        
        if key in data1 and key in data2:
            
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):

                result.append({
                    "key": key,
                    "status": 'nested',
                    'children': get_data_diff(data1[key], data2[key])
                })

            elif data1[key] == data2[key]:
                
                result.append({
                    'key': key,
                    'value': data1[key],
                    'status': 'nonchanged'
                })
        
            else: 
                
                result.append({
                    'key': key,
                    'old_value': data1[key],
                    'value': data2[key],
                    'status': 'changed'
                })

        elif key in data2 and key not in data1:
            
            result.append({
                "key": key,
                'value': data2[key],
                "status": 'added'
            })

        elif key in data1 and key not in data2:
            
            result.append({
                "key": key,
                "value": data1[key],
                "status": 'deleted'
            })  

    return result


def make_format(format_type, data1, data2):

    available_format = ['stylish', 'plain']

    if format_type in available_format:

        if format_type == "stylish":
            return stylish(get_data_diff(data1, data2))
        
        elif format_type == 'plain':
            return plain(get_data_diff(data1, data2))


def generate_diff(file_path1, file_path2, format='stylish'):

    data1 = data_from_file(file_path1)
    data2 = data_from_file(file_path2)

    make_data = make_format(format, data1, data2)

    formated = '\n'.join(make_data)

    if format == "stylish":
        return f"{{\n{formated}\n}}"
    
    elif format == 'plain':
        return f"{formated}"

    return f"{{\n{formated}\n}}"




