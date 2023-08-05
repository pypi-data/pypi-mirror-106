import os
import json
import environ
os.environ['PYTHON_EGG_CACHE'] = '/tmp' # a writable directory 

def load_default_auth():
    try:
        print("Trying to load auth from file")
        return load_file_auth("env.json")
    except:
        try:
            print("Trying to load auth from environment variable")
            return load_env_auth()
        except:
            print("Unable to load auth. Exiting.")
            exit(1)

def load_str_auth(str):
    return json.loads(str)

def load_file_auth(file_name):
    with open(file_name) as auth_file:
        return json.load(auth_file)

def load_env_auth(name="AUTH"):
    auth = json.loads(environ[name])
    return auth

if(__name__=="__main__"):
    auth = load_default_auth()