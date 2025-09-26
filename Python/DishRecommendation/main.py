

menu_item_list = [
{
    "item_id": "1",
    "item_name": "Dal Tadka",
    "item_description": "Dal with a Tadka",
    "item_price": 200,
    "item_category": "Main Course",
    "allergen": "Dairy",
    "dish_of_the_day": "Y"
},
{
    "item_id": "2",
    "item_name": "Dal Makhani",
    "item_description": "Dal with a Makkhan",
    "item_price": 300,
    "item_category": "Main Course",
    "allergen": "Dairy",
    "dish_of_the_day": "N"
},
{
    "item_id": "3",
    "item_name": "Paneer Pasanda",
    "item_description": "Paneer pasand ka",
    "item_price": 600,
    "item_category": "Main Course",
    "allergen": "Dairy",
    "dish_of_the_day": "N"
},
{
    "item_id": "4",
    "item_name": "Spring Roll",
    "item_description": "Rolled Spring",
    "item_price": 200,
    "item_category": "Starter",
    "allergen": "",
    "dish_of_the_day": "N"
},
{
    "item_id": "5",
    "item_name": "Paneer Pakoda",
    "item_description": "Pakoda stuffed with Paneer",
    "item_price": 600,
    "item_category": "Starter",
    "allergen": "Dairy",
    "dish_of_the_day": "N"
}
]

menu_item_dict = {item["item_name"]: item for item in menu_item_list}


item_stock_list = [
{
    "item_id": "1",
    "item_name": "Dal Tadka",
    "item_stock": 0
},
{
    "item_id": "2",
    "item_name": "Dal Makhani",
    "item_stock": 15
},
{
    "item_id": "3",
    "item_name": "Paneer Pasanda",
    "item_stock": 5
},
{
    "item_id": "4",
    "item_name": "Spring Roll",
    "item_stock": 20
},
{
    "item_id": "5",
    "item_name": "Paneer Pakoda",
    "item_stock": 25
}
]

item_stock_dict = {item["item_id"]: item for item in item_stock_list}

item_rating_list = [
{
    "item_id": "1",
    "item_name": "Dal Tadka",
    "item_rating": 4.0,
    "number_of_ratings": 3
},
{
    "item_id": "2",
    "item_name": "Dal Makhani",
    "item_rating": 4.5,
    "number_of_ratings": 5
},
{
    "item_id": "3",
    "item_name": "Paneer Pasanda",
    "item_rating": 5.0,
    "number_of_ratings": 4
},
{
    "item_id": "4",
    "item_name": "Spring Roll",
    "item_rating": 2.0,
    "number_of_ratings": 7
},
{
    "item_id": "5",
    "item_name": "Paneer Pakoda",
    "item_rating": 2.5,
    "number_of_ratings": 2
}
]

item_rating_dict = {item["item_id"]: item for item in item_rating_list}


# O(n)- Optimize to O(1)
def dish_of_the_day():
    dish = input("Dish of the day: ")

    for item_name, item in menu_item_dict.items():
        if item["item_name"] == dish:
            item["dish_of_the_day"] = "Y"
        else:
            item["dish_of_the_day"] = "N"

    # for item_id, item in menu_item_dict.items():
    #     print(item_id, item)


# O(nlogn)- Optimize to O(logn)
# Which sort algo here, stable sort?
def reco_dish():
    dish_of_day_item = [item["item_name"] for item in menu_item_dict.values() if item["dish_of_the_day"] == "Y"]
    print(dish_of_day_item[0])
    dish_of_day_stock = [item["item_stock"] for item in item_stock_dict.values()
                         if item["item_name"] == dish_of_day_item[0]]
    print(dish_of_day_stock[0])
    recommended_dish = ""
    if dish_of_day_stock[0] != 0:
        recommended_dish = dish_of_day_item[0]
    else:
        sorted_items = sorted(item_rating_dict.values(), key=lambda x: x['item_rating'], reverse=True)
        item_names_descending_ratings = [item['item_name'] for item in sorted_items]
        print(item_names_descending_ratings)
        item_stock = {}
        # for item_name in item_names_descending_ratings:
        #     print("outside" + item_name)
        #     if item_name in item_stock_dict["item_name"]:
        #         print("inside" + item_name)
        #         stock = item_stock_dict[item_name]["item_stock"]
        #         print(stock)
        #         item_stock[item_name] = (stock)

        for item_name in item_names_descending_ratings:
            print("outside : " + item_name)
            print(item_stock_dict)
            if item_name.strip() in item_stock_dict:
                print("inside : " + item_name)
                print(item_stock_dict)

                stock = item_stock_dict[item_name]["item_stock"]
                print(stock)
                item_stock[item_name] = (stock)

        print(item_stock)

    # print("recommended_dish: " + recommended_dish)


# O(1), worst case when resizing requires then O(n)
def add_dish(item_id, item_name, item_description, item_price, item_category, allergen, dish_of_the_day):
    # New record to be added
    new_record_menu = {
        "item_id": item_id,
        "item_name": item_name,
        "item_description": item_description,
        "item_price": item_price,
        "item_category": item_category,
        "allergen": allergen,
        "dish_of_the_day": dish_of_the_day
        }
    # Add the new record to the dictionary
    menu_item_dict[new_record_menu["item_name"]] = new_record_menu

    new_record_stock = {
        "item_id": item_id,
        "item_name": item_name,
        "item_stock": 0
    }

    item_stock_dict[new_record_stock["item_id"]] = new_record_stock

    new_record_rating = {
        "item_id": item_id,
        "item_name": item_name,
        "item_rating": 0,
        "number_of_ratings": 0
    }

    item_rating_dict[new_record_rating["item_id"]] = new_record_rating


# O(n)- Optimize to O(1)
def rate_dish(dish, rating):
    for item_name, item in item_rating_dict.items():
        if item["item_name"] == dish:
            item["item_rating"] = (item["item_rating"] * item["number_of_ratings"] + rating) / (item["number_of_ratings"] + 1)
            item["number_of_ratings"] = item["number_of_ratings"] + 1
            break


# O(n)- Optimize to O(1)
def add_remove_dish_stock(dish, qty):
    for item_name, item in item_stock_dict.items():
        if item["item_name"] == dish:
            item["item_stock"] += qty
            break


# dish_of_the_day()
# add_dish("6", "Paneer Tikka", "Grilled paneer with spices", 600, "Starter", "Dairy", 4.5, "N")
# add_remove_dish_stock("Spring Roll", 15)
# rate_dish("Paneer Pakoda", 4)

reco_dish()

# for item_id, item in menu_item_dict.items():
#     print(item_id, item)
#
# for item_id, item in item_stock_dict.items():
#     print(item_id, item)
#
# for item_id, item in item_rating_dict.items():
#     print(item_id, item)



# if __name__ == '__main__':
#     print_hi('PyCharm')
