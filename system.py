from experta import *
from PIL import Image

details_of_cars = []
details_map = {}


def preprocess():
    global details_of_cars, details_map
    cars = open("cars.txt")
    cars_all = cars.read()
    cars_list = cars_all.split("\n")
    cars.close()
    for single_car in cars_list:
        s_car_file = open("Cars_details/Cars_info/"+single_car+".txt")
        a = s_car_file.read()
        detail_list = a.split("\n")
        details_of_cars.append(detail_list)
        details_map[str(detail_list)] = single_car
        s_car_file.close()


def identify_car(*args):
    cars_list = []
    for a in args:
        cars_list.append(a)
    return details_map[str(cars_list)]



def if_not_matching(car):
    print("La voiture la plus proche selon votre choix est \"", car, "\"\n")
    im = Image.open("Cars_details/Cars_photos/"+car+".jpg")
    im.show()


class findYourCar(KnowledgeEngine):
    @DefFacts()
    def initial(self):
        print("Bonjour! \n")
        print("Répondez juste aux questions suivantes: (oui/non)\n")

        yield Fact(action="find_car")

    @Rule(Fact(action='find_car'), NOT(Fact(BE=W())), salience=1)
    def Question_0(self):
        self.declare(
            Fact(BE=input("Avez vous un budget élevé ~>")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(BM=W())), salience=1)
    def Question_1(self):
        self.declare(
            Fact(BM=input("Avez vous un budget moyen ~>")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(BF=W())), salience=1)
    def Question_2(self):
        self.declare(
            Fact(BF=input("Avez vous un budget faible ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(CE=W())), salience=1)
    def Question_3(self):
        self.declare(
            Fact(CE=input("Vous voulez que votre voiture consomme l'essence ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(CD=W())), salience=1)
    def Question_4(self):
        self.declare(
            Fact(CD=input(" Vous voulez que votre voiture consomme le diesel ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(P5=W())), salience=1)
    def Question_5(self):
        self.declare(
            Fact(P5=input("Voulez-vous une voiture de 5 places ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(P2=W())), salience=1)
    def Question_6(self):
        self.declare(
            Fact(P2=input("Voulez-vous une voiture de 2 places ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(V2=W())), salience=1)
    def Question_7(self):
        self.declare(
            Fact(V2=input("Voulez-vous une voiture de 2 portes ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(V4=W())), salience=1)
    def Question_8(self):
        self.declare(
            Fact(V4=input("Voulez-vous une voiture de 4 portes ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(A=W())), salience=1)
    def Question_9(self):
        self.declare(
            Fact(A=input(" Voulez-vous une voiture avec une boite de vitesse automatique ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(M=W())), salience=1)
    def Question_10(self):
        self.declare(
            Fact(M=input(" Voulez-vous une voiture avec une boite de vitesse manuelle ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(MA=W())), salience=1)
    def Question_11(self):
        self.declare(
            Fact(MA=input(" Vous voulez des équipement de motorisation avancé ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(SA=W())), salience=1)
    def Question_12(self):
        self.declare(
            Fact(SA=input(" Vous voulez des équipement de sécurité avancé ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(CA=W())), salience=1)
    def Question_13(self):
        self.declare(
            Fact(CA=input(" Vous voulez des équipement de confort avancée ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(C1=W())), salience=1)
    def Question_14(self):
        self.declare(
            Fact(C1=input(" Vous voulez une voiture de couleur Rouge ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(C2=W())), salience=1)
    def Question_15(self):
        self.declare(
            Fact(C2=input(" Vous voulez une voiture de couleur bleu ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(C3=W())), salience=1)
    def Question_16(self):
        self.declare(
            Fact(C3=input(" Vous voulez une voiture de couleur noir ~> ")))  #

    @Rule(Fact(action='find_car'), NOT(Fact(C4=W())), salience=1)
    def Question_17(self):
        self.declare(
            Fact(C4=input(" Vous voulez une voiture de couleur blanc ~> ")))  #

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_1(self):
        self.declare(Fact(car="lamborghini_Rouge"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_2(self):
        self.declare(Fact(car="lamborghini_Bleu"))
        im = Image.open("Cars_details/Cars_photos/lamborghini_Bleu.jpg")
        im.show()
        self.declare(Fact(ClrShowed="yes"))

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_3(self):
        self.declare(Fact(car="lamborghini_Noir"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'), 
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_4(self):
        self.declare(Fact(car="lamborghini_blanc"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_5(self):
        self.declare(Fact(car="ferrari_Rouge"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_6(self):
        self.declare(Fact(car="ferrari_Bleu"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_7(self):
        self.declare(Fact(car="ferrari_Noir"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_8(self):
        self.declare(Fact(car="ferrari_blanc"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_9(self):
        self.declare(Fact(car="porche_Rouge"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_10(self):
        self.declare(Fact(car="porche_Noir"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_11(self):
        self.declare(Fact(car="porche_Bleu"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_12(self):
        self.declare(Fact(car="porche_blanc"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_13(self):
        self.declare(Fact(car="mercedes_Rouge"))
        im = Image.open("")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_14(self):
        self.declare(Fact(car="mercedes_Noir"))
        im = Image.open("")
        im.show()
    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_15(self):
        self.declare(Fact(car="mercedes_Bleu"))
        im = Image.open("")
        im.show()
    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_16(self):
        self.declare(Fact(car="mercedes_Blanc"))
        im = Image.open("")
        im.show()
  
    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_17(self):
        self.declare(Fact(car="range_rover_Rouge"))
        im = Image.open("")
        im.show()
    

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_18(self):
        self.declare(Fact(car="range_rover_Noir"))
        im = Image.open("")
        im.show()


    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_19(self):
        self.declare(Fact(car="range_rover_Bleu"))
        im = Image.open("")
        im.show()


    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_20(self):
        self.declare(Fact(car="range_rover_Blanc"))
        im = Image.open("")
        im.show()


    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_21(self):
        self.declare(Fact(car="BMW_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_22(self):
        self.declare(Fact(car="BMW_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()
     
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_23(self):
        self.declare(Fact(car="BMW_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()
     
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_24(self):
        self.declare(Fact(car="BMW_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()
  
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_25(self):
        self.declare(Fact(car="audi_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_26(self):
        self.declare(Fact(car="audi_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()
 
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_27(self):
        self.declare(Fact(car="audi_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_28(self):
        self.declare(Fact(car="audi_blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_29(self):
        self.declare(Fact(car="wallyscar_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_30(self):
        self.declare(Fact(car="wallyscar_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

 
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_31(self):
        self.declare(Fact(car="wallyscar_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_32(self):
        self.declare(Fact(car="wallyscar_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_33(self):
        self.declare(Fact(car="KIA_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_34(self):
        self.declare(Fact(car="KIA_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()   

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_35(self):
        self.declare(Fact(car="KIA_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show() 
     
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_36(self):
        self.declare(Fact(car="KIA_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_37(self):
        self.declare(Fact(car="mazda_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_38(self):
        self.declare(Fact(car="mazda_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_39(self):
        self.declare(Fact(car="mazda_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_40(self):
        self.declare(Fact(car="mazda_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()


    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_41(self):
        self.declare(Fact(car="peugeot_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_42(self):
        self.declare(Fact(car="peugeot_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_43(self):
        self.declare(Fact(car="peugeot_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_44(self):
        self.declare(Fact(car="peugeot_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_45(self):
        self.declare(Fact(car="volkswagen_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_46(self):
        self.declare(Fact(car="volkswagen_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_47(self):
        self.declare(Fact(car="volkswagen_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2=""),
          Fact(A="non"), Fact(M="oui"), Fact(MA=""),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_48(self):
        self.declare(Fact(car="volkswagen_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_49(self):
        self.declare(Fact(car="renault_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
           Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_50(self):
        self.declare(Fact(car="renault_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
           Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_51(self):
        self.declare(Fact(car="renault_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_52(self):
        self.declare(Fact(car="renault_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_53(self):
        self.declare(Fact(car="fiat_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_54(self):
        self.declare(Fact(car="fiat_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_55(self):
        self.declare(Fact(car="fiat_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()
    
    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_56(self):
        self.declare(Fact(car="fiat_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_57(self):
        self.declare(Fact(car="citroen_Rouge"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_58(self):
        self.declare(Fact(car="citroen_Noir"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_59(self):
        self.declare(Fact(car="citroen_Bleu"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'),
         Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_60(self):
        self.declare(Fact(car="citroen_Blanc"))
        #im = Image.open("C: \Users\Houssem Rouached\Desktop\Projet_IA_Sysexpert\Cars_details\")
        #im.show()

    @Rule(Fact(action='find_car'), Fact(car=MATCH.car), salience=-998)
    def car(self, car):
        a = car
        print("La voiture la plus convenable pour vous est  \""+a+"\"\n")

    @Rule(Fact(action='find_car'),
          Fact(BE=MATCH.BE),
          Fact(BM=MATCH.BM),
          Fact(BF=MATCH.BF),
          Fact(CE=MATCH.CE),
          Fact(CD=MATCH.CD),
          Fact(P5=MATCH.P5),
          Fact(P2=MATCH.P2),
          Fact(V4=MATCH.V4),
          Fact(V2=MATCH.V2),
          Fact(A=MATCH.A),
          Fact(M=MATCH.M),
          Fact(MA=MATCH.MA),
          Fact(SA=MATCH.SA),
          Fact(CA=MATCH.CA),
          Fact(C1=MATCH.C1),
          Fact(C2=MATCH.C2),
          Fact(C3=MATCH.C3),
          Fact(C4=MATCH.C4),
          NOT(Fact(car=MATCH.car)), salience=-999)
    def not_matched(self, BE, BM, BF, CE, CD, P5, P2, V4, V2, A, M, MA, SA, CA, C1, C2, C3, C4):
        print("Il n'y a pas une voiture pour vos critére ,")
        listofCar = [BE, BM, BF, CE, CD, P5, P2,
                      V4, V2, A, M, MA, SA, CA, C1, C2, C3, C4]
        max_Cart = 0
        max_car = ""
        for key, val in details_map.items():
            Cart = 0
            temp = eval(key)
            for i in range(0, len(listofCar)):
                if (temp[i] == listofCar[i]):
                    Cart = Cart + 1
            if Cart > max_Cart:
                max_Cart = Cart
                max_car = val
        if_not_matching(max_car)


if __name__ == "__main__":
    preprocess()
    engine = findYourCar()
    while (1):
        engine.reset()  # prepare
        engine.run()
        print("Voulez-vous rechoisir une autre voiture")
        if input() == "non":
            print("🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗")
            print("Merci d'avoir passé ce test ")
            print("🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗")
            break
