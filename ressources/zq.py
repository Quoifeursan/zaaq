import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import filedialog

def ouvrir_fichier():
       # Ouvrir la boîte de dialogue de sélection de fichier
    filepath = filedialog.askopenfilename(filetypes=[('Backup ZQ', '*.zq')])

    # Vérifier si un fichier a été sélectionné
    if filepath:
        # Charger le contenu du fichier dans une variable
        with open(filepath, 'r') as file:
            contenu = file.read()
            print(contenu)

            idx_hvenme = contenu.find("HVENME&") + len("HVENME&")
            idx_frmpwd = contenu.find("&FRMPWD")
            idx_ifneedcontact = contenu.find("&IFNEEDCONTACT")
            ide = contenu[idx_hvenme:idx_frmpwd]
            pw = contenu[idx_frmpwd+len("&FRMPWD&"):idx_ifneedcontact]
            mail = contenu[idx_ifneedcontact+len("&IFNEEDCONTACT&"):]


            # Connexion à la base de données
            connexion = sqlite3.connect("ressources/database.db")
            cursor = connexion.cursor()

            # Création de la table "saves" si elle n'existe pas déjà
            cursor.execute("CREATE TABLE IF NOT EXISTS saves (ide TEXT, pw TEXT, mail TEXT)")

            # Insertion des valeurs dans la table
            cursor.execute("INSERT INTO saves (ide, pw, mail) VALUES (?, ?, ?)", (ide, pw, mail))

            # Validation de la transaction
            connexion.commit()

            # Fermeture de la connexion
            connexion.close()

