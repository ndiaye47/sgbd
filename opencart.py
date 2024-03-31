#Faisons le premier test avec Tkinter

from tkinter import *
import tkinter as tk
import mysql.connector

# Fonction pour récupérer et afficher le nombre d'utilisateurs
def get_user_count():
    cursor.execute("SELECT COUNT(*) FROM oc_user")
    user_count = cursor.fetchone()[0]
    result_label.config(text="Nombre d'utilisateurs: {}".format(user_count))

# Fonction pour récupérer et afficher le nombre d'utilisateurs connectés
def get_online_user_count():
    cursor.execute("SELECT COUNT(*) FROM oc_customer_online")
    online_user_count = cursor.fetchone()[0]
    result_label.config(text="Nombre d'utilisateurs connectés: {}".format(online_user_count))

# Fonction pour récupérer et afficher le nombre de produits commandés
def get_ordered_product_count():
    cursor.execute("SELECT SUM(quantity) FROM oc_order_product")
    ordered_product_count = cursor.fetchone()[0]
    result_label.config(text="Nombre de produits commandés: {}".format(ordered_product_count))

# Connexion à la base de données OpenCart

connection = mysql.connector.connect(
   host="localhost",
     user="root",
     password="",
     database="opencartbd"
 )
cursor = connection.cursor()


# Création de la fenêtre Tkinter
root = tk.Tk()
root.title("Monitoring OpenCart")


# Création des onglets
root.title("Monitoring OpenCart")


menuPrincipale = Menu(root)

menuPrincipale.add_cascade(label="admin")
menuPrincipale.add_cascade(label="Client")
menuPrincipale.add_cascade(label="Produit")

root.config(menu=menuPrincipale)
# Création des boutons pour afficher différentes options
user_button = tk.Button(root, text="Nombre d'utilisateurs", command=get_user_count)
user_button.pack(pady=5)

online_user_button = tk.Button(root, text="Nombre d'utilisateurs connectés", command=get_online_user_count)
online_user_button.pack(pady=5)

ordered_product_button = tk.Button(root, text="Nombre de produits commandés", command=get_ordered_product_count)
ordered_product_button.pack(pady=5)

# Étiquette pour afficher le résultat
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Exécution de la boucle principale Tkinter
root.mainloop()



print("bonjour absa")