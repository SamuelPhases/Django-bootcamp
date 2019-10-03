def hello():
    print("Hello Mike")

hello()

def hellos(name='Grace'):
    print("Hello {}".format(name))

def returnEm(name):
    return 'Welcome {}'.format(name)

hellos('Mary')

greeting = returnEm('Peter')

print(greeting)