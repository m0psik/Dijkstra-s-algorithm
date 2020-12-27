import os


def test():
    os.system('python3 ../../src/main.py input.txt output.txt')
    assert open('output.txt').read() == open('answer.txt').read()
