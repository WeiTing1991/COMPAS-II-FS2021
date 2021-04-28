import os

def test_directory(filename):
    HERE = os.path.dirname(__file__)
    filepath = os.path.join(HERE, filename)
    print(filepath)
    return filepath