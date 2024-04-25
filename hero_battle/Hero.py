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
