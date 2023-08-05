
def grecha(f):
    def wrapper(*args, **kwargs):
        print('Гречаный привет для Гречного Гречи')

        return f(*args, **kwargs)
    return wrapper


def before_after(arg):
    def bef(f):
        def wrapper(*args, **kwargs):
            print(arg)
            responce = f(*args, **kwargs)
            print(arg)

            return responce
        return wrapper
    return bef
