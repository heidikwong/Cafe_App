# products = []
# # with open("products.txt", "r") as file:  # open file r-mode
# #     for line in file.readlines():        # loop through & read lines
# #         products.append(line.strip())    # append to list
# # new_product = input("Please add a product to your list: ")
# # products.append(new_product)             # append item to list
# # with open("products.txt", "w") as file:  # open list.txt
# #     for product in products:             # loop through list
# #         file.write(product + "\n")       # write into list.txt


# # def product_menu():
# #     print("Product menu")
# #     user_input = input("please select an option from the product menu")
# #     return user_input

# # product_user_input = product_menu()
import pandas as pd

products = pd.read_csv("database/product_list.csv")
print(products)

#turn dataframe to dict
product_list = products.to_dict('records')
print(product_list)


#load csv -> into a dict
# df = pd.DataFrame(product_list)
# print(df)

#dict -> write into csv only values

