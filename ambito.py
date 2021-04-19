def ambito_test():
    def hacer_local():
        spam = "spam local"
    def hacer_nolocal():
        nonlocal spam
        spam = "spam no local"
    def hacer_global():
        global spam
        spam = "spam global"

    spam = "test spam"
    hacer_local()
    print("desde de asginar la variable local: ", spam)
    hacer_nolocal()
    print("despues de asignar la variable nolocal: ", spam)
    hacer_global()
    print("despues de la asginacion de variable global: ", spam)


ambito_test()
print("el ambito global:", spam)
