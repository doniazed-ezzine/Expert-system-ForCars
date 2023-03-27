from tkinter import messagebox, ttk
from experta import *
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

#definitions d'une liste pour contenir les details des voitures 
details_of_cars = []
details_map = {}

#définition d'interface pricipale 
root = Tk()
#titre de l'interface 
root.title("IntelliCar")
root.iconbitmap("logos.ico")
root.configure(bg='white')


#definition d'une deuxiéme interface 
root_res = tk.Toplevel()
root_res.title("IntelliCar")
root_res.iconbitmap("logos.ico")
root_res.configure(bg='white')



#fonction 'preprocess' qui permet d'identifier et liée les propriétes à une voiture approprié 
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

#fonction qui permet d'ajouter les éléments dans une liste aussi conserve la forme d'itérable.
def identify_car(*args):
    cars_list = []
    for a in args:
        cars_list.append(a)
    return details_map[str(cars_list)]

#fonction qui traite le cas ou iln'ya pas la voiture convenable elle identifie la voiture la plus convenable 
def if_not_matching(car):
    try:
        print("La voiture la plus proche selon votre choix est \"", car, "\"\n")
        im = Image.open("Cars_details/Cars_photos/"+car+".jpg")
        im.show()
        
    except Exception :
        pass

#fonction qui permet la fermeture de l'interface 
def on_closing():
    if messagebox.askokcancel("Quit", "voulez vous Quitter?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


#définition des message nécessaire 
img=PhotoImage(name="header.PNG", file="header.PNG")
btn3=Button(root, image=img ).grid(row=0, column=2, columnspan=2 )


btn4=Button(root_res, image=img ).grid(row=0, column=2, columnspan=2 )
imgg=Image.open('valider.PNG')
image2=imgg.resize((100,50),Image.ANTIALIAS)
newimg=ImageTk.PhotoImage(image2)

imgCancel=Image.open('annuler.PNG')
image2c=imgCancel.resize((100,50),Image.ANTIALIAS)
newimgCancel=ImageTk.PhotoImage(image2c)


#définition de la fonction 'runApp' qui est la fonction pricipale de déclenchement du systéme 
engine = None
def runApp():
    global engine
    engine.reset()
    engine.run()
    


#définition des bouton de délenchement et de fermeture 
btn2=Button(root, image=newimg, command=runApp ).grid(row=8, column=4, columnspan=2 ,rowspan=2 )
btn22=Button(root, image=newimgCancel,command=on_closing).grid(row=10, column=4,pady=10, rowspan=2)



#définition de tous les eléments principale pour la fabrication de l'interface 
myLabel_be = Label(
    root, text="Avez vous un budget élevé (Supérieur à 300M Dinars) ",bg = "white",font = "Verdana 10 italic").grid(row=3, column=2)

lst = ['oui', 'non']
bee = ttk.Combobox(root, values=lst, state='readonly')
bee.grid(row=3, column=3,pady=5 )
bee.set('non')


myLabel_bm = Label(
    root, text="Avez vous un budget moyen (Entre 100M et 300M Dinars) ",bg = "white",font = "Verdana 10 italic").grid(row=4, column=2)
bmm = ttk.Combobox(root, values=lst, state='readonly')
bmm.grid(row=4, column=3 ,pady=5 )
bmm.set('non')


myLabel_bf = Label(
    root, text="Avez vous un budget Faible (Entre 60M et 100M Dinars) ",bg = "white",font = "Verdana 10 italic").grid(row=5, column=2 )
bff = ttk.Combobox(root, values=lst, state='readonly')
bff.grid(row=5, column=3,pady=5 )
bff.set('non')


myLabel_ce = Label(
    root, text="Vous voulez que votre voiture consomme l'essence  ",bg = "white",font = "Verdana 10 italic").grid(row=6, column=2)
cee= ttk.Combobox(root, values=lst, state='readonly')
cee.grid(row=6, column=3,pady=5)
cee.set('non')


myLabel_cd = Label(root, text=" Vous voulez que votre voiture consomme le diesel  ",bg = "white",font = "Verdana 10 italic").grid(row=7, column=2)
cdd = ttk.Combobox(root, values=lst, state='readonly')
cdd.grid(row=7,column=3,pady=5)
cdd.set('non')


myLabel_p5 = Label(root, text="Voulez-vous une voiture de 5 places  ",bg = "white",font = "Verdana 10 italic").grid(row=8, column=2)
pp5 = ttk.Combobox(root, values=lst, state='readonly')
pp5.grid(row=8, column=3,pady=5)
pp5.set('non')

myLabel_p2 = Label(
    root, text="Voulez-vous une voiture de 2 places  ",bg = "white",font = "Verdana 10 italic").grid(row=9, column=2)
pp2 =ttk.Combobox(root, values=lst, state='readonly')
pp2.grid(row=9, column=3,pady=5)
pp2.set('non')


myLabel_v2 = Label(root, text="Voulez-vous une voiture de 2 portes  ",bg = "white",font = "Verdana 10 italic").grid(row=10, column=2)
vv2=ttk.Combobox(root, values=lst, state='readonly')
vv2.grid(row=10, column=3,pady=5)
vv2.set('non')


myLabel_v4 = Label(
    root, text="Voulez-vous une voiture de 4 portes  ",bg = "white",font = "Verdana 10 italic").grid(row=11, column=2)
vv4 =ttk.Combobox(root, values=lst, state='readonly')
vv4.grid(row=11, column=3,pady=5)
vv4.set('non')

myLabel_A = Label(
    root, text=" Voulez-vous une voiture avec une boite de vitesse automatique  ",bg = "white",font = "Verdana 10 italic").grid(row=12, column=2)
aa =ttk.Combobox(root, values=lst, state='readonly')
aa.grid(row=12, column=3,pady=5)
aa.set('non')

myLabel_m = Label(
    root, text="  Voulez-vous une voiture avec une boite de vitesse manuelle",bg = "white",font = "Verdana 10 italic").grid(row=13, column=2)
mm=ttk.Combobox(root, values=lst, state='readonly')
mm.grid(row=13, column=3,pady=5)
mm.set('non')

myLabel_ma = Label(
    root, text=" Vous voulez des équipement de motorisation avancé   ",bg = "white",font = "Verdana 10 italic").grid(row=14, column=2)
maa =ttk.Combobox(root, values=lst, state='readonly')
maa.grid(row=14, column=3,pady=5)
maa.set('non')

myLabel_sa = Label(
    root, text=" Vous voulez des équipement de sécurité avancé  " ,bg = "white",font = "Verdana 10 italic").grid(row=15, column=2)
saa =ttk.Combobox(root, values=lst, state='readonly')
saa.grid(row=15, column=3,pady=5)
saa.set('non')

myLabel_ca = Label(
    root, text=" Vous voulez des équipement de confort avancée  " ,bg = "white",font = "Verdana 10 italic").grid(row=16, column=2)
caa = ttk.Combobox(root, values=lst, state='readonly')
caa.grid(row=16, column=3,pady=5)
caa.set('non')

myLabel_c1 = Label(
    root, text=" Vous voulez une voiture de couleur Rouge  ",bg = "white",font = "Verdana 10 italic").grid(row=17, column=2)
cc1 = ttk.Combobox(root, values=lst, state='readonly')
cc1.grid(row=17, column=3,pady=5)
cc1.set('non')


myLabel_c2 = Label(
    root, text=" Vous voulez une voiture de couleur Noir  " ,bg = "white",font = "Verdana 10 italic").grid(row=18, column=2)
cc2 = ttk.Combobox(root, values=lst, state='readonly')
cc2.grid(row=18, column=3, pady=5)
cc2.set('non')

myLabel_c3 = Label(
    root, text=" Vous voulez une voiture de couleur Bleu ",bg = "white",font = "Verdana 10 italic").grid(row=19, column=2)
cc3 = ttk.Combobox(root, values=lst, state='readonly')
cc3.grid(row=19, column=3, pady=5)
cc3.set('non')

myLabel_c4 = Label(
    root, text=" Vous voulez une voiture de couleur Blanche  ",bg = "white",font = "Verdana 10 italic").grid(row=20, column=2)
cc4 = ttk.Combobox(root, values=lst, state='readonly')
cc4.grid(row=20, column=3,   pady=5)
cc4.set('non')

#image du footer de l'interrface 
imgfooter=PhotoImage( file="footer.PNG")
largeur = imgfooter.width()  
hauteur = imgfooter.height()
lablimg2=Label(root, image=imgfooter).grid(row=21, column=2, columnspan=2 )



#class 'findYourCar' qui contient les régles et leur liasion 
class findYourCar(KnowledgeEngine):
    @DefFacts()
    def initial(self):

        yield Fact(action="find_car")

    @Rule(Fact(action='find_car'), NOT(Fact(BE=bee.get())), salience=1)
    def Question_0(self):
        self.declare(
            Fact(BE=bee.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(BM=bmm.get())), salience=1)
    def Question_1(self):
        self.declare(
            Fact(BM=bmm.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(BF=bff.get())), salience=1)
    def Question_2(self):
        self.declare(
            Fact(BF=bff.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(CE=cee.get())), salience=1)
    def Question_3(self):
        self.declare(
            Fact(CE=cee.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(CD=cdd.get())), salience=1)
    def Question_4(self):
        self.declare(
            Fact(CD=cdd.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(P5=pp5.get())), salience=1)
    def Question_5(self):
        self.declare(
            Fact(P5=pp5.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(P2=pp2.get())), salience=1)
    def Question_6(self):
        self.declare(
            Fact(P2=pp2.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(V2=vv2.get())), salience=1)
    
    def Question_7(self):
        self.declare(
            Fact(V2=vv2.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(V4=vv4.get())), salience=1)
    def Question_8(self):
        self.declare(
            Fact(V4=vv4.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(A=aa.get())), salience=1)
    def Question_9(self):
        self.declare(
            Fact(A=aa.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(M=mm.get())), salience=1)
    def Question_10(self):
        self.declare(
            Fact(M=mm.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(MA=maa.get())), salience=1)
    def Question_11(self):
        self.declare(
            Fact(MA=maa.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(SA=saa.get())), salience=1)
    def Question_12(self):
        self.declare(
            Fact(SA=saa.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(CA=caa.get())), salience=1)
    def Question_13(self):
        self.declare(
            Fact(CA=caa.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(C1=cc1.get())), salience=1)
    def Question_14(self):
        self.declare(
            Fact(C1=cc1.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(C2=cc2.get())), salience=1)
    def Question_15(self):
        self.declare(
            Fact(C2=cc2.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(C3=cc3.get())), salience=1)
    def Question_16(self):
        self.declare(
            Fact(C3=cc3.get()))

    @Rule(Fact(action='find_car'), NOT(Fact(C4=cc4.get())), salience=1)
    def Question_17(self):
        self.declare(
            Fact(C4=cc4.get()))

        

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_1(self):
        self.declare(Fact(car="lamborghini_Rouge La Lamborghini est une marque de voitures de sport italienne connue  pour ses modèles de voitures de luxe ultra-performantes .\n La société a été fondée en 1963 par Ferruccio Lamborghini, un entrepreneur italien passionné de voitures de sport.\n Depuis, la marque a connu un grand succès grâce à ses voitures emblématiques, telles que la Lamborghini Countach, la Lamborghini Diablo et la Lamborghini Murciélago.\n Les voitures Lamborghini sont généralement équipées de moteurs V12 puissants et de technologies de pointe,\n ce qui leur permet d atteindre des vitesses élevées et d offrir une expérience de conduite intense.\n De plus, les voitures Lamborghini sont reconnues pour leur design audacieux et distinctif, avec des lignes agressives et des couleurs vives.\n En résumé, la Lamborghini est une marque de voitures de sport de haute performance et de luxe,\n reconnue pour ses moteurs puissants, \n ses technologies avancées et son design unique.\n"))
        
        canv = Canvas(root_res, width=80, height=80, bg='white')
        canv.grid(row=2, column=3)

        img2 = ImageTk.PhotoImage(Image.open("Cars_details/Cars_photos/lamborghini_Bleu.jpg"))  # PIL solution
        canv.create_image(20, 20, anchor=NW, image=img2)

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_2(self):
        self.declare(Fact(car="lamborghini_Noir La Lamborghini est une marque de voitures de sport italienne connue  pour ses modèles de voitures de luxe ultra-performantes .\n La société a été fondée en 1963 par Ferruccio Lamborghini, un entrepreneur italien passionné de voitures de sport.\n Depuis, la marque a connu un grand succès grâce à ses voitures emblématiques, telles que la Lamborghini Countach, la Lamborghini Diablo et la Lamborghini Murciélago.\n Les voitures Lamborghini sont généralement équipées de moteurs V12 puissants et de technologies de pointe,\n ce qui leur permet d atteindre des vitesses élevées et d offrir une expérience de conduite intense.\n De plus, les voitures Lamborghini sont reconnues pour leur design audacieux et distinctif, avec des lignes agressives et des couleurs vives.\n En résumé, la Lamborghini est une marque de voitures de sport de haute performance et de luxe,\n reconnue pour ses moteurs puissants, \n ses technologies avancées et son design unique.\n"))
        img = PhotoImage(file="Cars_details/Cars_photos/lamborghini_Noir.jpg")
        btn2=Button(root_res, image=img).grid(row=0, column=2, columnspan=2 )
        

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_3(self):
        self.declare(Fact(car="lamborghini_bleu  La Lamborghini est une marque de voitures de sport italienne connue  pour ses modèles de voitures de luxe ultra-performantes .\n La société a été fondée en 1963 par Ferruccio Lamborghini, un entrepreneur italien passionné de voitures de sport.\n Depuis, la marque a connu un grand succès grâce à ses voitures emblématiques, telles que la Lamborghini Countach, la Lamborghini Diablo et la Lamborghini Murciélago.\n Les voitures Lamborghini sont généralement équipées de moteurs V12 puissants et de technologies de pointe,\n ce qui leur permet d atteindre des vitesses élevées et d offrir une expérience de conduite intense.\n De plus, les voitures Lamborghini sont reconnues pour leur design audacieux et distinctif, avec des lignes agressives et des couleurs vives.\n En résumé, la Lamborghini est une marque de voitures de sport de haute performance et de luxe,\n reconnue pour ses moteurs puissants, \n ses technologies avancées et son design unique.\n"))
        im = Image.open("Cars_details/Cars_photos/lamborghini_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_4(self):
        self.declare(Fact(car="lamborghini_Blanc La Lamborghini est une marque de voitures de sport italienne connue  pour ses modèles de voitures de luxe ultra-performantes .\n La société a été fondée en 1963 par Ferruccio Lamborghini, un entrepreneur italien passionné de voitures de sport.\n Depuis, la marque a connu un grand succès grâce à ses voitures emblématiques, telles que la Lamborghini Countach, la Lamborghini Diablo et la Lamborghini Murciélago.\n Les voitures Lamborghini sont généralement équipées de moteurs V12 puissants et de technologies de pointe,\n ce qui leur permet d atteindre des vitesses élevées et d offrir une expérience de conduite intense.\n De plus, les voitures Lamborghini sont reconnues pour leur design audacieux et distinctif, avec des lignes agressives et des couleurs vives.\n En résumé, la Lamborghini est une marque de voitures de sport de haute performance et de luxe,\n reconnue pour ses moteurs puissants, \n ses technologies avancées et son design unique.\n"))
        im = Image.open("Cars_details/Cars_photos/lamborghini_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_5(self):
        self.declare(Fact(car="ferrari_Rouge sa référence est FERRARI PUROSANGUE sa prix est 980.000 DT \n La Ferrari est une voiture de sport prestigieuse et performante.\n Elle est reconnue pour son design élégant et sportif, avec des lignes fluides\n et des détails caractéristiques tels que sa calandre en forme de cheval cabré et ses feux arrière en forme de boomerang.\nSous le capot, la Ferrari est équipée d un moteur V8 ou V12 puissant et performant,\n capable de délivrer des performances impressionnantes sur route et sur circuit. \nLa voiture est également dotée d'un châssis léger et rigide,\n d'une transmission manuelle ou automatique à double embrayage et d une suspension sportive adaptée à des performances de haut niveau.\nEn termes de confort et de technologie, la Ferrari offre une expérience de conduite de haut niveau grâce à ses sièges en cuir confortables,\n à son volant sport multifonction et à sa console centrale intuitive. \nLa voiture est également équipée d'un système audio haute fidélité,\n d'un système de navigation et d'un écran tactile pour un accès facile aux différentes fonctions.\nEn résumé, la Ferrari est une voiture de sport de haut niveau,\n capable de combiner performances exceptionnelles, confort de conduite et technologie de pointe."))
        im = Image.open("Cars_details/Cars_photos/ferrari_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_6(self):
        self.declare(Fact(car="ferrari_Noir sa référence est FERRARI PUROSANGUE sa prix est 980.000 DT \n La Ferrari est une voiture de sport prestigieuse et performante.\n Elle est reconnue pour son design élégant et sportif, avec des lignes fluides\n et des détails caractéristiques tels que sa calandre en forme de cheval cabré et ses feux arrière en forme de boomerang.\nSous le capot, la Ferrari est équipée d un moteur V8 ou V12 puissant et performant,\n capable de délivrer des performances impressionnantes sur route et sur circuit. \nLa voiture est également dotée d'un châssis léger et rigide,\n d'une transmission manuelle ou automatique à double embrayage et d une suspension sportive adaptée à des performances de haut niveau.\nEn termes de confort et de technologie, la Ferrari offre une expérience de conduite de haut niveau grâce à ses sièges en cuir confortables,\n à son volant sport multifonction et à sa console centrale intuitive. \nLa voiture est également équipée d'un système audio haute fidélité,\n d'un système de navigation et d'un écran tactile pour un accès facile aux différentes fonctions.\nEn résumé, la Ferrari est une voiture de sport de haut niveau,\n capable de combiner performances exceptionnelles, confort de conduite et technologie de pointe."))
        im = Image.open("Cars_details/Cars_photos/ferrari_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_7(self):
        self.declare(Fact(car="ferrari_Bleu sa  référence est FERRARI PUROSANGUE sa prix est 980.000 DT \n La Ferrari est une voiture de sport prestigieuse et performante.\n Elle est reconnue pour son design élégant et sportif, avec des lignes fluides\n et des détails caractéristiques tels que sa calandre en forme de cheval cabré et ses feux arrière en forme de boomerang.\nSous le capot, la Ferrari est équipée d un moteur V8 ou V12 puissant et performant,\n capable de délivrer des performances impressionnantes sur route et sur circuit. \nLa voiture est également dotée d'un châssis léger et rigide,\n d'une transmission manuelle ou automatique à double embrayage et d une suspension sportive adaptée à des performances de haut niveau.\nEn termes de confort et de technologie, la Ferrari offre une expérience de conduite de haut niveau grâce à ses sièges en cuir confortables,\n à son volant sport multifonction et à sa console centrale intuitive. \nLa voiture est également équipée d'un système audio haute fidélité,\n d'un système de navigation et d'un écran tactile pour un accès facile aux différentes fonctions.\nEn résumé, la Ferrari est une voiture de sport de haut niveau,\n capable de combiner performances exceptionnelles, confort de conduite et technologie de pointe."))
        im = Image.open("Cars_details/Cars_photos/ferrari_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="non"),
          Fact(P2="oui"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_8(self):
        self.declare(Fact(car="ferrari_Blanc sa référence est FERRARI PUROSANGUE sa prix est 980.000 DT \n La Ferrari est une voiture de sport prestigieuse et performante.\n Elle est reconnue pour son design élégant et sportif, avec des lignes fluides\n et des détails caractéristiques tels que sa calandre en forme de cheval cabré et ses feux arrière en forme de boomerang.\nSous le capot, la Ferrari est équipée d un moteur V8 ou V12 puissant et performant,\n capable de délivrer des performances impressionnantes sur route et sur circuit. \nLa voiture est également dotée d'un châssis léger et rigide,\n d'une transmission manuelle ou automatique à double embrayage et d une suspension sportive adaptée à des performances de haut niveau.\nEn termes de confort et de technologie, la Ferrari offre une expérience de conduite de haut niveau grâce à ses sièges en cuir confortables,\n à son volant sport multifonction et à sa console centrale intuitive. \nLa voiture est également équipée d'un système audio haute fidélité,\n d'un système de navigation et d'un écran tactile pour un accès facile aux différentes fonctions.\nEn résumé, la Ferrari est une voiture de sport de haut niveau,\n capable de combiner performances exceptionnelles, confort de conduite et technologie de pointe."))
        im = Image.open("Cars_details/Cars_photos/ferrari_Blanc.jpg")
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
        im = Image.open("Cars_details/Cars_photos/porche_Rouge.jpg")
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
        im = Image.open("Cars_details/Cars_photos/porche_Noir.jpg")
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
        im = Image.open("Cars_details/Cars_photos/porche_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="oui"), Fact(BM="non"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_12(self):
        self.declare(Fact(car="porche_Blanc"))
        im = Image.open("Cars_details/Cars_photos/porche_Blanc.jpg")
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
        im = Image.open("Cars_details/Cars_photos/mercedes_Rouge.jpg")
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
        im = Image.open("Cars_details/Cars_photos/mercedes_Noir.jpg")
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
        im = Image.open("Cars_details/Cars_photos/mercedes_Bleu.jpg")
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
        im = Image.open("Cars_details/Cars_photos/mercedes_Blanc.jpg")
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
        im = Image.open("Cars_details/Cars_photos/range_rover_Rouge.jpg")
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
        im = Image.open("Cars_details/Cars_photos/range_rover_Noir.jpg")
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
        im = Image.open("Cars_details/Cars_photos/Bleu.jpg")
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
        im = Image.open("Cars_details/Cars_photos/range_rover_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_21(self):
        self.declare(Fact(car="BMW_Rouge \n BMW M4  est une marque allemande de voitures de luxe connue pour ses modèles \nà haute performance \net son design élégant. \nLa société a été fondée en 1916 et est basée à Munich, en Allemagne.\n BMW se distingue par sa technologie de pointe et ses innovations en matière de sécurité et de conduite. \nLes voitures BMW sont réputées pour leur agilité et leur maniabilité sur la route, ainsi que pour leur confort et leur performance exceptionnels.\n La gamme de voitures BMW comprend des berlines, des coupés, des cabriolets, \n des SUV et des véhicules électriques."))
        im = Image.open("Cars_details/Cars_photos/BMW_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_22(self):
        self.declare(Fact(car="BMW_Noir \n BMW M4  est une marque allemande de voitures de luxe connue pour ses modèles \nà haute performance \net son design élégant. \nLa société a été fondée en 1916 et est basée à Munich, en Allemagne.\n BMW se distingue par sa technologie de pointe et ses innovations en matière de sécurité et de conduite. \nLes voitures BMW sont réputées pour leur agilité et leur maniabilité sur la route, ainsi que pour leur confort et leur performance exceptionnels.\n La gamme de voitures BMW comprend des berlines, des coupés, des cabriolets, \n des SUV et des véhicules électriques."))
        im = Image.open("Cars_details/Cars_photos/BMW_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_23(self):
        self.declare(Fact(car="BMW_Bleu  \n BMW M4  est une marque allemande de voitures de luxe connue pour ses modèles \nà haute performance \net son design élégant. \nLa société a été fondée en 1916 et est basée à Munich, en Allemagne.\n BMW se distingue par sa technologie de pointe et ses innovations en matière de sécurité et de conduite. \nLes voitures BMW sont réputées pour leur agilité et leur maniabilité sur la route, ainsi que pour leur confort et leur performance exceptionnels.\n La gamme de voitures BMW comprend des berlines, des coupés, des cabriolets, \n des SUV et des véhicules électriques."))
        im = Image.open("Cars_details/Cars_photos/BMW_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_24(self):
        self.declare(Fact(car="BMW_Blanc sa référence est BMW M4 sa prix = 199.999 DT  \n BMW est une marque allemande de voitures de luxe connue pour ses modèles \nà haute performance \net son design élégant. \nLa société a été fondée en 1916 et est basée à Munich, en Allemagne.\n BMW se distingue par sa technologie de pointe et ses innovations en matière de sécurité et de conduite. \nLes voitures BMW sont réputées pour leur agilité et leur maniabilité sur la route, ainsi que pour leur confort et leur performance exceptionnels.\n La gamme de voitures BMW comprend des berlines, des coupés, des cabriolets, \n des SUV et des véhicules électriques."))
        im = Image.open("Cars_details/Cars_photos/BMW_Rouge.jpg")
        im = Image.open("Cars_details/Cars_photos/BMW_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_25(self):
        self.declare(Fact(car="audi_Rouge"))
        im = Image.open("Cars_details/Cars_photos/audi_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_26(self):
        self.declare(Fact(car="audi_Noir"))
        im = Image.open("Cars_details/Cars_photos/audi_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_27(self):
        self.declare(Fact(car="audi_Bleu"))
        im = Image.open("Cars_details/Cars_photos/audi_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_28(self):
        self.declare(Fact(car="audi_Blanc"))
        im = Image.open("Cars_details/Cars_photos/audi_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_29(self):
        self.declare(Fact(car="wallyscar_Rouge"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_30(self):
        self.declare(Fact(car="wallyscar_Noir"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="oui"), Fact(C4="non"))
    def car_31(self):
        self.declare(Fact(car="wallyscar_Bleu"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="oui"))
    def car_32(self):
        self.declare(Fact(car="wallyscar_Blanc"))
        im = Image.open("Cars_details/Cars_photos/wallyscar_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_33(self):
        self.declare(Fact(car="KIA_Rouge"))
        im = Image.open("Cars_details/Cars_photos/KIA_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_34(self):
        self.declare(Fact(car="KIA_Noir"))
        im = Image.open("Cars_details/Cars_photos/KIA_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_35(self):
        self.declare(Fact(car="KIA_Noir"))
        im = Image.open("Cars_details/Cars_photos/KIA_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_36(self):
        self.declare(Fact(car="KIA_Blanc"))
        im = Image.open("Cars_details/Cars_photos/KIA_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_37(self):
        self.declare(Fact(car="mazda_Rouge"))
        im = Image.open("Cars_details/Cars_photos/mazda_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_38(self):
        self.declare(Fact(car="mazda_Noir"))
        im = Image.open("Cars_details/Cars_photos/mazda_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_39(self):
        self.declare(Fact(car="mazda_Bleu"))
        im = Image.open("Cars_details/Cars_photos/mazda_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="oui"), Fact(BF="non"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="oui"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_40(self):
        self.declare(Fact(car="mazda_Blanc"))
        im = Image.open("Cars_details/Cars_photos/mazda_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_41(self):
        self.declare(Fact(car="peugeot_Rouge"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_42(self):
        self.declare(Fact(car="peugeot_Noir"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_43(self):
        self.declare(Fact(car="peugeot_Bleu"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_44(self):
        self.declare(Fact(car="peugeot_Blanc"))
        im = Image.open("Cars_details/Cars_photos/peugeot_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
         Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_45(self):
        self.declare(Fact(car="volkswagen_Rouge"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_46(self):
        self.declare(Fact(car="volkswagen_Noir"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_47(self):
        self.declare(Fact(car="volkswagen_Bleu"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
         Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="oui"), Fact(CD="non"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="oui"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_48(self):
        self.declare(Fact(car="volkswagen_Blanc"))
        im = Image.open("Cars_details/Cars_photos/volkswagen_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_49(self):
        self.declare(Fact(car="renault_Rouge"))
        im = Image.open("Cars_details/Cars_photos/renault_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_50(self):
        self.declare(Fact(car="renault_Noir"))
        im = Image.open("Cars_details/Cars_photos/renault_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_51(self):
        self.declare(Fact(car="renault_Bleu"))
        im = Image.open("Cars_details/Cars_photos/renault_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="oui"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_52(self):
        self.declare(Fact(car="renault_Blanc"))
        im = Image.open("Cars_details/Cars_photos/renault_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_53(self):
        self.declare(Fact(car="fiat_Rouge"))
        im = Image.open("Cars_details/Cars_photos/fiat_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_54(self):
        self.declare(Fact(car="fiat_Noir"))
        im = Image.open("Cars_details/Cars_photos/fiat_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_55(self):
        self.declare(Fact(car="fiat_Bleu : sa référence est  FIAT 500 sa prix = 62 500 DT \n La Fiat est une voiture italienne, célèbre pour son design élégant et son confort de conduite.\n Elle offre une gamme de modèles adaptés à tous les besoins, du petit citadin au grand familial.\n Sa technologie avancée et ses performances dynamiques en font une voiture fiable et agréable à conduire.\n Son intérieur est soigné et bien pensé, avec des matériaux de qualité et des équipements modernes.\n La Fiat est une voiture idéale pour les conducteurs à la recherche d'un véhicule à la fois esthétique et fonctionnel.\n"))
        im = Image.open("Cars_details/Cars_photos/fiat_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="non"), Fact(V2="oui"),
          Fact(A="non"), Fact(M="oui"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_56(self):
        self.declare(Fact(car="fiat_Blanc"))
        im = Image.open("Cars_details/Cars_photos/fiat_Blanc.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="oui"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="non"))
    def car_57(self):
        self.declare(Fact(car="citroen_Rouge"))
        im = Image.open("Cars_details/Cars_photos/citroen_Rouge.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="oui"), Fact(C3="non"), Fact(C4="non"))
    def car_58(self):
        self.declare(Fact(car="citroen_Noir"))
        im = Image.open("Cars_details/Cars_photos/citroen_Noir.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"), Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="oui"), Fact(C4="non"))
    def car_59(self):
        self.declare(Fact(car="citroen_Bleu"))
        im = Image.open("Cars_details/Cars_photos/citroen_Bleu.jpg")
        im.show()

    @Rule(Fact(action='find_car'),
          Fact(BE="non"), Fact(BM="non"), Fact(BF="oui"),
          Fact(CE="non"), Fact(CD="oui"), Fact(P5="oui"),
          Fact(P2="non"), Fact(V4="oui"), Fact(V2="non"),
          Fact(A="oui"), Fact(M="non"),   Fact(MA="non"),
          Fact(SA="non"), Fact(CA="non"), Fact(C1="non"),
          Fact(C2="non"), Fact(C3="non"), Fact(C4="oui"))
    def car_60(self, car):
        self.declare(Fact(car="citroen_Blanc"))
        #print("La voiture convenable pour vous est  \""+car+"\"\n")
        im = Image.open("Cars_details/Cars_photos/citroen_Blanc.jpg")
        im.show()

    #la régle qui permet de matcher les voiture et les propriétés afin d'identifier la voiture convenable 
    @Rule(Fact(action='find_car'), Fact(car=MATCH.car), salience=-998)
    def car(self, car):
        root_res = tk.Toplevel()
        root_res.title("IntelliCar")
        root_res.iconbitmap("logos.ico")
        root_res.configure(bg='white')
        a = car
        Label_res=Label(root_res,text="La voiture convenable pour vous est  \""+a+"\"\n").grid(row=1,column=1)
        
     
        
    #la fonction qui permet d'identifier la voiture  la plus proche 
    @Rule()
    def not_matched(self):
        print("Il n'y a pas une voiture pour vos critére ,")
        listofcar = [bee.get(), bmm.get(), bff.get(), cee.get(), cdd.get(), pp5.get(), pp2.get(),
                     vv4.get(), vv2.get(), aa.get(), mm.get(), maa.get(), saa.get(), caa.get(), cc1.get(), cc2.get(), cc3.get(),
                    cc4.get()]
        
        listCarsDetails = [["oui", "non", "non", "oui", "non", "non", "oui", "non", "oui", "oui", "non", "oui",
                            "non", "non", "oui", "non", "non", "non"],
                           ["oui", "non", "non", "oui", "non", "non", "oui", "non", "oui", "oui", "non", "oui",
                            "non", "non", "non", "oui", "non", "non"],
                           ["oui", "non", "non", "oui", "non", "non", "oui", "non", "oui", "oui", "non", "oui",
                            "non", "non", "non", "non", "oui", "non"],
                           ["oui", "non", "non", "oui", "non", "non", "oui", "non", "oui", "oui", "non", "oui",
                            "non", "non", "non", "non", "non", "oui"],
                           ["oui", "non", "non", "non", "oui", "non", "oui", "non", "oui",
                               "non", "oui", "oui", "non", "non", "oui", "non", "non", "non"],
                           ["oui", "non", "non", "non", "oui", "non", "oui", "non", "oui",
                               "non", "oui", "oui", "non", "non", "non", "oui", "non", "non"],
                           ["oui", "non", "non", "non", "oui", "non", "oui", "non", "oui",
                               "non", "oui", "oui", "non", "non", "non", "non", "oui", "non"],
                           ["oui", "non", "non", "non", "oui", "non", "oui", "non", "oui",
                               "non", "oui", "oui", "non", "non", "non", "non", "non", "oui"],
                           ["oui", "non", "non", "non", "oui", "oui", "non",
                            "oui", "non", "oui", "non", "non", "oui", "oui", "oui", "non", "non", "non"],
                           ["oui", "non", "non", "non", "oui", "oui", "non",
                            "oui", "non", "oui", "non", "non", "oui", "oui", "non", "oui", "non", "non"],
                           ["oui", "non", "non", "non", "oui", "oui", "non",
                            "oui", "non", "oui", "non", "non", "oui", "oui", "non", "non", "oui", "non"],
                           ["oui", "non", "non", "non", "oui", "oui", "non",
                            "oui", "non", "oui", "non", "non", "oui", "oui", "non", "non", "non", "oui"],
                           # aprés porshe
                           ["oui", "non", "non", "oui", "non", "oui", "non", "oui", "non",
                               "oui", "non", "non", "non", "oui", "oui", "non", "non", "non"],
                           ["oui", "non", "non", "oui", "non", "oui", "non", "oui", "non",
                            "oui", "non", "non", "non", "oui", "non", "oui", "non", "non"],
                           ["oui", "non", "non", "oui", "non", "oui", "non", "oui", "non",
                            "oui", "non", "non", "non", "oui", "non", "non", "oui", "non"],
                           ["oui", "non", "non", "oui", "non", "oui", "non", "oui", "non",
                            "oui", "non", "non", "non", "oui", "non", "non", "non", "oui"],
                           # aprés mercedes
                           ["oui", "non", "non", "non", "oui", "oui", "non", "oui", "non",
                               "non", "oui", "oui", "oui", "oui", "oui", "non", "non", "non"],
                           ["oui", "non", "non", "non", "oui", "oui", "non", "oui", "non",
                            "non", "oui", "oui", "oui", "oui", "non", "oui", "non", "non"],
                           ["oui", "non", "non", "non", "oui", "oui", "non", "oui", "non",
                            "non", "oui", "oui", "oui", "oui", "non", "non", "oui", "non"],
                           ["oui", "non", "non", "non", "oui", "oui", "non", "oui", "non",
                            "non", "oui", "oui", "oui", "oui", "non", "non", "non", "oui"],
                           # aprés range
                           ["non", "oui", "non", "oui", "non", "oui", "non", "non", "oui",
                               "non", "oui", "non", "non", "non", "oui", "non", "non", "non"],
                           ["non", "oui", "non", "oui", "non", "oui", "non", "non", "oui",
                            "non", "oui", "non", "non", "non", "non", "oui", "non", "non"],
                           ["non", "oui", "non", "oui", "non", "oui", "non", "non", "oui",
                            "non", "oui", "non", "non", "non", "non", "non", "oui", "non"],
                           ["non", "oui", "non", "oui", "non", "oui", "non", "non", "oui",
                            "non", "oui", "non", "non", "non", "non", "non", "non", "oui"],
                           # aprésBMW
                           ["non", "oui", "non", "oui", "non", "oui", "non", "oui", "non",
                               "oui", "non", "non", "oui", "non", "oui", "non", "non", "non"],
                           ["non", "oui", "non", "oui", "non", "oui", "non", "oui", "non",
                               "oui", "non", "non", "oui", "non", "non", "oui", "non", "non"],
                           ["non", "oui", "non", "oui", "non", "oui", "non", "oui", "non",
                               "oui", "non", "non", "oui", "non", "non", "non", "oui", "non"],
                           ["non", "oui", "non", "oui", "non", "oui", "non", "oui", "non",
                               "oui", "non", "non", "oui", "non", "non", "non", "non", "oui"],
                           # wallysCar
                            ["non","oui","non","oui","non","oui","non","non","oui","non","oui","non","non","oui",
                             "oui","non","non","non"],
                            ["non","oui","non","oui","non","oui","non","non","oui","non","oui","non","non","oui",
                             "non","oui","non","non"],
                            ["non","oui","non","oui","non","oui","non","non","oui","non","oui","non","non","oui",
                             "non","non","oui","non"],
                            ["non","oui","non","oui","non","oui","non","non","oui","non","oui","non","non","oui",
                             "non","non","non","oui"],
                            #kIA
                            ["non","oui","non","non","oui","oui","non","oui","non","non","oui","non","non","non",
                             "oui","non","non","non"],
                            ["non","oui","non","non","oui","oui","non","oui","non","non","oui","non","non","non",
                             "non","oui","non","non"],
                            ["non","oui","non","non","oui","oui","non","oui","non","non","oui","non","non","non",
                             "non","non","oui","non"],
                            ["non","oui","non","non","oui","oui","non","oui","non","non","oui","non","non","non",
                             "non","non","non","oui"],
                            #mazda
                            ["non","oui","non","non","oui","oui","non","oui","non","non","oui","oui","non","non",
                             "oui","non","non","non"],
                             ["non","oui","non","non","oui","oui","non","oui","non","non","oui","oui","non","non",
                             "non","oui","non","non"],
                            ["non","oui","non","non","oui","oui","non","oui","non","non","oui","oui","non","non",
                             "non","non","oui","non"],
                            ["non","oui","non","non","oui","oui","non","oui","non","non","oui","oui","non","non",
                             "non","non","non","oui"],
                            #peugeot
                            ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","non",
                             "oui","non","non","non"],
                            ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","non",
                             "non","oui","non","non"],
                            ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","non",
                             "non","non","oui","non"],
                            ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","non",
                             "non","non","non","oui"],
                            #volsvagen
                             ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","oui",
                            "oui","non","non","non"],
                            ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","oui",
                            "non","oui","non","non"],
                            ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","oui",
                            "non","non","oui","non"],
                            ["non","non","oui","oui","non","oui","non","oui","non","non","oui","non","non","oui",
                            "non","non","non","oui"],
                            #renault 
                            ["non","non","oui","non","oui","oui","non","oui","non","non","oui","non","oui","non",
                             "oui","non","non","non"],
                            ["non","non","oui","non","oui","oui","non","oui","non","non","oui","non","oui","non",
                             "non","oui","non","non"],
                            ["non","non","oui","non","oui","oui","non","oui","non","non","oui","non","oui","non",
                             "non","non","oui","non"],
                            ["non","non","oui","non","oui","oui","non","oui","non","non","oui","non","oui","non",
                             "non","non","non","oui"],
                            #fiat
                            ["non","non","oui","non","oui","oui","non","non","oui","non","oui","non","non","non",
                             "oui","non","non","non"],
                            ["non","non","oui","non","oui","oui","non","non","oui","non","oui","non","non","non",
                             "non","oui","non","non"],
                            ["non","non","oui","non","oui","oui","non","non","oui","non","oui","non","non","non",
                             "non","non","non","oui"],
                            #citroen
                            ["non","non","oui","non","oui","oui","non","oui","non","oui","non","non","non","non",
                             "oui","non","non","non"],
                            ["non","non","oui","non","oui","oui","non","oui","non","oui","non","non","non","non",
                             "non","oui","non","non"],
                            ["non","non","oui","non","oui","oui","non","oui","non","oui","non","non","non","non",
                             "non","non","oui","non"],]
        listScore = []
        listCars = ["lamborghini_Rouge", "lamborghini_Bleu",
                    "lamborghini_Noir", "lamborghini_Blanc",
                    "ferrari_Rouge", "ferrari_Bleu",
                    "ferrari_Noir", "ferrari_Blanc",
                    "porche_Rouge", "porche_Bleu",
                    "porche_Noir", "porche_Blanc",
                    "mercedes_Rouge", "mercedes_Bleu",
                    "mercedes_Noir", "mercedes_Blanc",
                    "range_rover_Rouge", "range_rover_Bleu",
                    "range_rover_Noir", "range_rover_Blanc",
                    "BMW_Rouge", "BMW_Bleu",
                    "BMW_Noir", "BMW_Blanc",
                    "audi_Rouge", "audi_Bleu",
                    "audi_Noir", "audi_Blanc",
                    "wallyscar_Rouge", "wallyscar_Bleu",
                    "wallyscar_Noir", "wallyscar_Blanc",
                    "KIA_Rouge", "KIA_Bleu",
                    "KIA_Noir", "KIA_Blanc",
                    "mazda_Rouge", "mazda_Bleu",
                    "mazda_Noir", "mazda_Blanc",
                    "peugeot_Rouge", "peugeot_Bleu",
                    "peugeot_Noir", "peugeot_Blanc",
                    "volkswagen_Rouge", "volkswagen_Bleu",
                    "volkswagen_Noir", "volkswagen_Blanc",
                    "renault_Rouge", "renault_Bleu",
                    "renault_Noir", "renault_Blanc",
                    "fiat_Rouge", "fiat_Bleu",
                    "fiat_Noir", "fiat_Blanc",
                    "citroen_Rouge", "citroen_Bleu",
                    "citroen_Noir", "citroen_Blanc"
                    ]
        max_count = 0
        max_car = ""
        for i in range(0, len(listCarsDetails)):
            score = 0
            for j in range (0,len(listofcar)):
                if (listCarsDetails[i] == listofcar[j]):
                     score = score + 1
            listScore.append(score)        
            
        max_car = listScore.index(max(listScore),0,len(listScore))
        
 
        if_not_matching(listCars[max_car])



    #la fonction principale 
if __name__ == "__main__":
    engine = findYourCar()
    engine.reset()
    
    root.mainloop()
    
    
    
