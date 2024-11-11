def f():
    print("I am the f function")

def eater(x):
    print("nom nom, i just ate a function")
    print(x.__name__)
    print("what was that? i guess it is still alive inside me?")


eater(f)
