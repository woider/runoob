from _datetime import datetime


def exectime(func):
    def inner(*args, **kwargs):
        begin = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        inter = end - begin
        return '{0}.{1}'.format(inter.seconds, inter.microseconds)

    return inner
