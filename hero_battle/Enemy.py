from typing import overload

class Enemy:
    # class attributes (shared by all instances of the class, for example, constants, a bit like static members)

    # constructor
    def __init__(self, toe: str, hp: int = 10, ad: int = 1) -> None:
        # instance attributes (instance attributes are searched first, if not found, then class attributes are searched)
        print("Enemy constructor called")
        # encapsulation: __type_of_enemy is now private via double underscore, use getters and setters
        self.__type_of_enemy: str = toe
        self.__health_points: int = hp
        self.__attack_damage: int = ad

    def get_type_of_enemy(self) -> str:
        return self.__type_of_enemy

    def get_health_points(self) -> int:
        return self.__health_points

    def set_health_points(self, hp: int) -> None:
        self.__health_points = hp

    def get_attack_damage(self) -> int:
        return self.__attack_damage

    def set_attack_damage(self, ad: int) -> None:
        self.__attack_damage = ad

    def print_info(self):
        print(
            f"{self.get_type_of_enemy()} has {self.get_health_points()} health points and can do an attack of damage {self.get_attack_damage()}"
        )

    def talk(self)->None:
        print(f"I am a {self.get_type_of_enemy()}. Prepare to fight!")

    def walk_forward(self)->None:
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self)->None:
        print(f"{self.__type_of_enemy} attacks for damage of {self.__attack_damage}.")

# Zombie inherits from Enemy
class Zombie(Enemy):
    def __init__(self, hp: int, ad:int) -> None:
        super().__init__("Zombie", hp, ad) # super().__init__ has no self

    # method override (polymorphism; same method signature in subclass)
    def talk(self):
        print("The Rangers got zombified in 2012, grrrrrrr")

    # method overloading
    # cannot have overloading like c++ as python is dynamically
    # typed, not statically typed like c++. cannot have methods
    # with the same name, so overloading is achieved differently
    # in python. 

    # method overloading is done using default values the method's
    # parameter list. but CANNOT have type hints if doing this 
    def spread_disease(self, msg=None)->None:
        # python's ternary operator, one-line if statement:
        # XX if condition else YY
        print("The Zombie Rangers are trying to spread disease") if msg==None else print(f"{msg}")

    # or we can use the inbuilt @overload decorator with ellipsis...
    # to create overloaded methods which CAN have type hints 
    @overload 
    def eat_flesh(self) -> None: # signature
        ...

    @overload
    def eat_flesh(self, msg:str) -> None: # signature
        ...

    @overload
    def eat_flesh(self, msg:int) -> None: # signature
        ...

    def eat_flesh(self, msg=None) -> None: # definition
        if msg == None:
           print("no argument: yummy flesh, yum yum, grrrrrrr")
        elif (type(msg)==int):
           print(f"integer argument: {msg}")
        elif (type(msg)==str):
           print(f"string argument: {msg}")
        else:
           print("eat_flesh error")

# Ogre inherits from Enemy
class Ogre(Enemy):
    def __init__(self, hp:int, ad:int) ->None:
        super().__init__("Ogre", hp, ad)

    # method override (polymorphism; method with same signature in subclass)
    def talk(self):
        "Arrrrghhhh, og og og"