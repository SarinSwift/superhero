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
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    # overrides the builtin string function
    # Whenever you want a hero object in string form, it'll call this function
    # this will return 1 name
    def __str__(self):
        return self.name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total = 0
        for x in self.abilities:
            total += x.attack()
        return total

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense.

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        defenses = 0
        if len(self.armors) == 0:
            return 0

        for armor in self.armors:
            defenses += armor.defend()

        if self.health == 0:
            defenses = 0
            return defenses
        else:
            return defenses


    def take_damage(self, damage_amt):
        self.health = self.health - damage_amt
        if self.health <= 0:
            self.deaths += 1

        else:
            return 0


    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_armor(self, name):
        self.armors.append(name)



class Team:
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
        if len(self.heroes) == 0:
            return 0
        for hero in self.heroes:
            if hero.name == name:
                return hero
            else:
                return 0

    def view_all_heroes(self):
        # this iterates through hero objects in the heroes list
        for hero in self.heroes:
            # prints all the names of heros in a list
            print(hero)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        tot_attack_strength = 0
        for hero in self.heroes:
            tot_attack_strength += hero.attack()
            killed_heroes = other_team.defend(tot_attack_strength)

        for hero in self.heroes:
            hero.add_kill(killed_heroes)

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        tot_defence = 0
        count = 0
        for hero in self.heroes:
            # hero.defend() colloects all the heros defense
            tot_defence += hero.defend()
        if damage_amt > tot_defence:
            excess_damage = damage_amt - tot_defence
            num_kills = self.deal_damage(excess_damage)
        return num_kills

    def deal_damage(self, damage):
        # loop through each hero
        # check if the hero health > damage
        if len(self.heroes) != 0:
            damage_per_hero = damage // len(self.heroes)
        else:
            return 0
        count = 0
        for hero in self.heroes:
            if hero.health > damage_per_hero:
                hero.take_damage(damage_per_hero)
            else:
                hero.take_damage(damage_per_hero)
                count += 1
        return count #returns numbers of deaths

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            # might be hero.health ,   not hero.self.health
            hero.health = hero.start_health

    def stats(self):
        print("Ratio of kills to deaths is {}:{}".format(self.kills, self.deaths))

    # def update_kills(self):
    #     for hero in self.heroes:
    #


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        random_defend_value = random.randint(0, self.defense)
        return random_defend_value







if __name__ == "__main__":
    hero = Hero("wonder woman")
    print(hero.attack())

    ability = Ability("Divine speed", 300)
    hero.add_ability(ability)
    print(hero.attack())

    new_ability = Ability("Super human strenght", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
