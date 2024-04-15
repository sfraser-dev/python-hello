class Enemy:
    # class attributes (shared by all instances of the class, for example, constants, a bit like static members)

    # constructor
    def __init__(self, toe: str, hp: int = 10, ad: int = 1) -> None:
        # instance attributes (instance attributes are searched first, if not found, then class attributes are searched)
        print("Enemy constructor called")
        # encapsulation: __type_of_enemy is now private via double underscore, use getters and setters
        self.__type_of_enemy: str = toe 
        self.health_points: int = hp
        self.attack_damage: int = ad

    def get_type_of_enemy(self) -> str:
        return self.__type_of_enemy

    def set_type_of_enemy(self, toe: str) -> None:
        self.__type_of_enemy = toe

    def print_info(self):
        print(
            f"{self.get_type_of_enemy()} has {self.health_points} health points and can do an attack of damage {self.attack_damage}"
        )

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Prepare to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for damage of {self.attack_damage}.")
