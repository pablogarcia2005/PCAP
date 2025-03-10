class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
    
    def atacar(self, otro_pokemon):
        if otro_pokemon.vida <= 0:
            raise ValueError(f"{otro_pokemon.nombre}  ya no tiene vida.")
        
        daño = self.ataque
        otro_pokemon.vida -= daño
        print(self.nombre ," ataca a " , otro_pokemon.nombre , " y causa " , daño , " puntos de daño y le queda " , otro_pokemon.vida , " de vida")
        if otro_pokemon.vida <= 0:
            print(otro_pokemon.nombre , " ha sido derrotado.")

pikachu = Pokemon("Pikachu", "eléctrico", 100, 20)
charmander = Pokemon("Charmander", "fuego", 80, 15)

pikachu.atacar(charmander)
charmander.atacar(pikachu)      

        