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
        return 0


    def view_all_heroes(self):
        viewed_heroes = []
        if len(self.heroes) == 0:
            print("No heroes in this team!")
        # this iterates through hero objects in the heroes list
        for hero in self.heroes:
            # prints all the names of heros in a list
            viewed_heroes.append(hero.name)
        print(viewed_heroes)




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
        for hero in self.heroes:
            # hero.defend() colloects all the heros defense
            tot_defence += hero.defend()
        excess_damage = damage_amt - tot_defence
        if excess_damage > 0:
            return self.deal_damage(excess_damage)
        else:
            return 0


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
            hero.health = 100

    def stats(self):
        # print("Ratio of kills to deaths is {}:{}".format(self.kills, self.deaths))
        for hero in self.heroes:
            print(hero.name + "'s ratio of kills to deaths is " + str(hero.kills) + ":" + str(hero.deaths))

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

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        self.team_one = Team(raw_input("input team 1's name: "))
        print("Go {}!!!".format(self.team_one.team_name))

        print("\n")
        hero1 = Hero(raw_input("input a hero's name: "))
        self.team_one.add_hero(hero1)
        print("You have added {} to {}".format(hero1.name, self.team_one.team_name))

        print("\n")
        ability1 = Ability(raw_input("input name of ability: "), input("input ability's attack strength: "))
        hero1.add_ability(ability1)
        print("You have added the ability {} to {}".format(ability1.name, hero1.name))

        print("\n\n")
        hero2 = Hero(raw_input("input a second hero's name: "))
        self.team_one.add_hero(hero2)
        print("You have added {} to {}".format(hero2.name, self.team_one.team_name))

        print("\n")
        ability2 = Ability(raw_input("input name of ability: "), input("input ability's attack strength: "))
        hero2.add_ability(ability2)
        print("You have added the ability {} to {}".format(ability2.name, hero2.name))


    def build_team_two(self):
        print("\n\n")
        self.team_two = Team(raw_input("input team 2's name: "))
        print("Go {}!!!".format(self.team_two.team_name))
        # add the hero
        print("\n")
        hero1 = Hero(raw_input("input a hero's name: "))
        self.team_two.add_hero(hero1)
        print("You have added {} to {}".format(hero1.name, self.team_two.team_name))
        # add the ability
        print("\n")
        ability1 = Ability(raw_input("input name of ability: "), input("input ability's attack strength: "))
        hero1.add_ability(ability1)
        print("You have added the ability {} to {}".format(ability1.name, hero1.name))
        # add armor
        print("\n")
        armor = Armor(raw_input("input name of armor: "), input("input armors attack strenght: "))
        hero1.add_armor(armor)
        print("You have added {} to {}".format(armor.name, hero1.name))

        # add hero 2
        print("\n\n")
        hero2 = Hero(raw_input("input a second hero's name: "))
        self.team_two.add_hero(hero2)
        print("You have added {} to {}".format(hero2.name, self.team_two.team_name))
        # add ability to hero 2
        print("\n")
        ability2 = Ability(raw_input("input name of ability: "), input("input ability's attack strength: "))
        hero2.add_ability(ability2)
        print("You have added the ability {} to {}".format(ability2.name, hero2.name))
        # add armor to hero 2
        print("\n")
        armor2 = Armor(raw_input("input name of armor: "), input("input armors attack strenght: "))
        hero2.add_armor(armor2)
        print("You have added {} to {}".format(armor2.name, hero2.name))

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """
        running = True
        while running:
            deaths_team_one = 0
            for hero in self.team_one.heroes:
                if hero.health <= 0:
                    deaths_team_one += 1
            self.team_one.attack(self.team_two)
            if deaths_team_one == len(self.team_one.heroes):
                running = False

            deaths_team_two = 0
            for hero in self.team_two.heroes:
                if hero.health <= 0:
                    deaths_team_two += 1
            self.team_two.attack(self.team_one)
            if deaths_team_two == len(self.team_two.heroes):
                running = False






    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        # print(self.team_one.team_name + "stats: " + self.team_one.stats())
        # print(self.team_two.team_name + "stats: " + self.team_two.stats())
        print("\n")
        print("Team 1 stats:")
        self.team_one.stats()

        print("\n")
        print("Team 2 stats:")
        self.team_two.stats()






if __name__ == "__main__":

    game_is_running = True
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()

        play_again = raw_input("Would you want to play again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()



    # hero number 1 / 2 abilities / 1 armor
    # hero = Hero("wonder woman")
    # print(hero.attack())
    # ability_hero = Ability("Divine speed", 300)
    # hero.add_ability(ability_hero)
    # print(hero.attack())
    # new_ability_hero = Ability("Super human strenght", 800)
    # hero.add_ability(new_ability_hero)
    # print(hero.attack())
    # armor = Armor("Knife", 100)
    # hero.add_armor(armor)
    # print(hero.defend())

    # hero number 2 / 2 abilities / 1 armor
    # hero_2 = Hero("batman")
    # print(hero_2.attack())
    # ability = Ability("Fly", 300)
    # hero_2.add_ability(ability)
    # print(hero_2.attack())
    # new_ability = Ability("Super kill", 800)
    # hero_2.add_ability(new_ability)
    # print(hero_2.attack())
    # armor = Armor("Bat", 500)
    # hero_2.add_armor(armor)
    # print(hero_2.defend())

    # hero number 3 / 1 ability / no armor
    # hero_3 = Hero("ant")
    # print(hero_3.attack())
    # ability_hero_3 = Ability("Fire", 10)
    # hero_3.add_ability(ability_hero_3)
    # print(hero_3.attack())
    # armor = Armor("Best armor", 4000)
    # hero_3.add_armor(armor)
    # print(hero_3.defend())

    # adding 2 heros to this team
    # team_1 = Team("winning team")
    # team_1.add_hero(hero_2)
    # team_1.add_hero(hero)
    # print(team_1.heroes[0])
    # print(team_1.heroes[1])
    # print(team_1.find_hero("batman"))
    # print(team_1.view_all_heroes()) # ??why does the view_all_heroes print a 'None' after listed all heroes??
    # team_1.revive_heroes()
    # print("\n")

    # adding 1 hero to this team
    # team_2 = Team("losing team")
    # team_2.add_hero(hero_3)
    # print(team_2.view_all_heroes()) # ??why does the view_all_heroes print a 'None' after the listed all heroes??
    # print(team_1.heroes[0].kills)
    # print(team_1.heroes[1].kills)
    # print(team_2.heroes[0].deaths)
