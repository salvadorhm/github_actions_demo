import pytest
import operaciones as op

def test_suma():
    assert op.suma(3,4) == 7
    assert op.suma(10,4) == 14

def test_resta():
    assert op.resta(3,4) == -1
    assert op.resta(10,4) == 6

def test_multiplicacion():
    assert op.multiplicacion(3,4) == 12
    assert op.multiplicacion(10,4) == 40

def test_division():
    assert op.division(3,4) == 0.75
    assert op.division(10,4) == 2.5
    assert op.division(10,0) == None

def test_mayor():
    assert op.mayor(3,4) == 4 # valida el primer numero
    assert op.mayor(10,4) == 10 # valida el segundo numero
    assert op.mayor(4,4) == "iguales" # valida que sean iguales
