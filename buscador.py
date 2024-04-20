import unittest

def buscardatos(*args, **kwargs):
    for key, value in kwargs.items():
        esta = True
        for i, n in value.items():
            if n not in args:
                esta = False
        if esta:
            return key
    return "Los datos no se encuentran en la base de datos"
        
database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso",
    },
    "persona2": {
        'primer_nombre': "Juan",
        "segundo_nombre": "Roman",
        "primer_apellido": "Riquelme",
        "segundo_apellido": "",
    },
    "persona3": {
        "primer_nombre": "Lionel",
        "segundo_nombre": "Andres",
        "primer_apellido": "Messi",
        "segundo_apellido": "Cuccittini",
    }
}


            

buscardatos("Pablo", "Diego", "Ruiz", "Picasso", **database)

class TestKwargs(unittest.TestCase):
    
    def test1(self):
        resultado = buscardatos("Pablo", "Diego", "Ruiz", "Picasso",**database)
        self.assertEqual(resultado, "persona1")
    
    def test_persona_no_cargada(self):
        resultado = buscardatos("Diego", "Armando", "Maradona", "", **database)
        self.assertEqual(resultado, "Los datos no se encuentran en la base de datos")

    def test2(self):
        resultado = buscardatos("Juan", "Roman", "Riquelme", "", **database)
        self.assertEqual(resultado, "persona2")

    def test4(self):
        resultado = buscardatos("Lionel", "Andres", "Messi", "Cuccittini", **database)
        self.assertEqual(resultado, "persona3")

    
unittest.main()