import pymysql
import os

# Database
try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='pass1',
                                 database='Cafe_DB',
                                 charset='utf8mb4')
except pymysql.err.OperationalError:
    print("Connection to database failed. Please load again.")


def disconnect_db():
    connection.close()


def fetch_row(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchone()
    cursor.close()
    return results

def fetch_table(table_name):
    cursor = connection.cursor()
    sql = f"SELECT * FROM {table_name}"
    cursor.execute(sql)
    table_rows = cursor.fetchall()
    cursor.close()
    return table_rows


# Menus
def main_menu():
    print("\nYou're at Main Menu")
    print("[0] Exit app \n[1] Product Menu \n[2] Courier Menu\n[3] Order Menu")


def product_menu():
    print("\nYour're at Product Menu")
    print("[1] Show product list \n[2] Add New product \n[3] Update product \n[4] Delete Product \n[0] Back To Main Menu")


def courier_menu():
    print("\nYour're at Courier Menu")
    print("[1] Show courier list \n[2] Add New courier \n[3] Update Courier \n[4] Delete Courier \n[0] Back To Main Menu")


def order_menu():
    print("\nYou're at Order Menu")
    print("[1] View order \n[2] Create Order\n[3] Update Order Status \n[4] Update Order Details\n[5] Delete Order\n[0] Back to Main Menu")


# Products
def show_product_list():
    # cursor = connection.cursor()
    # sql = "SELECT * FROM products"
    # cursor.execute(sql)
    # products = cursor.fetchall()
    products = 'products'
    products_rows = fetch_table(products)


    print("\n------------------PRODUCTS------------------")
    print(f"{'ID' :<2} | {'Item':^16} |  {'Price':^9}|  {'QTN':^9}")
    for product in products_rows:
        product_id, item, price, quantity = product
        print("{:<2} {:^20} {:^12} {:^9}".format(product_id, item, price, quantity))



def add_product():
    print("Add new product")
    try:
        new_product = input("Name of new product: ").title().strip()
        new_product_price = input("Price of new product ").strip()
        if len(new_product) > 0 and len(new_product_price) > 0:
            if isinstance(new_product_price, int) is False or isinstance(new_product_price, float) is False:
                return print("Product price must be numbers. Please start again.")
            else:
                cursor = connection.cursor()
                sql = "INSERT INTO products (item, price) VALUES(%s, %s)"
                add_product_data = (new_product, new_product_price)
                cursor.execute(sql, add_product_data)
                connection.commit()
                print(f"\n{new_product} £{new_product_price} successfully added.")
                cursor.close()
        else:
            print("\n**ALERT**\nName and Price must not be empty. Please add product again.")
    except ValueError:
        print("\n**ALERT**\nPrice must be a number. Please add product again.")


def update_product():
    print("\n---Update product---")
    show_product_list()

    try:
        product_id = int(input("Select no. of product: ").strip())
        if product_id:
            sql = f"SELECT item, price FROM products WHERE product_id = {product_id}."
            chosen_product_name, chosen_product_price = fetch_row(sql)
            new_product_name = input("Update product name (Blank to remain unchanged): ").title().strip()
            new_product_price = input("Update price (Blank to remain unchanged): ").title().strip()

            if len(new_product_name) == 0:
                new_product_name = chosen_product_name

            if len(new_product_price) == 0:
                new_product_price = chosen_product_price
            elif isinstance(new_product_price, int) is False or isinstance(new_product_price, float) is False:
                return print("Product price must be numbers. Please start again.")

            cursor = connection.cursor()
            sql = "UPDATE products SET item =%s, price=%s WHERE product_id = %s"
            update_product_data = (new_product_name, new_product_price, product_id)
            cursor.execute(sql, update_product_data)
            connection.commit()
            print(f"Updated: {new_product_name} £{new_product_price}.")
            cursor.close()

        else:
            print("Product no. must not be empty. Please start again.")
    except ValueError:
        print('Product no. and price should be numbers. \nPlease start again.')
    except TypeError:
        print('Product doesn\'t exist. Please select again.')


def delete_product():
    print("\nDelete product")
    show_product_list()
    try:
        product_id = input("Select product no.: ")
        if len(product_id) > 0:
            sql = f"SELECT item, price FROM products WHERE product_id = {product_id}"
            chosen_product_name, chosen_price = fetch_row(sql)

            print(f"***ALERT***\nYou're going to delete {chosen_product_name} £{chosen_price}.")
            delete_option = input("[Y] or [N]?").title()
            if delete_option == 'Y':
                cursor = connection.cursor()
                sql = "DELETE FROM products WHERE product_id = %s"
                cursor.execute(sql, product_id)
                connection.commit()
                print(f"{chosen_product_name} £{chosen_price} deleted.")
                cursor.close()
            elif delete_option == 'N':
                print(f"[{chosen_product_name}] {chosen_price} remains unchanged.")
            else:
                print("Invalid input. Product not deleted.")
    except TypeError:
        print('Product doesn\'t exist. Please select again.')


# Courier
def show_courier_list():
    print("\n---Orders---")
    cursor = connection.cursor()
    sql = "SELECT * FROM couriers"
    cursor.execute(sql)
    couriers = cursor.fetchall()

    print("\n-------------------Couriers-------------------")
    print(f"{'ID' :<2} | {'Courier':^20} |  {'Phone':^16}")
    for courier in couriers:
        courier_id, courier_name, courier_phone = courier
        print("{:<2} {:^24} {:^16}".format(courier_id, courier_name,courier_phone))
    cursor.close()


def add_courier():
    print("\nAdd courier")
    try:
        new_courier = input("Name: ").title().strip()
        new_courier_phone = input("Phone no.:").strip()
        if len(new_courier) > 0 and len(new_courier_phone) > 0:
            new_courier_phone = int(new_courier_phone)
            cursor = connection.cursor()
            sql = f"INSERT INTO couriers (courier_name, courier_phone) VALUES(%s, %s)"
            add_courier_data = (new_courier, new_courier_phone)
            cursor.execute(sql, add_courier_data)
            connection.commit()
            print(f"\n{new_courier}| Phone no. {new_courier_phone} successfully added.")
            cursor.close()
        else:
            print("\n**ALERT**\nName and phone must not be empty. Please add courier again.")
    except ValueError:
        print("\n**ALERT**\nPhone no. should be numbers. Please add courier again.")


def update_courier():
    print("\n---Update courier---")
    show_courier_list()

    try:
        courier_id = input("Select courier no.:").strip()
        if len(courier_id) > 0:
            courier_id = int(courier_id)
            sql = f"SELECT courier_id, courier_name, courier_phone FROM couriers WHERE courier_id = {courier_id}."
            chosen_courier_id, chosen_courier_name, chosen_courier_phone = fetch_row(sql)

            new_courier_name = input("Update courier name (Blank to remain unchanged): ").title().strip()
            new_courier_phone = input("Update phone (Blank to remain unchanged): ").title().strip()

            if len(new_courier_name) == 0:
                new_courier_name = chosen_courier_name

            if len(new_courier_phone) == 0:
                new_courier_phone = chosen_courier_phone
            elif isinstance(int(new_courier_phone), int) is False:
                return print("\nPhone no. must be numbers. Please update again.")

            cursor = connection.cursor()
            sql = "UPDATE couriers SET courier_name =%s, courier_phone=%s WHERE courier_id =%s"
            update_courier_data = (new_courier_name, new_courier_phone, chosen_courier_id)
            cursor.execute(sql, update_courier_data)
            connection.commit()
            print(f"\nUpdated: {new_courier_name} | {new_courier_phone}.")
            cursor.close()

        else:
            print("Product no. must not be empty. Please start again.")
    except ValueError:
        print('Phone no. should be numbers. \nPlease start again.')
    except TypeError:
        print('Courier doesn\'t exist. Please select again.')


def delete_courier():
    print("\nDelete courier")
    show_courier_list()
    try:
        courier_id = input("Select courier no.: ")
        if len(courier_id) > 0:
            sql = f"SELECT courier_id, courier_name, courier_phone FROM couriers WHERE courier_id = {courier_id}"
            courier_id, chosen_courier_name, chosen_courier_phone = fetch_row(sql)

            print(f"***ALERT***\nYou're going to delete[{courier_id}] {chosen_courier_name}| Phone: {chosen_courier_phone}.")
            delete_option = input("[Y] or [N]?").title()
            if delete_option == 'Y':
                cursor = connection.cursor()
                sql = "DELETE FROM couriers WHERE courier_id = %s"
                cursor.execute(sql, courier_id)
                connection.commit()
                print(f"[{courier_id}] {chosen_courier_name}|Phone: {chosen_courier_phone} deleted.")
                cursor.close()
            elif delete_option == 'N':
                print(f"[{courier_id}] {chosen_courier_name}|Phone: {chosen_courier_phone} remains unchanged.")
            else:
                print("Invalid input. Courier not deleted.")
    except TypeError:
        print('Courier doesn\'t exist. Please select again.')
    except ValueError:
        print("Invalid courier number. Please choose again.")


# Customer
def create_order():
    print("Create Order")
    try:
        user_name = input("Name: ").title().strip()
        if len(user_name) > 0:
            user_address = input("Address: ")
            user_phone = input("Phone no.:")
        else:
            print("Name must not be empty. Please start again.")

        show_product_list()
        order_item = input("\nPlease enter no. of items to order e.g. 1,2,3: ")

        if len(order_item) > 0:
            show_courier_list()
            courier_option = int(input("\nPlease select courier no.: "))
        else:
            print("Items must be selected for a new order. Please create order again.")

        order_status = 1

        cursor = connection.cursor()
        sql = """INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items) 
        VALUES (%s, %s, %s, %s, %s, %s)"""
        create_order_data = (user_name, user_address, user_phone,courier_option, order_status, order_item)
        cursor.execute(sql, create_order_data)
        connection.commit()
        print(f"\nOrders added: \n Name: {user_name} | Phone: {user_phone} | Address: {user_address}")
        print(f"\nOrders Details:\n Courier ID:{courier_option} \n Items: {order_item}")
        cursor.close()

    except ValueError:
        print("\n**ALERT**\nPhone no. should be numbers. Please create order again.")
    except TypeError:
        print('Courier or products doesn\'t exist. Please select again.')


def show_order_status_list():
    cursor = connection.cursor()
    sql = "SELECT * FROM order_status"
    cursor.execute(sql)
    order_status = cursor.fetchall()

    print("\n---Order Status---")
    print(f"{'ID' :<4} | {'Status':<15} |")
    for row in order_status:
        status_id, status = row
        print("{:<6} {:<15} ".format(status_id, status))
    cursor.close()


def view_orders():
    cursor = connection.cursor()
    sql = "SELECT * FROM orders"
    cursor.execute(sql)
    orders = cursor.fetchall()

    print("\n-----------Orders-----------")
    print(f"{'ID' :<2} | {'Customer':^15}| {'Phone':^12} | {'Address':^16}| {'Courier':^4} | {'Status':^6} | {'Items':^12}| ")
    for order in orders:
        order_id, customer_name, customer_phone, customer_address, courier, status, items = order
        print("{:<2} {:^17} {:^16} {:^16} {:^6} {:^10} {:^14}".format(order_id, customer_name, customer_phone, customer_address, courier, status, items))
    cursor.close()


def update_order_status():
    print("Update Order Status")
    view_orders()
    order_id = int(input("Please enter order number: "))
    sql = f"SELECT order_id, customer_name, customer_phone, customer_address, courier, status, items FROM orders WHERE order_id = {order_id}."
    order_id, customer_name, customer_phone, customer_address, courier, status, items = fetch_row(sql)
    print(f"Selected Order: {order_id} {customer_name} | Order Status: {status}")

    show_order_status_list()
    new_order_status = int(input("\nPlease select new status ID:"))

    cursor = connection.cursor()
    sql = f"UPDATE orders SET status = {new_order_status} WHERE order_id={order_id}"
    cursor.execute(sql)
    connection.commit()
    print(f"Order status is updated from {status} to {new_order_status} ")
    cursor.close()


def update_order():
    print("Update Order")
    view_orders()
    try:
        order_id = int(input("Please select order no.: ").strip())

        if order_id:
            sql = f"SELECT order_id, customer_name, customer_phone, customer_address, courier, status, items FROM orders WHERE order_id = {order_id}."
            order_id, customer_name, customer_phone, customer_address, courier, status, items = fetch_row(sql)
            new_customer_name = input("Update name (Blank to remain unchanged): ").title().strip()
            new_customer_address = input("Update address (Blank to remain unchanged): ").title().strip()
            new_customer_phone = input("Update phone no. (Blank to remain unchanged): ").strip()

            if len(new_customer_name) == 0:
                new_customer_name = customer_name

            if len(new_customer_address) == 0:
                new_customer_address = customer_phone

            if len(new_customer_phone) == 0:
                new_customer_address = customer_address

            show_product_list()
            new_order_item = input("\nUpdate product IDs e.g. 1,2,3 (Blank to remain unchanged): ")

            if len(new_order_item) == 0:
                new_order_item = items

            show_courier_list()
            courier_option = int(input("\nPlease select courier no.: "))


            cursor = connection.cursor()
            sql = "UPDATE products SET item =%s, price=%s WHERE product_id = %s"
            update_product_data = (new_product_name, new_product_price, product_id)
            cursor.execute(sql, update_product_data)
            connection.commit()
            print(f"Updated: {new_product_name} £{new_product_price}.")
            cursor.close()

        else:
            print("Order ID must not be empty. Please start again.")
    except ValueError:
        print('Order ID should be a number. \nPlease start again.')
    except TypeError:
        print('Product doesn\'t exist. Please select again.')


def delete_order():
    print("\nDelete Order")
    view_orders()
    try:
        order_id = int(input("Select courier no.: ").strip())
        if order_id:
            sql = f"SELECT order_id, customer_name, customer_phone, customer_address, courier, status, items FROM orders WHERE order_id = {order_id}."
            order_id, customer_name, customer_phone, customer_address, courier, status, items = fetch_row(sql)

            print(f"***ALERT***\nYou're going to delete Order[{order_id}]|Name:{customer_name}| Item:{items}.")
            delete_option = input("[Y] or [N]?").title()
            if delete_option == 'Y':
                cursor = connection.cursor()
                sql = f"DELETE FROM orders WHERE order_id = {order_id}"
                cursor.execute(sql)
                connection.commit()
                print(f"Order[{order_id}]|Name:{customer_name}| Item:{items} deleted.")
                cursor.close()
            elif delete_option == 'N':
                print(f"Order[{order_id}]|Name:{customer_name}| Item:{items} remains unchanged.")
            else:
                print("Invalid input. Order not deleted.")
    except TypeError:
        print('Order doesn\'t exist. Please select again.')
    except ValueError:
        print("Order id must be numbers. Please start again.")