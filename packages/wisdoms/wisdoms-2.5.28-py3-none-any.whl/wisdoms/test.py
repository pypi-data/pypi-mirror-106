# Created by Q-ays.
# whosqays@gmail.com

def a(**kwargs):
    print(kwargs)
    print(kwargs['a'])


if __name__ == '__main__':
    d = {'a': "xdfsd", "b": 'fdsf'}
    a(**d)
