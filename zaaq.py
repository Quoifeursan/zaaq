import sqlite3
from tkinter import *
from ressources.zq import ouvrir_fichier
from ressources.read import afficher_contenu_table

# Connexion à la base de données
conn = sqlite3.connect("ressources/database.db")

def verifier_identifiants(identifiant, mot_de_passe):
    # Vérifier les identifiants dans la base de données
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs WHERE ide = ? AND mdp = ?", (identifiant, mot_de_passe))
    row = cursor.fetchone()
    cursor.close()
    
    return row is not None

def connexion():
    connexion_window = Toplevel(fenetre)
    connexion_window.grid_rowconfigure(0, weight=1)
    connexion_window.grid_rowconfigure(1, weight=1)
    connexion_window.grid_rowconfigure(2, weight=1)
    connexion_window.grid_rowconfigure(3, weight=1)
    connexion_window.grid_columnconfigure(0, weight=1)
    connexion_window.grid_columnconfigure(1, weight=1)
    connexion_window.grid_columnconfigure(2, weight=1)
    connexion_window.grid_columnconfigure(3, weight=1)
    connexion_window.grid_columnconfigure(4, weight=1)
    connexion_window.configure(bg='#00122c')
    connexion_window.title("Connexion")
    connexion_window.geometry("400x300")
    connexion_window.iconbitmap("ressources/img/icon.ico")
    connexion_window.wm_iconbitmap("ressources/img/icon.ico")

    def valider():
        identifiant = id_entry.get()
        mot_de_passe = mdp_entry.get()

        # Vérifier les identifiants dans la base de données
        if verifier_identifiants(identifiant, mot_de_passe):
            # Fermer la fenêtre de saisie des données
            connexion_window.destroy()
            # Réactiver la fenêtre principale
            fenetre.deiconify()
        else:
            # Afficher un message d'erreur
            error_label.config(text="Identifiant ou mot de passe incorrect.", fg="red")


    labelTitre = Label(connexion_window, text="Connexion", bg='#00122c', fg='white', font=('calibri', 13))
    labelTitre.grid(row=0, column=2)

    id_entry = Entry(connexion_window, width=14)
    id_entry.grid(row=1, column=3)
    labid = Label(connexion_window, text="Identifiant", bg='#00122c', fg='white')
    labid.grid(row=1, column=1)

    mdp_entry = Entry(connexion_window, width=14)
    mdp_entry.grid(row=2, column=3)
    labelmdp = Label(connexion_window, text="Mot de passe", bg='#00122c', fg='white')
    labelmdp.grid(row=2, column=1)

    butValider = Button(connexion_window, text="Valider", width=18, height=2, relief=FLAT, bg="#00205a", fg="white", font=('calibri', 8), activebackground="white", command=valider)
    butValider.grid(row=3, column=2)

    error_label = Label(connexion_window, text="", bg='#00122c', fg='red')
    error_label.grid(row=4, column=0, columnspan=5)

    # Désactiver la fenêtre principale
    fenetre.withdraw()

    # Attacher le grab à la fenêtre Toplevel
    connexion_window.grab_set()

    def fermer_connexion():
        # Fermer la fenêtre Toplevel
        connexion_window.destroy()
        # Fermer l'application
        fenetre.quit()

    # Définir la fonction de fermeture de la fenêtre Toplevel
    connexion_window.protocol("WM_DELETE_WINDOW", fermer_connexion)


# Créer une fenêtre Tkinter
fenetre = Tk()
fenetre.geometry('700x300')
fenetre.configure(bg='#00122c')
fenetre.grid()
fenetre.title("ZAAQ")
fenetre.iconbitmap("ressources/img/icon.ico")
fenetre.wm_iconbitmap("ressources/img/icon.ico")

fenetre.grid_rowconfigure(0, weight=1)
fenetre.grid_rowconfigure(1, weight=1)
fenetre.grid_rowconfigure(2, weight=1)
fenetre.grid_rowconfigure(3, weight=1)
fenetre.grid_rowconfigure(4, weight=1)
fenetre.grid_columnconfigure(0, weight=1)
fenetre.grid_columnconfigure(1, weight=1)
fenetre.grid_columnconfigure(2, weight=1)
fenetre.grid_columnconfigure(3, weight=1)
fenetre.grid_columnconfigure(4, weight=1)

imageO = PhotoImage(file="ressources/img/logomain.png")
imageO_width = imageO.width()
imageO_height = imageO.height()
canvas = Canvas(fenetre, width=imageO_width, height=imageO_height, bd=0, highlightthickness=0)
canvas.grid(row=0, column=1, columnspan=3)
canvas.create_image(0, 0, anchor="nw", image=imageO)

butAdd = Button(fenetre, text="Ouvrir backup", width=18, height=2, relief=FLAT, bg="#00205a", fg="white", font=('calibri', 8), activebackground="white", command=ouvrir_fichier)
butAdd.grid(row=2, column=1)

butAdd = Button(fenetre, text="Résultat Backup", width=18, height=2, relief=FLAT, bg="#00205a", fg="white", font=('calibri', 8), activebackground="white", command=afficher_contenu_table)
butAdd.grid(row=2, column=3)

# Lancer la boucle principale Tkinter
connexion()
fenetre.mainloop()
