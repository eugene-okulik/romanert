def finish_me(func):

    def wrapper(*args):
        result = func(*args)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
