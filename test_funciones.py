
from funciones import sumar

def test_sumar():
    assert sumar(2,4)==6
    assert sumar(-2,2)==0
    assert sumar(2,5)==7
    
    
# from funciones import primos

# def primos_test():
#     assert primos(5) is True
#     assert primos(6) is False