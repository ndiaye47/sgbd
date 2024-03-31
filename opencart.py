#Faisons le premier test avec Tkinter

from tkinter import *
import tkinter as tk
import mysql.connector

# Fonction pour récupérer et afficher la liste des clients
def get_customer_list():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("SELECT firstname,lastname FROM oc_customer")
    customers = cursor.fetchall()
    customer_list = '\n'.join([customer[0] for customer in customers])
    result_label.config(text="Liste des clients:\n{}".format(customer_list))

# Fonction pour récupérer et afficher le nombre total de clients
def get_total_customers():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("SELECT COUNT(*) FROM oc_customer")
    total_customers = cursor.fetchone()[0]
    result_label.config(text="Nombre total de clients: {}".format(total_customers))
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