# Database
products = open("../database/product_list.txt", "r+")
product_list = [product.strip() for product in products.readlines()]
couriers = open("../database/courier_list.txt", "r+")
courier_list = [courier.strip() for courier in couriers.readlines()]

#Menus
main_menu = "[0] Exit app \n[1] Product Menu \n[2] Courier Menu"
product_menu = "1 Show product list \n2 Add New product \n3 Update product \n4 Delete Product \n0 Back To Main Menu"
courier_menu = "1 Show courier list \n2 Add New courier \n3 Update courier \n4 Delete Product \n0 Back To Main Menu"

#App Start
print("Welcome to the cafe app.")
while True:
    print("\n--Main Menu--")
    print(main_menu)
    user_option = int(input("\nEnter your option: "))

    if user_option == 0:
        print("\nApp exiting...")
        quit()

    elif user_option == 1:
        print(product_menu)
        menu_option = int(input("\nChoose what you want to do from above: "))
        # Back to main menu
        if menu_option == 0:
            print("\nReturning to main menu")

        # Product Menu
        elif menu_option == 1:
            print(product_list)

        elif menu_option == 2:
            print("Add new product")
            new_product = input("\nName of new product: ")
            products.write("\n"+new_product)
            print("\nNew product added.")

        elif menu_option == 3:
            print("\nUpdate product")
            print(list(enumerate(product_list)))
            product_index = int(input("\nEnter product no. you want to update: "))
            product_list[product_index] = input("Enter new product name: ")
            products = open("../database/product_list.txt", "w")
            products.write("\n".join(product_list))
            print("\nProduct name updated.")
            products.close()

        elif menu_option == 4:
            print("\nDelete prodcut")
            print(list(enumerate(product_list)))
            product_index = int(input("\nEnter the no. of product to delete: "))
            print(f"{product_list[product_index]} deleted.")
            product_list.pop(product_index)
            print(product_list)
            products = open("../database/product_list.txt", "w")
            products.write("\n".join(product_list))

    #Courier Menu
    elif user_option == 2:
        print(courier_menu)
        menu_option = int(input("\nChoose from above: "))

        if menu_option == 0:
            print("\nReturning to main menu")
            break

        elif menu_option == 1:
            print(courier_list)

        elif menu_option == 2:
            print("\nAdd courier")
            new_courier = input("Name of new courier: ")
            products.write("\n" + new_courier)
            print(f"\nNew courier {new_courier} created.")

        elif menu_option == 3:
            print("Update courier")
            print(list(enumerate(courier_list)))
            courier_index = int(input("Enter courier no.: "))
            courier_list[courier_index] = input("New courier name: ")
            couriers = open("../database/courier_list.txt", "w")
            couriers.write("\n".join(courier_list))
            print("Courier name updated.")

        elif menu_option == 4:
            print("Delete courier")





#test adding new line