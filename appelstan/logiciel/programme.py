from tkinter import *
from time import gmtime, strftime, sleep, time
import pymysql

#DEF DE LA FEN PRINCIPALE
base = Tk()
base.title('Appel Internat')
base.geometry("1280x1020")
base.config(bg = 'LightSteelBlue2')
base.resizable(width=TRUE, height=TRUE)

#MYSQL CONNEXION

db = pymysql.connect("localhost","root","","ETUDE" )
cursor = db.cursor()


#DEF DATE

heure = strftime('%H')
heure = int(heure)
jour =strftime('%d')
jour = int(jour)
mois =strftime('%m')
mois = int(mois)

if mois == 1:
    Mois = ' janvier'
elif mois == 2:
    Mois =' février'
elif mois == 3:
    Mois =' mars'
elif mois == 4:
    Mois =' avril'
elif mois == 5:
    Mois =' mai'
elif mois == 6:
    Mois =' juin'
elif mois == 7:
    Mois =' juillet'
elif mois == 8:
    Mois =' aout'
elif mois == 9:
    Mois =' septembre'
elif mois == 10:
    Mois =' novembre'
elif mois == 11:
    Mois =' décembre'
elif mois == 12:
    Mois =' janvier'

#DEF ETUDE 

if heure < 19:
    appel = str('1ere etude du ' + jour + Mois)
elif heure > 19:
    appel = str('2eme étude du ' + jour + Mois)

appel1 = "1ere étude du " + str(jour-1) + Mois
appel2 = "2eme étude du " + str(jour-1) + Mois
appel3 = "1ere étude du " + str(jour-2) + Mois
appel4 = "2eme étude du " + str(jour-2) + Mois
appel5 = "1ere étude du " + str(jour-3) + Mois
appel6 = "2eme étude du " + str(jour-3) + Mois

#DEF FONCTION

'''heure'''
def heure1():
    
    heure = Tk()
    heure.resizable(width=False, height=False) 
    heure.geometry("145x50+875+50")
    heure.overrideredirect(1) 
    heure.config(bg="white") 
    Label_Heure = Label((heure), font=('calibri', 30,))
    Label_Heure.pack()
    
    def Heure():
        Label_Heure.config(text=strftime('%H:%M:%S'))
        Label_Heure.after(200, Heure)
    Heure()
    heure.mainloop()

secondes=time()
gmt=gmtime(secondes)
fmt="%d/%m/%Y"
date = 'Etude du ' + strftime(fmt,gmt)

'''maj'''
def mise_à_jour():
    heure1()
    heure = strftime('%H')
    heure = int(heure)
    jour =strftime('%d')
    jour = int(jour)
    mois =strftime('%m')
    mois = int(mois)

    if mois == 1:
        Mois = ' janvier'
    elif mois == 2:
        Mois =' février'
    elif mois == 3:
        Mois =' mars'
    elif mois == 4:
        Mois =' avril'
    elif mois == 5:
        Mois =' mai'
    elif mois == 6:
        Mois =' juin'
    elif mois == 7:
        Mois =' juillet'
    elif mois == 8:
        Mois =' aout'
    elif mois == 9:
        Mois =' septembre'
    elif mois == 10:
        Mois =' novembre'
    elif mois == 11:
        Mois =' décembre'
    elif mois == 12:
        Mois =' janvier'
    if heure < 19:
        appel = str('1ere etude du ' + jour + Mois)
    elif heure > 19:
        appel = str('2eme étude du ' + jour + Mois)
    NomFichier = appel + ".txt"
    mon_fichier = open(NomFichier, "w")
    mon_fichier.write('RETARD:')
    for n in range(1,200):
        sql = "SELECT Prenom,  Nom FROM ETUDE WHERE place=" + n + " AND 'etat' == 'abs'"
        cursor.execute(sql)
        results = cursor.fetchall()
        L1 = 0
        for row in results:
            Prenom = row[0]
            Nom = row[1]
            ABS = str(Nom + ' ' + Prenom)
            mon_fichier = open(NomFichier, "a")
            mon_fichier.write(ABS +'\n')
            L1 =L1 + 1
            mon_fichier.close()
    mon_fichier = open(NomFichier, "a")
    mon_fichier.write('\n' + '\n' + 'RETARD:' + '\n')
    mon_fichier.close()
    for n in range(1,200):
        sql = "SELECT Prenom,  Nom FROM ETUDE WHERE place=" + n + " AND 'etat' == 'ret'"
        cursor.execute(sql)
        results = cursor.fetchall()
        L2 = 0
        for row in results:
            Prenom = row[0]
            Nom = row[1]
            RET = str(Nom + ' ' + Prenom)
            mon_fichier = open(NomFichier, "a")
            mon_fichier.write(RET +'\n')
            L2 = L2 + 1
            mon_fichier.close()

    mon_fichier = open(NomFichier, "r")
    for n in range(1,L1):
        ligne = mon_fichier.readline(n)
        Absent1.insert(ligne)
    for n in range(L1+1,L2):
        ligne = mon_fichier.readline(n)
        Retard1.insert(ligne)
    mon_fichier.close()        

'''afficher étude précedente'''
def EtudePrecedente(jour, Mois):
    appel = str('1ere etude du ' + jour + Mois)
    NomFichier = appel + ".txt"
    fd = open(NomFichier, "r")
    x = 0
    while fd.readline():
        x += 1
    mon_fichier = open(NomFichier, "r")
    for n in range(1,k):
        ligne = mon_fichier.readline(n)
        if ligne == 'RETARD:':
            break
        else:
            ligne = mon_fichier.readline(n)
            Absent2.insert(ligne)
        for k in range(n,x):
            ligne = mon_fichier.readline(k)
            Retard2.insert(ligne)
    mon_fichier.close()
 
'''ouvre les anciennes études'''
def AncienneEtude(date):
    base2 = Tk()
    base2.title(date)
    base2.geometry("640x1020")
    base2.resizable(width=TRUE, height=TRUE)
    nom = date + ".txt"
    mon_fichier = open(nom, "r")
    contenu = str(mon_fichier.read())
    mon_fichier.close
    Label300 = Label(base2, text = contenu, bd=0, bg="white", height="8", width="60",font=("Calibri", 15))
    Label300.place(x=25, y=15,width=590, height=990 )
    mon_fichier.close
    base2.mainloop


def Aff_etude_1():
    AncienneEtude(appel1)

def Aff_etude_2():
    AncienneEtude(appel2)
    
def Aff_etude_3():
    AncienneEtude(appel3)

def Aff_etude_4():
    AncienneEtude(appel4)

def Aff_etude_5():
    AncienneEtude(appel5)

def Aff_etude_6():
    AncienneEtude(appel6)

#DEF DES FENTRES
Label3 = Label(base, text = "Etude en cours:",bd=0, bg="white", height="8", width="60", font=("Calibri", 15))
Label4 = Label(base, text = 'Etude précedente:',bd=0, bg="white", height="8", width="60", font=("Calibri", 15))
Label2= Label(base, text = date , bd=0, bg='white', font=("Calibri", 30))

Absent1 = Text(base, bd=0, bg="white", height="8", width="50", font="Calibri",)
Absent1.insert(END, "ABSENT:\n")
Absent1.config(state=DISABLED)

Retard1 = Text(base, bd=0, bg="white", height="8", width="50", font="Calibri",)
Retard1.insert(END, "RETARD:\n")
Retard1.config(state=DISABLED)

Absent2 = Text(base, bd=0, bg="white", height="8", width="50", font="Calibri",)
Absent2.insert(END, "ABSENT:\n")
Absent2.config(state=DISABLED)

Retard2 = Text(base, bd=0, bg="white", height="8", width="50", font="Calibri",)
Retard2.insert(END, "RETARD:\n")
Retard2.config(state=DISABLED)

photo = PhotoImage(file="stan.png")


#PLACEMENT

Label2.place(x=350, y=5,width=500, height=50 )

Label3.place(x=25, y=67,width=390, height=40 )
Label4.place(x=455, y=67,width=390, height=40 )

Absent1.place(x=20,y=110, height=400, width=400)
Retard1.place(x=20,y=530, height=400, width=400)

Absent2.place(x=450,y=110, height=400, width=400)
Retard2.place(x=450,y=530, height=400, width=400) 

canvas = Canvas(base,width=198, height=190)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.place(x=1050,y=17)

bouton = Button(base,font=30, text="Mise à jour", width="20", height=5,bd=0, bg="white", activebackground="LightSteelBlue2",command=mise_à_jour)
bouton.place(x=855,y=110)

bouton1 = Button(base,font=30, text= appel1, width="40", height=5,bd=0, bg="white", activebackground="LightSteelBlue2",command=Aff_etude_1)
bouton1.place(x=855,y=280)

bouton2 = Button(base,font=30, text= appel2, width="40", height=5,bd=0, bg="white", activebackground="LightSteelBlue2",command=Aff_etude_2)
bouton2.place(x=855,y=390)

bouton3 = Button(base,font=30, text= appel3, width="40", height=5,bd=0, bg="white", activebackground="LightSteelBlue2",command=Aff_etude_3)
bouton3.place(x=855,y=500)

bouton4 = Button(base,font=30, text= appel4, width="40", height=5,bd=0, bg="white", activebackground="LightSteelBlue2",command=Aff_etude_4)
bouton4.place(x=855,y=610)

bouton5 = Button(base,font=30, text= appel5, width="40", height=5,bd=0, bg="white", activebackground="LightSteelBlue2",command=Aff_etude_5)
bouton5.place(x=855,y=720)

bouton6 = Button(base,font=30, text= appel6, width="40", height=5,bd=0, bg="white", activebackground="LightSteelBlue2",command=Aff_etude_6)
bouton6.place(x=855,y=830)

EtudePrecedente(jour, Mois)

#FIN

base.mainloop()
db.close()

#BROUILLON
'''



'''
