def get_test_template(path):
    txt = """\
import os


def _prepare():
    # set default path
    os.environ.setdefault('DATAPATH', os.path.join(%s, 'datapath'))
    os.environ.setdefault('STASHPATH', os.path.join(%s, 'stashpath'))
    os.environ.setdefault('SAVEDPATH', os.path.join(%s, 'savedpath'))
    
    # set default env
    json_template = {
        'env': {'None': None},
        'limit': 1
    }
    
    for i in json_template['env'].keys():
        os.environ.setdefault(i, str(json_template['env'][i]))


if __name__ == '__main__':
    _prepare()
"""
    txt = txt % (path, path, path)
    return txt
