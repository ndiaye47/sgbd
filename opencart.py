#Faisons le premier test avec Tkinter

import tkinter as tk
from tkinter import ttk
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


# Création de l'onglet principal
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Admin')
tab_control.add(tab2, text='Client')
tab_control.add(tab3, text='Produit')

tab_control.pack(expand=1, fill='both')
