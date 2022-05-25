import pymysql

def clear_screen():
    print("\n" * 3)


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


def fetch_table(table_name, sort_filter):
    cursor = connection.cursor()
    sql = f"SELECT * FROM {table_name} ORDER BY {sort_filter}"
    cursor.execute(sql)
    table_rows = cursor.fetchall()
    cursor.close()
    return table_rows


def insert_or_update(sql):

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()


# Menus
def main_menu():
    print("\n------You're at Main Menu------")
    print("[0] Exit app \n[1] Product Menu \n[2] Courier Menu\n[3] Order Menu")


def product_menu():
    clear_screen()
    print("\n------Your're at Product Menu------")
    print("[1] Show product list \n[2] Add New product \n[3] Update product \n[4] Delete Product \n[0] Back To Main Menu")


def courier_menu():
    clear_screen()
    print("\n------Your're at Courier Menu------")
    print("[1] Show courier list \n[2] Add New courier \n[3] Update Courier \n[4] Delete Courier \n[0] Back To Main Menu")


def order_menu():
    clear_screen()
    print("\n------You're at Order Menu------")
    print("[1] View order \n[2] Create Order\n[3] Update Order Status \n[4] Update Order Details\n[5] Delete Order\n[0] Back to Main Menu")


# Products
def show_product_list():
    clear_screen()

    products_rows = fetch_table('products', 'product_id')

    print("\n------------------PRODUCTS------------------")
    print(f"{'ID' :<2} | {'Item':^16} |  {'Price':^9}|  {'QTN':^9}")

    for product in products_rows:
        product_id, item, price, quantity = product
        print("{:<2} {:^20} {:^12} {:^9}".format(product_id, item, price, quantity))


def add_product():
    clear_screen()
    print("---Add new product--")
    try:
        new_product = input("Name of new product: ").title().strip()
        new_product_price = input("Price of new product: ").strip()
        new_product_qtn = 0
        if len(new_product) > 0 and len(new_product_price) > 0:
            float(new_product_price)

            sql = f"""INSERT INTO products (item, price, quantity) 
            VALUES('{new_product}', '{new_product_price}', '{new_product_qtn}')"""

            insert_or_update(sql)
            print(f"\n{new_product} £{new_product_price} successfully added.")

        else:
            print("\n**ALERT**\nName and Price must not be empty. Please add product again.")
    except ValueError:
        print("\n**ALERT**\nPrice must be a number. Please add product again.")
    except pymysql.err.DataError:
        print("\n**ALERT**\nPrice must be a number. Please add product again.")


def update_product():
    clear_screen()
    print("\n------Update product------")
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

            sql = f"""UPDATE products 
            SET item ='{new_product_name}', price='{new_product_price}' 
            WHERE product_id = '{product_id}'"""
            insert_or_update(sql)

            print(f"\nUpdated: {new_product_name} £{new_product_price}.")

        else:
            print("\n**ALERT**\nProduct no. must not be empty. Please update product again.")
    except ValueError:
        print('P\n**ALERT**\nProduct no. should be numbers. \nPlease update product again.')
    except TypeError:
        print('\n**ALERT**\nProduct doesn\'t exist. Please update product again.')
    except pymysql.err.DataError:
        print("\n**ALERT**\nPrice must be a number. Please update product again.")


def delete_product():
    clear_screen()
    print("\n------Delete product------")
    show_product_list()
    try:
        product_id = input("Select product no.: ")
        if len(product_id) > 0:
            sql = f"SELECT item, price FROM products WHERE product_id = {product_id}"
            chosen_product_name, chosen_price = fetch_row(sql)

            print(f"***ALERT***\nYou're going to delete {chosen_product_name} £{chosen_price}.")
            delete_option = input("[Y] or [N]?").title()
            if delete_option == 'Y':

                sql = f"DELETE FROM products WHERE product_id = {product_id}"
                insert_or_update(sql)

                print(f"{chosen_product_name} £{chosen_price} deleted.")

            elif delete_option == 'N':
                print(f"{chosen_product_name} £{chosen_price} remains unchanged.")
            else:
                print("\n**ALERT**\nInvalid input. Product not deleted.")
    except TypeError:
        print('\n**ALERT**\nProduct doesn\'t exist. Please select again.')


# Courier
def show_courier_list():
    couriers_rows = fetch_table('couriers', 'courier_id')
    clear_screen()

    print("\n-------------------Couriers-------------------")
    print(f"{'ID' :<2} | {'Courier':^20} |  {'Phone':^16}")
    for courier in couriers_rows:
        courier_id, courier_name, courier_phone = courier
        print("{:<2} {:^24} {:^16}".format(courier_id, courier_name,courier_phone))


def add_courier():
    clear_screen()
    print("\n---Add courier---")
    try:
        new_courier = input("Name: ").title().strip()
        new_courier_phone = input("Phone no.:").strip()
        if len(new_courier) > 0 and len(new_courier_phone) > 0:
            int(new_courier_phone)

            sql = f"""INSERT INTO couriers (courier_name, courier_phone) 
            VALUES('{new_courier}','{new_courier_phone}')"""
            insert_or_update(sql)

            print(f"\n{new_courier}| Phone no. {new_courier_phone} successfully added.")

        else:
            print("\n**ALERT**\nName and phone must not be empty. Please add courier again.")
    except ValueError:
        print("\n**ALERT**\nPhone no. should be numbers. Please add courier again.")
    except pymysql.err.DataError:
        print("\n**ALERT**\nPhone no. must be a number. Please add product again.")


def update_courier():
    clear_screen()
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


            sql = f"""UPDATE couriers 
            SET courier_name ='{new_courier_name}', courier_phone='{new_courier_phone}' 
            WHERE courier_id ={chosen_courier_id}"""
            insert_or_update(sql)

            print(f"\nUpdated: {new_courier_name} | {new_courier_phone}.")

        else:
            print("\n**ALERT**\nProduct no. must not be empty. Please start again.")
    except ValueError:
        print('\n**ALERT**\nPhone no. should be numbers. \nPlease start again.')
    except TypeError:
        print('\n**ALERT**\nCourier doesn\'t exist. Please select again.')


def delete_courier():
    clear_screen()
    print("\n---Delete courier---")
    show_courier_list()
    try:
        courier_id = input("Select courier no.: ")
        if len(courier_id) > 0:
            sql = f"SELECT courier_id, courier_name, courier_phone FROM couriers WHERE courier_id = {courier_id}"
            courier_id, chosen_courier_name, chosen_courier_phone = fetch_row(sql)

            print(f"***ALERT***\nYou're going to delete[{courier_id}] {chosen_courier_name}| Phone: {chosen_courier_phone}.")
            delete_option = input("[Y] or [N]?").title()
            if delete_option == 'Y':
                sql = f"DELETE FROM couriers WHERE courier_id = {courier_id}"
                insert_or_update(sql)

                print(f"[{courier_id}] {chosen_courier_name}|Phone: {chosen_courier_phone} deleted.")

            elif delete_option == 'N':
                print(f"[{courier_id}] {chosen_courier_name}|Phone: {chosen_courier_phone} remains unchanged.")
            else:
                print("\n**ALERT**\nInvalid input. Courier not deleted.")
    except TypeError:
        print('\n**ALERT**\nCourier doesn\'t exist. Please select again.')
    except ValueError:
        print("\n**ALERT**\nInvalid courier number. Please choose again.")


# Order
def check_product_existence(order_item):
    cursor = connection.cursor()
    sql = f"SELECT product_id FROM products"
    cursor.execute(sql)
    table_rows = cursor.fetchall()
    cursor.close()
    product_stock = table_rows

    product_in_stock = []

    for product_id in product_stock:
        a, = product_id
        product_in_stock.append(a)

    selected_order_item = set([int(i) for i in order_item.split(',')])

    item_available_check = selected_order_item.issubset(product_in_stock)
    return item_available_check


def create_order():
    clear_screen()
    print("---Create Order---")
    try:
        user_name = input("Name: ").title().strip()
        if len(user_name) > 0:
            user_address = input("Address: ").strip()
            user_phone = input("Phone no.:")
            if len(user_address) > 0:
                int(user_phone)
            else:
                print("\n**ALERT**\nAddress must not be empty. Please create order again.")

            show_product_list()
            order_item = input("\nPlease enter item IDs to order e.g. 1,2,3: ")

            if len(order_item) > 0:
                order_valid = check_product_existence(order_item)
            else:
                print("Items must be selected for a new order. Please create order again.")

            if order_valid:
                show_courier_list()
                courier_option = int(input("\nPlease select courier no.: "))
                order_status = 1

                sql = f"""INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status, items) 
                                    VALUES (
                                    '{user_name}', 
                                    '{user_address}', 
                                    '{user_phone}',
                                    '{courier_option}',
                                    '{order_status}',
                                    '{order_item}')"""
                insert_or_update(sql)

                print(f"\nOrders added: \n -Name: {user_name} | Phone: {user_phone} | Address: {user_address}")
                print(f"\nOrders Details:\n -Courier ID:{courier_option} \n -Items: {order_item}")
            else:
                print(f"One or more selected items in [{order_item}] does not exist. \nPlease create order again.")





        else:
            print("\n**ALERT**\nName must not be empty. Please create order again.")

    except ValueError:
        print("\n**ALERT**\nPhone no. should be numbers. Please create order again.")
    except TypeError:
        print('\n**ALERT**\nInvalid input / Empty field not allowed. Please select again.')


def show_order_status_list():
    order_status_rows = fetch_table('order_status', 'status_id')
    clear_screen()

    print("\n---Order Status---")
    print(f"{'ID' :<4} | {'Status':<15} |")
    for row in order_status_rows:
        status_id, status = row
        print("{:<6} {:<15} ".format(status_id, status))


def view_orders():
    try:
        view_order_filter = input("Sort by [1]Order IDs [2] Status [3] Courier?: ").strip()
        if len(view_order_filter) > 0:
            view_order_filter = int(view_order_filter)

        if view_order_filter == 1:
            orders_rows = fetch_table('orders', 'order_id')
        elif view_order_filter == 2:
            orders_rows = fetch_table('orders', 'status')
        elif view_order_filter == 3:
            orders_rows = fetch_table('orders', 'courier')
        else:
            orders_rows = fetch_table('orders', 'order_id')

        clear_screen()
        print("\n--------------------------------ORDERS--------------------------------")
        print(f"""{'ID' :<2} | {'Customer':^15}| {'Phone':^12} | {'Address':^16}| {'Courier':^4} | {'Status':^6} | {'Items':^12}|""")
        for order in orders_rows:
            order_id, customer_name, customer_phone, customer_address, courier, status, items = order
            print("{:<2} {:^17} {:^14} {:^16} {:^8} {:^10} {:^12}".format(order_id, customer_name, customer_phone, customer_address, courier, status, items))
    except ValueError:
        print('\n**ALERT**\nInvalid menu option. Please select again.')


def update_order_status():
    clear_screen()
    print("-----Update Order Status-----")
    view_orders()
    try:
        order_id = int(input("Please enter order number: ").strip())
        if order_id:
            sql = f"""SELECT order_id, customer_name, customer_phone, customer_address, 
            courier, status, items FROM orders WHERE order_id = {order_id}."""
            order_id, customer_name, customer_phone, customer_address, courier, status, items = fetch_row(sql)
            print(f"Selected Order: {order_id} {customer_name} | Order Status: {status}")

            show_order_status_list()
            new_order_status = input("\nPlease select new status ID (Blank to remain unchanged): ").strip()

            if len(new_order_status) == 0:
                new_order_status = status
            else:
                new_order_status = int(new_order_status)

            sql = f"UPDATE orders SET status = {new_order_status} WHERE order_id={order_id}"
            insert_or_update(sql)

            print(f"Order status is updated from {status} to {new_order_status} ")
        else:
            print("\n**ALERT**\nOrder id not found. Please start again.")
    except ValueError:
        print('\n**ALERT**\nOrder ID should be a number. \nPlease start again.')
    except TypeError:
        print('\n**ALERT**\nOrder doesn\'t exist. Please select again.')


def update_order():
    clear_screen()
    print("-----Update Order-----")
    view_orders()


    try:
        order_id = int(input("Please select order no.: ").strip())

        if order_id:
            sql = f"""SELECT order_id, customer_name, customer_phone, customer_address, courier, status, items 
            FROM orders 
            WHERE order_id = {order_id}."""
            order_id, customer_name, customer_phone, customer_address, courier, status, items = fetch_row(sql)

            new_customer_name = input("Update name (Blank to remain unchanged): ").title().strip()
            new_customer_phone = input("Update phone no. (Blank to remain unchanged): ").strip()
            new_customer_address = input("Update address (Blank to remain unchanged): ").title().strip()

            if len(new_customer_name) == 0:
                new_customer_name = customer_name

            if len(new_customer_phone) == 0:
                new_customer_phone = customer_phone

            int(new_customer_phone)

            if len(new_customer_address) == 0:
                new_customer_address = customer_address

            show_product_list()
            order_item = input("\nUpdate product IDs e.g. 1,2,3 (Blank to remain unchanged): ")

            if len(order_item) == 0:
                order_item = items
                order_valid = check_product_existence(order_item)
            else:
                order_valid = check_product_existence(order_item)

            if order_valid:
                show_courier_list()
                new_courier = input("\nPlease select courier no. Blank to remain unchanged): ").strip()
                if len(new_courier) == 0:
                    new_courier = courier
                else:
                    new_courier = int(new_courier)

                sql = f"""UPDATE orders 
                        SET
                        customer_name='{new_customer_name}',
                        customer_phone='{new_customer_phone}', 
                        customer_address='{new_customer_address}', 
                        courier='{new_courier}', 
                        status='{status}', 
                        items='{order_item}'
                        WHERE order_id ='{order_id}'"""

                insert_or_update(sql)

                print(f"\nOrder [{order_id}] updated.")
            else:
                print(f"One or more selected items in [{order_item}] does not exist. \nPlease update order again.")

        else:
            print("\n**ALERT**\nOrder ID must not be empty. Please start again.")
    except ValueError:
        print('\n**ALERT**\nOrder ID /Phone no. should be number. \nPlease start again.')
    except TypeError:
        print('\n**ALERT**\nOrder doesn\'t exist. Please select again.')


def delete_order():
    clear_screen()
    print("\n----Delete Order----")
    view_orders()
    try:
        order_id = int(input("Select order ID.: ").strip())
        if order_id:
            sql = f"""SELECT order_id, customer_name, customer_phone, customer_address, courier, status, items 
            FROM orders WHERE order_id = {order_id}."""
            order_id, customer_name, customer_phone, customer_address, courier, status, items = fetch_row(sql)

            print(f"***ALERT***\nYou're going to delete Order[{order_id}] Name:{customer_name} | Item:{items}.")
            delete_option = input("[Y] or [N]?").title()
            if delete_option == 'Y':
                sql = f"DELETE FROM orders WHERE order_id = {order_id}"
                insert_or_update(sql)
                print(f"\nOrder[{order_id}] Name:{customer_name} | Item:{items} deleted.")

            elif delete_option == 'N':
                print(f"\nOrder[{order_id}] Name:{customer_name} | Item:{items} remains unchanged.")

            else:
                print("\n**ALERT**\nInvalid input. Order not deleted.")

    except TypeError:
        print('\n**ALERT**\nOrder doesn\'t exist. Please select again.')
    except ValueError:
        print("\n**ALERT**\nOrder id must be numbers. Please start again.")