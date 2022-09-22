import pickle

class vehiculo():
    fabricante = None
    velocidad = 100

    def __init__(self, fabricante, velocidad):
        self.fabricante = fabricante
        self.velocidad = velocidad

    def getFabricante(self):
        return self.fabricante

auto = vehiculo("Ford", 200)
f=open("miauto.bin", 'wb')
pickle.dump(auto, f)
f.close()
print("se ha guardado el vehiculo",auto.getFabricante())

f=open('miauto.bin', 'rb')
miauto=pickle.load(f)
f.close()

print(miauto.getFabricante(), "velocidad:", miauto.velocidad)
