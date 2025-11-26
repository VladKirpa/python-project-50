import json

def read_json(file_path):
    with open(file_path) as path:
        return json.load(path)
    

    
def get_data_diff(file1, file2):
    f1 = read_json(file1)
    f2 = read_json(file2)

    both = sorted(set(list(f1.keys()) + list(f2.keys())))
    result = []
    
    for key in both:
        
        #both
        if key in f1 and key in f2:
            if f1[key] == f2[key]:
                
                result.append(
                    {
                    'key': key,
                    'status': 'nonchanged',
                    'value': f1[key]
                    }
                )

            else:
                result.append({
                    'key':key,
                    'status':'changed',
                    'old_value' : f1[key],
                    'value' : f2[key]
                })
        #new
        elif key in f2 and key not in f1:
            
            result.append({
                'key':key,
                'status':'added',
                'value':f2[key]
            })

        #old
        elif key in f1 and key not in f2:
            
            result.append({
                'key':key,
                'status':'deleted',
                'value': f1[key]
            })


    return result




def make_data_diff(file_path1, file_path2):
    

    data = get_data_diff(file_path1, file_path2)

    result = []

    for i in data:
        
        key = i['key']
        status = i['status']
        value = i['value']

        if status == 'deleted':
            result.append(f'  - {key}: {value}')

        elif status == 'changed':
            result.append(f'  - {key}: {i['old_value']}')
            result.append(f'  + {key}: {value}')

        elif status == 'nonchanged':
            result.append(f'    {key}: {value}')

        elif status == 'added':
            result.append(f'  + {key}: {value}')
            
    return result


def generate_diff(file_path1, file_path2):

    make_data = make_data_diff(file_path1, file_path2)

    formated = '\n'.join(make_data)

    return f"{{\n{formated}\n}}"



