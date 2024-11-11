"""
_ _ _ _ _ _ _

hrac postupne hada pismenka, kdyz nejake odhali, zobrazi se vsechny jeho vyskyty

1. vypis stav = zbyly pocet pokusu, pismena, _ _ _ _ slovo
"""

class Hangman:
    def __init__(self, word, tries):
        self.word = word
        self.letters_tried = []
        self.tries_left = tries
    
    def game_state(self):
        """Vytisknuti momentalniho stavu hry"""
        if len(self.letters_tried) > 0:
            print("Uz si zkousel tato pismena:", *self.letters_tried)
        else:
            print("Zaciname!")
        
        print("Zbyva ti", self.tries_left, "pokusu!")
        
        print("Me slovo: ", end="")
        for letter in self.word:
            if letter in self.letters_tried:
                print(letter, end="")
            else:
                print("-", end="")
        print()
        

    def guess_letter(self):
        """Hrac zkusi pismeno"""
        l = input("Typni si pismenko! ")
        while l in l in self.letters_tried:
            print("To si uz zkousel :(")
            l = input("Typni si jine pismenko! ")
        self.letters_tried.append(l)
        self.tries_left -= 1
        
    def turn_evaluation(self):
        if self.letters_tried[-1] in self.word:
            print("Super, trefil si se!")
        else:
            print("Bohuzel, tohle pismenko se v mem slove nevyskytuje...")
    
    def is_over(self):
        all_letters_found = False
        for l in self.letters_tried:
            if l not in self.word:
                break
        else:
            all_letters_found = True
        
        if all_letters_found or self.tries_left == 0:
            return True
        return False
        
            
            


game = Hangman("kolobezka", 10)
while not game.is_over():
    game.game_state()
    game.guess_letter()
    game.turn_evaluation()
