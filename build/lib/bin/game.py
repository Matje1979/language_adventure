import random
import time

class Scene(object):
    
    def enter(self):
        pass
    
class VelikaSoba(Scene):

    def enter(self, player1):

        print """Otvaraju se velika vrata velike sobe.
             U sobi se nalaze bomba i njen brojcanik. 
             Vidis brojilo koje odbrojava tj vreme koje istice na svom satu.
             Pored bombe je tvoj poremeceni zamenik. Govori da je kasno,
             da cemo zajedno eksplodirati jer neces uspeti da pogodis broj 
             koja se sastoji od jedne cifre od jedan do 10. 
             Imas 20 sekundi da pogadjas. 
             Ako uspes, spaseni smo svi, ako ne uspes, dolazi do eksplozije... """
        #Creates a random number.
        code = "%d" % (random.randint(0,11))
        #From this time the programme starts counting.
        start = time.time()
        
        #This while loop will run until 20
        while True:
            
            guess = raw_input("> ")

            if guess == code:
                print """Uspeo si misija se nastavlja, 
                nada za covecanstvo postoji.
                Srecno se nastavlja prica!"""
            #What happens 20 seconds after start?
            elif (time.time() - start) >= 20:
                print "Vreme je isteklo. Dovidjenja!"
                exit(1)
            else:
                print "Greska! Proteklo je %d sekundi." % (time.time() - start)
            
