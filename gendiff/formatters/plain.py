from gendiff.formatters.stylish import to_str
 

def is_value(value):

    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return to_str(value)

        
def get_path(data, path=[]):

    for i in data:
        
        if i['status'] == 'nested':

            path.append(i['key'])
            for k in i['children']:
                get_path(i['children'])

        return path
    

def plain(data, path=""):

    result = []

    for i in data:
        key = i["key"]
        status = i["status"]

        cur_path = f'{path}.{key}' if path else key
        
        if i["status"] == "nested":

            child = plain(i['children'], cur_path)
            result.extend(child)

        else:

            value = is_value(i["value"])

            if status == 'added':
                
                result.append(
                    f"Property '{cur_path}' was added with value: {value}")

            elif status == 'deleted':

                result.append(f"Property '{cur_path}' was removed")

            elif status == 'changed':
                
                result.append(
                    f"Property '{cur_path}' was updated. "
                    f"From {is_value(i['old_value'])} to {value}")

    return result


                





