import utility as ut

# App Start
print("Welcome to the cafe app.")
while True:
    try:
        ut.main_menu()
        user_option = int(input("\nEnter your option: "))

        # Back to main menu
        if user_option == 0:
            print("\n>>> >>> Exiting...")
            ut.clear_screen()
            print("App Closed")
            ut.disconnect_db()
            quit()

        # Product Menu
        elif user_option == 1:
            while True:
                ut.product_menu()
                menu_option = int(input("\nPlease select from menu: "))

                if menu_option == 0:
                    print("\n>>> >>> Returning to main menu")
                    ut.clear_screen()
                    break

                # Product Menu
                elif menu_option == 1:
                    ut.show_product_list()

                elif menu_option == 2:
                    ut.add_product()

                elif menu_option == 3:
                    ut.update_product()

                elif menu_option == 4:
                    while True:
                        ut.delete_product()
                        break
                else:
                    print("Invalid option. Please choose from menu.")
                    continue

        # Courier Menu
        elif user_option == 2:
            while True:
                ut.courier_menu()
                menu_option = int(input("\nPlease select from menu: "))

                if menu_option == 0:
                    print("\n>>> >>> Returning to main menu")
                    break

                elif menu_option == 1:
                    ut.show_courier_list()

                elif menu_option == 2:
                    ut.add_courier()


                elif menu_option == 3:
                    ut.update_courier()

                elif menu_option == 4:
                    ut.delete_courier()
                    continue

                else:
                    print("Invalid option. Please choose from menu.")
                    continue

        # Order Menu
        elif user_option == 3:
            while True:
                ut.order_menu()
                menu_option = int(input("\nPlease select from menu: "))
                if menu_option == 0:
                    print("\n>>> >>> Returning to main menu")
                    break

                elif menu_option == 1:  # Print orders from db
                    ut.view_orders()

                elif menu_option == 2:  # New order
                    ut.create_order()

                elif menu_option == 3:  # Update order status
                    ut.update_order_status()

                elif menu_option == 4:  # Update order details
                    ut.update_order()

                elif menu_option == 5:  # Delete order
                    ut.delete_order()

                else:
                    print("Invalid option. Please choose from menu.")
                    break

        else:
            print("Invalid option. Please choose from menu.")
            continue

    except ValueError:
        print("\n**ALERT**\nInvalid menu option. Please start again.")