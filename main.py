import models
from models.personaje import Personaje
from models.daisy import Daisy
from models.kirby import Kirby
from models.shyguy import ShyGuy
from models.toad import Toad
from models.personajeDecorator import PersonajeDecorator
from models.espadaDecorator import EspadaDecorator
from models.hachaDecorator import HachaDecorator
from models.posionDecorator import PosionDecorator
from models.estrellaDecorator import EstrellaDecorator


# enemigo1 = Kirby()
# enemyConEspada = PosionDecorator(enemigo1)
# print(f"ATACANDO DAMANGE {enemyConEspada.defender()}")


def elegir_p() -> Personaje:
    fighter_selected: Personaje = None
    print("------------------------------------------------------------------")
    print("1-. Kirby")
    print("2-. Daisy")
    print("3-. Toad")
    print("4-. ShyGuy")
    personaje = int(input("Eliga un jugador: "))
    if personaje == 1:
        fighter_selected = Kirby()
    if personaje == 2:
        fighter_selected = Daisy()
    if personaje == 3:
        fighter_selected = Toad()
    if personaje == 4:
        fighter_selected = ShyGuy()
    return fighter_selected


def elegirObjeto(personaje: Personaje) -> Personaje:
    objeto = None
    print("-------------------------------------------------------------")
    print("2. Espada")
    print("3. Hacha")
    print("4. Pluma")
    op = int(input("Eliga un objeto: "))
    if op == 2:
        objeto = EstrellaDecorator(personaje)
    if op == 3:
        objeto = EspadaDecorator(personaje)
    if op == 4:
        objeto = HachaDecorator(personaje)
    if op == 5:
        objeto = PosionDecorator(personaje)
        (personaje)
    return objeto


def game():
    enemigo1: Personaje = None
    enemigo2: Personaje = None

    option: int = 0
    while(option != 4):
        print("-----------------------------------------------------")
        print("1-. Seleccionar jugadores")
        print("2-. Escoger Objetos")
        print("3-. Jugar")
        print("4-. Salir")
        option = int(input("Escoja una opcion: "))
        if option == 1:
            print("-------------------------------------------------")
            print("Seleccionar personajes")
            if enemigo1 == None:
                print("Selección del jugador 1")
                enemigo1 = elegir_p()
            if enemigo2 == None:
                print("Selección del jugador 2")
                enemigo2 = elegir_p()
        elif option == 2:
            if enemigo1 != None and enemigo2 != None:
                print("+++++++++++++++++++++++++++++++++++++++++++")
                print("1. Equipar personaje del jugador 1")
                print("2. Equipar personaje del jugador 2")
                op2 = int(input("Porfavor marque el numero de la opcion: "))
                if op2 == 1:
                    enemigo1 = elegirObjeto(enemigo1)
                if op2 == 2:
                    enemigo2 = elegirObjeto(enemigo2)
            else:
                print("No hay jugadores aun")
        elif option == 3:
            p1 = 0
            p2 = 0
            while enemigo1.get_hp() > 0 and enemigo2.get_hp() > 0:
                if enemigo1.get_speed() <= p2:
                    damage = enemigo1.atacar(10)
                    print(f"Jugador 1 attacks!  {damage} damage")
                    enemigo2.reduce_hp(damage)
                    print(f"Jugador 1 HP: {enemigo1.get_hp()}")
                    p1 = 0
                else:
                    p1 += 1
                if enemigo2.get_speed() <= p2:
                    damage = enemigo2.atacar(10)
                    print(f"Jugador 2 attacks! {damage} damage")
                    enemigo1.reduce_hp(damage)
                    print(f"Jugador 2 HP: {enemigo2.get_hp()}")
                    p2 = 0
                else:
                    p2 += 1
            if enemigo1.get_hp() <= 0:
                print("Gana jugador 2")
            if enemigo2.get_hp() <= 0:
                print("Gana jugador 1")

            enemigo1 = None
            enemigo2 = None
