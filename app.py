# Database
products = open("database/product_list.txt", "r")
product_list = [product.strip() for product in products.readlines()]

couriers = open("database/courier_list.txt", "r")
courier_list = [courier.strip() for courier in couriers.readlines()]

order_list = [{'customer_name': 'heidi', 'customer_address': 'rfhf', 'customer_phone': '6673', 'courier': '3', 'status': 'preparing'}]
order_status_list =["Preparing","Out for delivery", "Delivered"]

# Customer
class user:
    def __init__(self,name=str, address=str, phone=int, courier=str) -> None:
        self.name = user_name
        self.address = user_address
        self.phone = user_phone
        self.courier = courier_option
    
    def add_order(self):
         order_list.append({"customer_name": user_name,
         "customer_address": user_address,
         "customer_phone": user_phone,
         "courier" : courier_option,
         "status" : "preparing"})
         return order_list

# Menus
def main_menu():
    print("\nYou're at Main Menu")
    print("[0] Exit app \n[1] Product Menu \n[2] Courier Menu\n[3] Order Menu")

def product_menu():
    print("\nYour're at Product Menu")
    print("[1] Show product list \n[2] Add New product \n[3] Update product \n[4] Delete Product \n[0] Back To Main Menu")

def courier_menu():
    print("\nYour're at Courier Menu")
    print("[1] Show courier list \n[2] Add New courier \n[3] Update courier \n[4] Delete courier \n[0] Back To Main Menu")

def order_menu():
    print("You're at Order Menu")
    print("[1] View order \n[2] Add Order\n[3] Update Order Status \n[4] Update Order Details\n[0] Back to Main Menu")

def order_items():
    print("You can update the following:")
    print("[1] Name \n[2] Address\n[3]Phone \n[4] Courier \n[5] Status")


# App Start
print("Welcome to the cafe app.")
while True:
    try:
        main_menu()
        user_option = int(input("\nEnter your option: "))
    except ValueError:
        print("Invalid option. Please choose from menu.")
        continue

    # Back to main menu
    if user_option == 0:
        print("\nApp exiting...")
        quit()

    elif user_option == 1:
        product_menu()
        menu_option = int(input("\nChoose what you want to do from above: "))

        
        if menu_option == 0:
            print("\nReturning to main menu")
            break

        # Product Menu
        elif menu_option == 1:
            print(product_list)
            break

        elif menu_option == 2:
            print("Add new product")
            new_product = input("Name of new product: ")
            product_list.append(new_product)
            with open("database/product_list.txt", "w") as products:
                for product in product_list:
                    products.write(product+"\n")
            print("\nNew product added.")
            print(product_list)
            break

        elif menu_option == 3:
            while True:
                print("\nUpdate product")
                print(list(enumerate(product_list)))
                product_index = int(input("\nEnter product no. you want to update: "))
                try:
                    chosen_product = product_list[product_index]
                    new_product = input("Enter new product name: ")
                    product_list[product_index] = new_product
                    with open("database/product_list.txt", "w") as products:
                        for product in product_list:
                            products.write(product + "\n")
                        print(f"\n'{chosen_product}' is updated to '{new_product}'.")
                        break
                except IndexError:
                    print("Product doesn't exist. Please choose again.")
                    continue
                except ValueError:
                    print("Invalid product number. Please choose again.")
                    continue

        elif menu_option == 4:
            print("\nDelete product")
            print(list(enumerate(product_list)))
            product_index = int(input("\nEnter the no. of product to delete: "))
            try:
                chosen_product = product_list[product_index]
                del product_list[product_index]
                print(f"'{chosen_product}' successfully deleted.")
                print(product_list)
                with open("database/product_list.txt", "w") as products:
                    for product in product_list:
                        products.write(product + '\n')
                break
            except IndexError:
                print("Invalid product number. Please choose again.")
                continue



# Courier Menu
    elif user_option == 2:
        courier_menu()
        menu_option = int(input("\nChoose from above: "))

        while True:
            if menu_option == 0:
                print("\nReturning to main menu")
                break

            elif menu_option == 1:
                print(courier_list)
                break

            elif menu_option == 2:
                print("\nAdd courier")
                new_courier = input("Name of new courier: ")
                courier_list.append(new_courier)
                with open("database/courier_list.txt", "a") as couriers:
                    for courier in courier_list:
                        couriers.write(new_courier+"\n" )
                print(f"\nNew courier {new_courier} created.")
                break

            elif menu_option == 3:
                print("Update courier")
                print(list(enumerate(courier_list)))
                try:
                    courier_index = int(input("Enter courier no.: "))
                    chosen_courier = courier_list[courier_index]
                    new_courier= input("New courier name: ")
                    with open("database/courier_list.txt", "w") as couriers:
                        for courier in courier_list:
                            couriers.write(courier + "\n")
                    print(f"Courier {chosen_courier} is updated to {new_courier}.")
                    break
                except IndexError:
                    print("Courier doesn't exist. Please choose again.")
                    continue
                except ValueError:
                    print("Invalid courier number. Please choose again.")
                    continue

            elif menu_option == 4:
                print("Delete courier")
                print(list(enumerate(courier_list)))
                try:
                    courier_index = int(input("\nEnter courier no. to delete: "))
                    chosen_courier = courier_list[courier_index]
                    del courier_list[courier_index]
                    print(f"Courier '{chosen_courier}' deleted.")
                    print("Courier list:")
                    print(courier_list)

                    with open("database/courier_list.txt", "w") as couriers:
                        for courier in courier_list:
                            couriers.write(courier + "\n")
                    break
                except IndexError:
                    print("Courier doesn't exist. Please choose again.")
                    continue
                except ValueError:
                    print("Invalid courier number. Please choose again.")
                    continue

    elif user_option == 3:
        order_menu()
        menu_option = int(input("\nChoose from above: "))
        if menu_option == 1: #print orders dictionary
                print(order_list)

        elif menu_option == 2: #add new order
            print("To place order, please provide your details.")
            user_name = input("Name: ")
            user_address = input("Address: ")
            user_phone = input("Phone no.:")
            print("\n---Available Couriers---")
            print(list(enumerate(courier_list)))
            courier_option = input("Please select courier number: ")

            new_order = user(user_name, user_address, user_phone, user_option)
            new_order.add_order()

        elif menu_option == 3: # update order status
            print("Update Order Status")
            print(list(enumerate(order_list)))
            order_number = int(input("Please enter order number: "))
            old_order_status = order_list[order_number]['status']
            print("\n---Order Status List---")
            print(list(enumerate(order_status_list)))
            new_order_status = int(input("\nPlease select new order status:"))
            order_list[order_number]['status'] = order_status_list[new_order_status]
            print(f"Your order staus is updated from {old_order_status} to {order_status_list[new_order_status]} ")
            
        elif menu_option == 4: # update order
            print("Update Order")
            print(list(enumerate(order_list)))
            order_number = int(input("Please select order number: "))
            order_items()
            update_order_options = int(input("Choose an item to update: "))
            if update_order_options == 1:
                update_name = input("Please enter a new name: ")
                order_list[order_number]['customer_name'] = update_name
                print(f"The name is updated to {update_name}")

            elif update_order_options == 2:
                update_address = input("Enter new address: ")
                order_list[order_number]['customer_address'] = update_address
                print(f"The address is updated to {update_address}")

            elif update_order_options == 3:
                update_phone = input("Enter new phone number: ")
                order_list[order_number]['customer_phone'] = update_phone
                print(f"The phone number is updated to {update_phone}")

            elif update_order_options == 4:
                existing_courier = order_list[order_number]['courier']
                print(f"The current courier is no.{existing_courier}.")
                print(list(enumerate(courier_list)))
                update_courier = int(input("Please choose a new courier: "))
                new_courier = courier_list[update_courier]
                order_list[order_number]['courier'] = new_courier
                print(f"Courier is updated to {new_courier}.")

        elif menu_option == 5: # delete order
            print(list(enumerate(order_list)))
            print("\n ***ALERT: You are about to delete order***")
            order_number = int(input("Please select  order to DELETE: "))
            del order_list[order_number]