# Database
products = open("../database/product_list.txt", "r")
product_list = [product.strip() for product in products.readlines()]

couriers = open("../database/courier_list.txt", "r")
courier_list = [courier.strip() for courier in couriers.readlines()]


# Menus
def main_menu():
    print("\nYou're at Main Menu")
    print("[0] Exit app \n[1] Product Menu \n[2] Courier Menu")


def product_menu():
    print("\nYour're at Product Menu")
    print("[1] Show product list \n[2] Add New product \n[3] Update product \n[4] Delete Product \n[0] Back To Main Menu")


def courier_menu():
    print("\nYour're at Courier Menu")
    print("[1] Show courier list \n[2] Add New courier \n[3] Update courier \n[4] Delete courier \n[0] Back To Main Menu")


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

        while True:
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
                with open("../database/product_list.txt", "w") as products:
                    for product in product_list:
                        products.write(product+"\n")
                print("\nNew product added.")
                print(product_list)
                break

            elif menu_option == 3:
                print("\nUpdate product")
                print(list(enumerate(product_list)))
                product_index = int(input("\nEnter product no. you want to update: "))
                try:
                    chosen_product = product_list[product_index]
                    new_product = input("Enter new product name: ")
                    product_list[product_index] = new_product
                    with open("../database/product_list.txt", "w") as products:
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
                    product_list.pop(product_index)
                    print(f"'{chosen_product}' successfully deleted.")
                    print(product_list)
                    with open("../database/product_list.txt", "w") as products:
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
                with open("../database/courier_list.txt", "a") as couriers:
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
                    with open("../database/courier_list.txt", "w") as couriers:
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
                    print(f"Courier '{chosen_courier}' deleted.")
                    courier_list.pop(courier_index)
                    print(courier_list)

                    with open("../database/courier_list.txt", "w") as couriers:
                        for courier in courier_list:
                            couriers.write(courier + "\n")
                    break
                except IndexError:
                    print("Courier doesn't exist. Please choose again.")
                    continue
                except ValueError:
                    print("Invalid courier number. Please choose again.")
                    continue

