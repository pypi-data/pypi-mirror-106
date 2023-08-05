def preset_from_file(file):
    with open(file) as f:
        return f.read().strip('\n')


def ready_dict(dictobj):
    return {';;' + key + ';;': value for key,value in dictobj.items()}

def create_template(file,dictobj):
    with open(file) as f:

        text = f.read()
        
        for key in dictobj:
            text = text.replace(key,dictobj[key])

        return text

def create_template_from_source(textdata,dictobj):
    text = textdata
        
    for key in dictobj:
        text = text.replace(key,dictobj[key])

    return text
            
