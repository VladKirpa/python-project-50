###
def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


###
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
    

###
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
                result.append(f'{space}+ {key}: {stringify(value, deepth + 1)}')
        
    return result