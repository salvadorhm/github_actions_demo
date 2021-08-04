def suma(x,y)  :
    return x+y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x,y):
    if y==0:
        return None
    return x/y

def mayor(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return 'iguales'
