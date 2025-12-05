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


def stringify(value, deep):
    space = ' ' * (deep * 4)
    end_space = ' ' * ((deep * 4) - 4)

    res = []
    if isinstance(value, dict):
        
        for k, v in value.items():

            val = stringify(v, deep + 1)
            res.append(f"{space}{k}: {val}")

            format = '\n'.join(res)

            last_form = f'{{\n{format}\n{end_space}}}'
            
        return last_form
            
    else: 
        return to_str(value)
            

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


def stylish(data, deepth=1):
    space = ' ' * ((deepth * 4) - 2)
    end = ' ' * ((deepth * 4) - 2)

    result = []
    
    for i in data:

        if i['status'] == 'nested':
            
            result.append(f'{space}  {i['key']}: {{')
            result.extend(stylish(i['children'], deepth + 1))
            result.append(f'{end}  }}')

        else:

            key = i['key']
            value = i['value']
            status = i['status']

            if status == 'added':

                result.append(f"{space}+ {key}: {stringify(value, deepth + 1)}")
            
            elif status == 'deleted': 

                result.append(f'{space}- {key}: {stringify(value, deepth + 1)}')

            elif status == 'nonchanged':
                
                result.append(f'{space}  {key}: {stringify(value, deepth + 1)}')

            elif status == 'changed':

                old = i['old_value']

                result.append(f'{space}- {key}: {stringify(old, deepth + 1)}')
                result.append(f'{space}+ {key}: {stringify(value, deepth)}')
        
    return result


def generate_diff(file_path1, file_path2):

    data1 = data_from_file(file_path1)
    data2 = data_from_file(file_path2)
    make_data = stylish(get_data_diff(data1, data2))

    formated = '\n'.join(make_data)

    return f"{{\n{formated}\n}}"


