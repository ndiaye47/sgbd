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

# Fonction pour récupérer et afficher la liste des souhaits
def get_wishlist_product_ids():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("SELECT product_id FROM oc_customer_wishlist")
    wishlist_products = cursor.fetchall()
    wishlist_product_ids = '\n'.join([str(product[0]) for product in wishlist_products])
    result_label.config(text="ID des produits dans la liste des souhaits:\n{}".format(wishlist_product_ids))    
# Fonction pour récupérer les tendances de ventes mensuelle
def get_sales_trends():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("SELECT DATE_FORMAT(date_added, '%Y-%m') AS month, SUM(total) AS total_sales FROM oc_order GROUP BY month ORDER BY month")
    sales_trends = cursor.fetchall()
    sales_trends_text = ""
    for trend in sales_trends:
        sales_trends_text += "Mois: {}, Ventes: {}\n".format(trend[0], trend[1])
    result_label.config(text="Tendances de vente par mois:\n{}".format(sales_trends_text))

#Fonction clients plus de commandes
def get_top_customers():
    clear_result_label()  # Effacer le texte précédent
    cursor.execute("SELECT customer_id, COUNT(*) AS total_orders FROM oc_order GROUP BY customer_id ORDER BY total_orders DESC")
    top_customers = cursor.fetchall()
    top_customers_text = ""
    for customer in top_customers:
        top_customers_text += "ID client: {}, Nombre de commandes: {}\n".format(customer[0], customer[1])
    result_label.config(text="Clients avec le plus de commandes:\n{}".format(top_customers_text))
    

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

sales_trends_button = tk.Button(tab1, text="Tendances de vente par mois", command=get_sales_trends)
sales_trends_button.pack(pady=5)


#bouton WishList
wishlist_product_ids_button = tk.Button(tab1, text="ID des produits dans la liste des souhaits", command=get_wishlist_product_ids)
wishlist_product_ids_button.pack(pady=5)

#Le total
total_products_button = tk.Button(tab3, text="Nombre total de produits", command=get_total_products)
total_products_button.pack(pady=5)

# Étiquette pour afficher le résultat
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Exécution de la boucle principale Tkinters
root.mainloop()