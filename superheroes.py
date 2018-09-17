# superheroes.property

import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        lowest_attack_value = self.attack_strength // 2
        attack_value = random.randint(lowest_attack_value, self.attack_strength)
        return attack_value


    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)


class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for x in self.abilities:
            total += x.attack()
        return total

class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        # print(name)
        # print(self.heroes)
        # print(len(self.heroes))
        found = False
        # hero is the Hero objects. So, we loop through all the objects that's in Hero
        if len(self.heroes) == 0:
            return 0
        for hero in self.heroes:
            # print("remove hero {}".format(hero.name))
            if hero.name == name:
                self.heroes.remove(hero)
                found = True
        if found == False:
            return 0



    def find_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                return hero
            else:
                return 0

    def view_all_heroes(self):
        print(self.heroes)



if __name__ == "__main__":
    hero = Hero("wonder woman")
    print(hero.attack())

    ability = Ability("Divine speed", 300)
    hero.add_ability(ability)
    print(hero.attack())

    new_ability = Ability("Super human strenght", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
