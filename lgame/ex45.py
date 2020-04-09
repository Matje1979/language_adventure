
from sys import exit
import time
import random
import os
import game



#Creates a parent class for the player
class Person(object):

    def __init__(self, name, age, weight, gender):
        
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender

class Player(Person):


    def start(self):
        self.game.play()

class Scene(object):
    
    def enter(self):
        pass

class Uvod(Scene):
        
    def enter(self):
      
        print "Identifikacija:\n"
        #Creats a pause between two priting statements.
        time.sleep(1)

        name = raw_input("Kako se zoves?\n >")
        age = raw_input("Koliko imas godina?\n >")
        weight = raw_input("Koliko si tezak?\n >")
        gender = raw_input("Koji si pol?\n >")

        time.sleep(2)

        print "\nHello %s!\n" % name
        time.sleep(1)
      
        a = raw_input("Izaberi opciju:\n1.Zapocni igru\n 2.Odustani\n")

        if a.lower() == "zapocni igru" or a == "1":
            time.sleep(1)
            #Clears the screan without stopping the game.
            os.system('cls')
            return 'uvodna', Player(name, age, weight, gender)
        else:
            #this command ends the game.
            return exit(1)

class Uvodna(Scene):
    
    def enter(self, player1):
        print """   Godina je 2080. Raketa ujedinjenih nacija nalazi se u susednoj 
             galaksiji u potrazi za planetom na kojoj bi covecanstvo  
             moglo da se nastani. Situacija na Zemlji je vrlo losa. 
             Veci deo leda na polovima je otopljen. Priobalni gradovi su
             uglavnom potopljeni. Zbog epidemija I ratova doslo je do
             smanjenja broja stanovnika. Nije doslo do nuklearnog rata,
             ali preti rat izmedju bogatih I siromasnih jer su bogati resili
             da se otarase siromasnih posto vecinu poslova koji su obavljali
             siromasi I neobrazovani sada obavljaju roboti. Ti si vodja misije.
             Cilj misije je da se istrazi da li je na planeti u susednoj 
             galaksiji moguc zivot. U toku misije medjutim saznajete da se na
             planeti X nalazi velika kolicina supstance XYZ koja je vrlo mocna 
             energetski (cak 10 puta vise od nafte). Tvoj zamenik te hapsi I 
             baca u tamnicu pod izgovorom da si poludeo I da si pretnja za misiju.
             Jedini nacin da se izbavis je da prodjes niz testova opste informisanosti. 
             Imas 15 minuta da predjes sve nivoe.\n"""
        time.sleep(2)
        a = raw_input("When you are ready press 'r' i onda 'Enter'\n")
        if a == 'r':
            time.sleep(1)
            os.system('cls')
            return "vrata1"
        
class Vrata1(Scene):

    def enter(self, player1):

        print """\n  Nalazis se u mracnoj sobi. Prozorcic se otvara,
              i kroz njega ti dlakava ruka daje tanjir pun neki splacina. 
              Ti kazes da zelis da uradis test. Vlasnik dlakave ruke ti kaze 
              da je to Ok ali da moras to da trazis uctivo na Francuskom."""
        time.sleep(2)
        a = raw_input("""Da li ces da kazes:\n1. Je voudrais fair une test!\n ili\n
2.S\'il vous plait une paraplui!?\n""")
        time.sleep(1)
        os.system('cls')
        if a == "Je voudrais fair une test!" or a == "1":
            print "Novo pitanje:\n"
            time.sleep(1)
            b = raw_input("Kako se na Francuskom kaze 'jedna zena'?\n\n")
    
            if b == "une femme":
                print "\nTacan odgovor!\n"
                time.sleep(1)
                return 'vrata2'
            else:
                return 'vrata1'
        else:
            return 'vrata1'

class Vrata2(Scene):

    def enter(self, player1):
        
        time.sleep(1)
        print player1.name
        time.sleep(1)
        print player1.gender
    
        print """      Vrata se otvaraju, mracnim prljavim hodnikom 
              ides do stepenica.Penjes se, ali nakon tridesetak stepenika
              nailazis na zakljucana vrata. Kucas: Cujes glas sa druge strane 
              koji pita na portugalskom:\n"""
        time.sleep(2)
        print "Qui e? Voce es um hommem ou uma mulher?"
        time.sleep(2)
        a = raw_input("Odgovor:")

        if a.lower() == player1.name.lower() + "," + player1.gender.lower():
            if player1.gender.lower() == "f" or player1.gender.lower() == "female":
                time.sleep(1)
                print "Dobrodosla na novi nivo!"
                time.sleep(1)
                os.system('cls')
                return 'vrata3'
            elif player1.gender.lower() == "muski" or player1.gender.lower() == "m":
                time.sleep(1)
                os.system('cls')
                print "Dobrodosao na novi nivo!"
                time.sleep(2)
                os.system('cls')
                return 'vrata3'
            else:
                time.sleep(1)
                return 'vrata1'
        else:
            time.sleep(1)
            return 'vrata1'

class Vrata3(Scene):

    def enter(self, player1):

        print """hodnik vodi do drugih stepenica 
              (sat na tvojoj ruci pokazuje da je proslo x minuta). 
              Nailazis ubrzo na jos jedne sada nesto cistije stepenice. 
              Penjes se I nakon tridesetak stepenika, nailazis na vrata. 
              Kucas, tisina. Udaras. Cujes glas na srpskom: 
              Sta lupas, bolje reci koji je glavni grad kalifornije! """

        c = raw_input("Odgovor: ")
        
        if c.lower() == "sacramento":
            time.sleep(2)
            os.system('cls')
            return 'vrata4'
        elif c.lower() == "los angeles":
            print "Wrong answer! Moras iz pocetka"
            return 'vrata1'
        else:
            print "I don't understand, try again."
            return 'vrata3'

class Vrata4(Scene):

    def enter(self, player1):

        print """Ulazis u novi hodnik koji je sasvim cist. 
              Nailazis opet na stepenice, posle tridesetak stepenika
              opet nailazis na vrata. Na vratima je ekran, 
              i na ekranu se nalazi pitanje:"""
              
        answer = raw_input("""Ko bi prema Platonu trebao da bude vladar 
    idealne drzave 1. Ekonomista\n 2. Filozof?""")

        if answer == "2" or answer.lower() == "filozof":
            print "Tacan odgovor. Ti si bas neki znalac?!"
            time.sleep(2)
            os.system('cls')
            return 'velika soba'
        else:
            print "Greska, probaj ponovo."
            return 'vrata4'
                
                
class Game(object):

    def __init__(self, scene_name):
        self.scene_name = scene_name

    def play(self):
        
        scenes = {'uvod': Uvod(), 'uvodna': Uvodna(),
             'vrata1': Vrata1(),'vrata2': Vrata2(), 
             'vrata3': Vrata3(), 'vrata4': Vrata4(),
             'velika soba': game.VelikaSoba()}
        
        current_scene = scenes.get(self.scene_name)
        current_scene, player1 = current_scene.enter()
        current_scene = scenes.get(current_scene)

        while True:
 
            next_scene = current_scene.enter(player1)
            current_scene = scenes.get(next_scene)

game_play = Game('uvod')
game_play.play()


