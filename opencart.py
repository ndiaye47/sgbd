#Faisons le premier test avec Tkinter

from tkinter import *
import tkinter as tk
from tkinter import ttk
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

# Fonction pour récupérer et afficher la liste des produits
def get_product_list():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("select model from oc_product")
    products = cursor.fetchall()
    product_list = '\n'.join([product[0] for product in products])
    result_label.config(text="Liste des produits:\n{}".format(product_list))

# Fonction pour récupérer et afficher le nombre total de produits
def get_total_products():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("SELECT COUNT(*) FROM oc_product")
    total_products = cursor.fetchone()[0]
    result_label.config(text="Nombre total de produits: {}".format(total_products))

# Fonction pour récupérer et afficher la liste des utilisateurs connectés sur la base de donnee
def get_online_users_list():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("SELECT customer_id FROM oc_customer_online")
    online_users = cursor.fetchall()
    # Convertir les valeurs int en str
    online_users_list = '\n'.join([str(user[0]) for user in online_users])
    result_label.config(text="Id utilisateurs connectes:\n{}".format(online_users_list))

# Fonction pour effacer le texte de l'étiquette result_label
def clear_result_label():
    result_label.config(text="")
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

# Création de l'onglet principal

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Admin')
tab_control.add(tab2, text='Client')
tab_control.add(tab3, text='Produit')

tab_control.pack(expand=1, fill='both')

# Création des boutons pour chaque onglet
customer_list_button = tk.Button(tab2, text="Liste des clients", command=get_customer_list)
customer_list_button.pack(pady=5)

total_customers_button = tk.Button(tab2, text="Nombre total de clients", command=get_total_customers)
total_customers_button.pack(pady=5)

online_users_button = tk.Button(tab1, text="Liste des utilisateurs connectés", command=get_online_users_list)
online_users_button.pack(pady=5)

product_list_button = tk.Button(tab3, text="Liste des produits", command=get_product_list)
product_list_button.pack(pady=5)

#Le total
total_products_button = tk.Button(tab3, text="Nombre total de produits", command=get_total_products)
total_products_button.pack(pady=5)