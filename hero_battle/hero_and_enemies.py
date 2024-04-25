from typing import overload
import random

class Enemy:
    # class attributes (shared by all instances of the class, for example, constants, a bit like static members)

    # constructor
    def __init__(self, toe: str, hp: int = 10, ad: int = 1) -> None:
        # instance attributes (instance attributes are searched first, if not found, then class attributes are searched)
        print("Enemy constructor called")
        # encapsulation: __type_of_enemy, __health_points,
        # __attack_damage are now private via double underscore
        # (name mangling). Double underscore name mangling does
        # the following to attributes:
        # _Enemy__type_of_enemy (prepended the underscore
        # classname to the double underscored attribute name).
        # use getters and setters instead
        self.__type_of_enemy: str = toe
        self.__health_points: int = hp
        self.__attack_damage: int = ad

    # getters and setters (using getters and setters is
    # non-pythonic, instead use the in-built
    # @property decorator)
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

    # methods / behaviours
    def print_info(self) -> None:
        print(
            f"{self.get_type_of_enemy()} has {self.get_health_points()} health points and can do an attack of damage {self.get_attack_damage()}"
        )

    def talk(self)->None:
        print(f"I am a {self.get_type_of_enemy()}. Prepare to fight!")

    def walk_forward(self)->None:
        print(f"{self.get_type_of_enemy()} moves closer to you.")

    def attack(self)->None:
        print(f"{self.get_type_of_enemy()} attacks for damage of {self.get_attack_damage()}.")

    # pretend "virtual function" 
    def possible_attribute_change(self) -> None:
        ...

# class Zombie inherits from Enemy
class Zombie(Enemy):
    def __init__(self, hp: int, ad:int) -> None:
        super().__init__("Zombie", hp, ad) # super().__init__ has no self

    # method *OVERRIDE* (polymorphism; same method signature in subclass)
    def talk(self) -> None:
        print("The Rangers got zombified in 2012, grrrrrrr")

    # method __OVERLOADING__
    # cannot have __OVERLOADING__ like c++ as python is dynamically
    # typed, not statically typed like c++. cannot have methods
    # with the same name, so __OVERLOADING__ is achieved differently
    # in python. 

    # method __OVERLOADING__ is done using default values the method's
    # parameter list. but CANNOT have type hints if doing this 
    def spread_disease(self, msg=None)->None:
        # python's ternary operator, one-line if statement:
        # XX if condition else YY
        print("The Zombie Rangers are trying to spread disease") if msg==None else print(f"{msg}")

    # or we can use the inbuilt "@OVERLOAD" decorator with ellipsis (...)
    # to create overloaded methods which CAN have type hints 
    @overload 
    def eat_flesh(self) -> None: # signature
        ...

    @overload
    def eat_flesh(self, msg:str) -> None: # signature with str msg
        ...

    @overload
    def eat_flesh(self, msg:int) -> None: # signature with int msg
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

    def possible_attribute_change(self) -> None:
        will_adapt: bool = random.random() < 0.6
        if will_adapt:
            self.set_health_points(self.get_health_points()+2)
            print("random adaption: zombie health has increased by 2 points")

# class Ogre inherits from Enemy
class Ogre(Enemy):
    def __init__(self, hp:int, ad:int) ->None:
        super().__init__("Ogre", hp, ad)

    # method override (polymorphism; method with same signature in subclass)
    def talk(self) -> None:
        print("Og og og, Princess Fiona, watch me fight, ug ug ug")

    def possible_attribute_change(self) -> None:
        will_adapt: bool = random.random() < 0.2
        if will_adapt:
            self.set_attack_damage(self.get_attack_damage()+1)
            print("random adaption: ogre attack has increased by 1 point")

class Weapon:
    def __init__(self, wt: str, ai: int) -> None:
        self.__typeof = wt
        self.__attack_increase = ai

    # using @property decorator instead of getters and setters
    # much more pythonic
    """
    def get_weapon_type(self) -> str:
        return self.__weapon_type
    def get_attack_increase(self) -> int:
        return self.__attack_increase
    """
    @property # @property is the getter by default
    def typeof(self)-> str:
        return self.__typeof
    @typeof.setter # explicit setter
    def typeof(self, wt: str) -> None:
        self.__typeof = wt

    """
    def set_weapon_type(self, wt: str) -> None:
        self.__weapon_type = wt
    def set_attack_increase(self, ai:int) -> None:
        self.__attack_increase += ai
    """
    @property
    def attack_increase(self)-> int:
        return self.__attack_increase
    @attack_increase.setter
    def attack_increase(self, ai:int) -> None:
        self.__attack_increase += ai

class Hero:
    def __init__(self, hp:int, ad:int, w:Weapon) -> None:
        self.__health_points:int = hp
        self.__attack_damage:int = ad
        self.__weapon: Weapon = w # composition (has-a relationship; hero has a Weapon)
        self.__is_weapon_activated:bool = False # guard inactive

    # __health_points getter and setter
    @property
    def health_points(self) -> int:
            return self.__health_points
    @health_points.setter
    def health_points(self, hp:int) -> None:
        self.__health_points = hp

    # __attack_damage getter and setter
    @property
    def attack_damage(self) -> int:
        return self.__attack_damage
    @attack_damage.setter
    def attack_damage(self, val_in:int) -> None:
        self.__attack_damage = val_in

    # __is_weapon_activated getter and setter
    @property
    def is_weapon_activated(self) -> bool:
        return self.__is_weapon_activated
    @is_weapon_activated.setter
    def is_weapon_activated(self, val_in:bool) -> None:
        self.__is_weapon_activated = val_in

    # __weapon getter and setter
    @property
    def weapon(self) -> Weapon:
        return self.__weapon
    @weapon.setter
    def weapon(self, val_in:Weapon) -> None:
        self.__weapon = val_in

    def use_weapon(self):
        if self.is_weapon_activated: # check if guard active
            pass
        else:
            self.attack_damage += self.weapon.attack_increase
            self.is_weapon_activated = True # guard active

    def attack (self) -> None:   
        print(f"Hero attacks for {self.attack_damage} damage")
