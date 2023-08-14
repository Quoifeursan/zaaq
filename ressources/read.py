import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def afficher_contenu_table():
  # Connexion à la base de données
    connexion = sqlite3.connect("ressources/database.db")
    cursor = connexion.cursor()

    # Sélection de tout le contenu de la table "saves"
    cursor.execute("SELECT * FROM saves")
    rows = cursor.fetchall()

    # Fermeture de la connexion
    connexion.close()

    # Vérification si la liste rows est vide
    if not rows:
        print("La table est vide.")
        return

    # Création d'une fenêtre Toplevel pour afficher le contenu
    fenetre_affichage = tk.Toplevel()
    fenetre_affichage.title("Contenu de la table saves")

    # Création d'un Treeview pour afficher les données tabulaires
    treeview = ttk.Treeview(fenetre_affichage)

    # Définition des colonnes
    treeview["columns"] = tuple(range(len(rows[0])))

    # Configuration des en-têtes de colonnes
    for i, col_name in enumerate(cursor.description):
        treeview.heading(i, text=col_name[0])

    # Ajout des lignes de données
    for row in rows:
        treeview.insert("", tk.END, values=row)

    # Affichage du Treeview
    treeview.pack()