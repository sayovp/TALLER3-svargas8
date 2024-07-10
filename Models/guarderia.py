from perro import Perro

perro_1 = Perro("Zeus", "Rottweiler", 45.8, 3)
perro_2 = Perro("Nala", "Golden R.", 8.5, 0)
perro_3 = Perro("Atila", "Alabai", 58.9, 5)

print(perro_1.obtener_nombre())
print(perro_2.obtener_edad())
print(perro_3.obtener_nombre(), perro_3.obtener_edad())
