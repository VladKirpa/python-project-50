import os

from gendiff.scripts.parser import parse_format


def data_from_file(file_path):
    
    _, type = os.path.splitext(file_path)

    format = type[1:]
    
    with open(file_path, 'r') as f:
        inside = f.read()

    return parse_format(inside, format)


def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def get_data_diff(data1, data2):

    both = sorted(set(list(data1.keys()) + list(data2.keys())))
    result = []
    
    for key in both:
        
        # both
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                
                result.append(
                    {
                    'key': key,
                    'status': 'nonchanged',
                    'value': data1[key]
                    }
                )

            else:
                result.append({
                    'key': key,
                    'status': 'changed',
                    'old_value': data1[key],
                    'value': data2[key]
                })
        # new
        elif key in data2 and key not in data1:
            
            result.append({
                'key': key,
                'status': 'added',
                'value': data2[key]
            })

        # old
        elif key in data1 and key not in data2:
            
            result.append({
                'key': key,
                'status': 'deleted',
                'value': data1[key]
            })

    return result


def make_data_diff(diff_data):
    
    result = []

    for i in diff_data:
        
        key = i['key']
        status = i['status']
        value = i['value']

        if status == 'deleted':
            result.append(f'  - {key}: {to_str(value)}')

        elif status == 'changed':
            result.append(f'  - {key}: {to_str(i['old_value'])}')
            result.append(f'  + {key}: {to_str(value)}')

        elif status == 'nonchanged':
            result.append(f'    {key}: {to_str(value)}')

        elif status == 'added':
            result.append(f'  + {key}: {to_str(value)}')
            
    return result


def generate_diff(file_path1, file_path2):

    data1 = data_from_file(file_path1)
    data2 = data_from_file(file_path2)

    make_data = make_data_diff(get_data_diff(data1, data2))

    formated = '\n'.join(make_data)

    return f"{{\n{formated}\n}}"



