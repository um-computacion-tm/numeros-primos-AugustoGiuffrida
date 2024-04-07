import unittest


def is_primo(value):
    # %-->resto
    if value <= 1:  # Si el número es 1 o menor, no es primo
        return False
    for i in range(2, value): #un rango desde el dos hasta el numero elegido
        if value % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False
    return True    #caso contrario devuelve Verdadero
        

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, False)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()