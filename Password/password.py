import re
import hashlib
import json
from tkinter import * 
from tkinter.messagebox import *

def newpassword():
    password=entree.get()
    
    list=lire()
    one_special=re.search('[!@#$%\^&\*]',password)==None
    one_upper= re.search('[A-Z]',password)==None
    one_lower= re.search('[a-z]',password)==None
    one_number=re.search('\d',password)==None
    password_exist=encrypt(password) in list.values()
    user_exist=user.get() in list.keys()
    if user_exist:
        showinfo("ERREUR !", "Utilisateur invalide !") 
    elif len(password)<8 or password_exist or one_upper or one_lower or one_special or one_number:
        showinfo("ERREUR !", "Mot de passe invalide !")
    else:
        showinfo("VALIDE !", "Mot de passe enregistré !")
        save(user.get(),encrypt(password))
    return password
            
def encrypt(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def save(user, crypte):
    ecrire=open("data.json", "r+")
    donnes=json.load(ecrire)
    donnes[user] = crypte
    ecrire.seek(0)
    ecrire.write(json.dumps(donnes))
    ecrire.close()

def lire():
    with open("data.json", "r+") as affiche:
        test=json.load(affiche)
    return test

def affiche():
    test=lire()
    affichage=""
    for i,j in test.items():
        affichage+= i+": "+j+"\n\n"
    showinfo("Affichage des mots de passe",affichage)

from tkinter import * 

fenetre = Tk()
fenetre.title("Password")
fenetre.geometry("700x350")
fenetre.configure(bg='grey')
bouton2=Button(fenetre, text="Afficher les mots de passe", command=affiche).pack( padx=5, pady=5)
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack( padx=30, pady=30)
Label(Frame1, text="Utilisateur :").pack(side = TOP,padx=5, pady=5)
user = Entry(Frame1, width=30)
user.pack(side = TOP,padx=5, pady=5)
test=Label(Frame1, text="mot de passe :")
entree = Entry(Frame1, width=30)
bouton1=Button(Frame1, text="Créer le compte.", command=newpassword)
test.pack(padx=5, pady=5)
entree.pack(padx=5, pady=5)
bouton1.pack(side = BOTTOM, padx=5, pady=5)
bouton3=Button(fenetre, text="Quitter", bg="red" , command=fenetre.quit).pack(side=BOTTOM,padx=5, pady=5)
fenetre.mainloop()
