import sys

sys.path.append(r"E:\Anaconda\Lib\site-packages")


def function():
    import chucknorris.quips as q

    return q.random("Janet")


print(function())