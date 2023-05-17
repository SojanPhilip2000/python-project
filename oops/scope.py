def check_scope():
    def dolocal():
        test="local test"

    def dononlocal():
        nonlocal test
        test="non local test"
    def doglobal():
        global test
        test="global test"
    test="default"

    dolocal()
    print("test value after do local: "+ test)
    dononlocal()
    print("test value after do non local: "+ test)
    doglobal()
    print("test value after do global: " + test)

check_scope()
print("test value after main: "+ test)
