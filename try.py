import pymysql
connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='pass1',
                                 database='Cafe_DB',
                                 charset='utf8mb4')


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