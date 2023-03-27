from tkinter import *
from tkinter import messagebox
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="0000",
  database="boutique"
)

root = Tk()
root.title("Gestion de stock")

listbox = Listbox(root, width=50)
listbox.pack()

def afficher_produits():
  listbox.delete(0, END)
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM produit")
  produits = mycursor.fetchall()
  for produit in produits:
    listbox.insert(END, produit)

nom_produit = Entry(root, width=30)
nom_produit.pack()
description_produit = Entry(root, width=30)
description_produit.pack()
prix_produit = Entry(root, width=30)
prix_produit.pack()
quantite_produit = Entry(root, width=30)
quantite_produit.pack()
id_categorie_produit = Entry(root, width=30)
id_categorie_produit.pack()

def ajouter_produit():
  nom = nom_produit.get()
  description = description_produit.get()
  prix = prix_produit.get()
  quantite = quantite_produit.get()
  id_categorie = id_categorie_produit.get()

  if nom == "" or description == "" or prix == "" or quantite == "" or id_categorie == "":
    messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
    return

  mycursor = mydb.cursor()
  mycursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)", (nom, description, prix, quantite, id_categorie))
  mydb.commit()
  afficher_produits()

ajouter_bouton = Button(root, text="Ajouter un produit", command=ajouter_produit)
ajouter_bouton.pack()

def supprimer_produit():
  selection = listbox.curselection()
  if len(selection) == 0:
    messagebox.showerror("Erreur", "Veuillez sélectionner un produit")
    return
  produit = listbox.get(selection[0])
  id_produit = produit[0]
  mycursor = mydb.cursor()
  mycursor.execute("DELETE FROM produit WHERE id_produit=%s", (id_produit,))
  mydb.commit()
  afficher_produits()

supprimer_bouton = Button(root, text="Supprimer le produit sélectionné", command=supprimer_produit)
supprimer_bouton.pack()

afficher_produits()

root.mainloop()

mydb.close()
