"""
Napisz klasę Zwierze, w której określisz odpowiednie pola:
- liczba nóg
- liczba oczu
- waga w kg
- sposob wydawania potomstwa na świat
- habitat (wodny, lądowy, wodnolądowy)
- tryb życia (dzienny nocny)

oraz metody:
- sprawdzająca stan przytomności (śpi lub jest aktywne)
- śpij i wybudź się - jako argument podaj godzinę, odwołaj się do trybu życia, żeby określić czy jest to możliwe
- rodź potomstwo - wynikiem ma być jajo lub noworodek

zwierzęta nocne budzą się o 18 a zasypiają o 6 rano (użyj domkniętych przedziałów)
zwierzęta dzienne budzą się o 6 rano a zasypiają o 18 (użyj domkniętych przedziałów)
Ssaki rodzą od 1 do 5 młodych (możesz uwzględnić szczególne przypadki jajorodnych)
Ptaki składają od 1 do 3 jaj
Płazy - dziesiątki jaj
Gady - dziesiątki jaj
Ryby - setki tysięcy jaj
Pajęczaki - dziesiątki do setek
"""
import random

class Animal:
    def __init__(self, legs, eyes, weight, type_of, habitat, lifestyle):
        self.legs = legs
        self.eyes = eyes
        self.weight = weight
        self.type_of = type_of
        self.birth = None  # egg/cub
        self.habitat = habitat
        self.lifestyle = lifestyle  # diurnal/nocturnal
        self.is_conscious = "awake"
        self.the_time = None

    def go_to_sleep(self, time):
        self.the_time = time
        if self.lifestyle.lower() == "diurnal":
            if self.the_time in range(8, 19):
                self.is_conscious = "sleeping"
            else:
                if self.is_conscious == "sleeping":
                    print("Bro, I should be sleeping anyway! ")
                else:
                    self.is_conscious = "sleeping"  # Gdyby wcześniej wywołana była metoda wake_up
                    print("Bro, I'm sleeping already! ")
        elif self.lifestyle.lower() == "nocturnal":
            if self.the_time in range(1, 7) or self.the_time in range(18, 25):
                self.is_conscious = "sleeping"
            else:
                if self.is_conscious == "sleeping":
                    print("Bro, I should be sleeping anyway! ")
                else:
                    self.is_conscious = "sleeping"  # Gdyby wcześniej wywołana była metoda wake_up
                    print("Bro, I'm sleeping already! ")

    def wake_up_man_the_roof_is_on_fire(self, time):
        """
        Ze względu na to, że stan w self.is_councious nie zmienia się automatycznie zależnie od godziny
        muszę dodać dodatkową opcję w tym module w liniach 72/73 oraz 81/82
        """
        self.the_time = time
        if self.lifestyle.lower() == "diurnal":
            if self.the_time not in range(8, 19):
                self.is_conscious = "awake"
            else:
                if self.is_conscious == "awake":
                    print("Bro, I'm awake anyway!")
                else:
                    self.is_conscious = "awake"  # Gdyby wcześniej wywołana była metoda go_to_sleep
                    print("Bro, I'm awake!")
        elif self.lifestyle.lower() == "nocturnal":
            if self.the_time not in range(1, 7) or self.the_time not in range(18, 25):
                self.is_conscious = "awake"
            else:
                if self.is_conscious == "awake":
                    print("Bro, I'm awake anyway!")
                else:
                    self.is_conscious = "awake"  # Gdyby wcześniej wywołana była metoda go_to_sleep
                    print("Bro, I'm awake!")

    def consciousness_checker(self):
        print(self.is_conscious)

    def give_birth_chop_chop(self):
        if self.type_of.lower() == "mammal":
            randomize_mammal = str(random.randint(1, 5))
            if randomize_mammal == "1":
                self.birth = randomize_mammal + " cub"
            else:
                self.birth = randomize_mammal + " cubs"
        elif self.type_of.lower() == "bird":
            randomize_bird = str(random.randint(1, 3))
            if randomize_bird == "1":
                self.birth = randomize_bird + " egg"
            else:
                self.birth = randomize_bird + " eggs"
        elif self.type_of.lower() == "fish":
            randomize_fish = str(random.randint(100000, 500000))
            self.birth = randomize_fish + " eggs"
        elif self.type_of.lower() == "spider":
            randomize_spider = str(random.randint(15, 300))
            self.birth = randomize_spider + " eggs"
        else:
            randomize_else = str(random.randint(10, 90))
            self.birth = randomize_else + " eggs"
        print(f"{self.birth}! Mazel tov!")

    def

bird = Animal("two", "two", "2 kg", "bird", "land", "diurnal")
bird.go_to_sleep(12)
bird.wake_up_man_the_roof_is_on_fire(10)
bird.consciousness_checker()
bird.give_birth_chop_chop()



