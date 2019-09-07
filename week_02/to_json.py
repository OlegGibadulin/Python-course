import functools
import json

def to_json(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
        """d = func()
        str_up = "'{"
        for c in d:
            str_up += '"' + str(c) + '": ' + str(d[c]) + ", "

        str_up = str_up[:-2:] + "}'"
        return str_up"""
    return new_func

@to_json
def get_data():
  return {
    'data': 42,
    'agaa': 10
  }
  
print (get_data())  # вернёт '{"data": 42}'