def queryCatalog(category, dictOfSpecs):
    query = "db.products.find({\"category\":\"" + category + "\","
    for key, value in dictOfSpecs.items():
        if isinstance(value, str):
            query = query + "\"" + key + "\":\"" + value + "\","
        else:
            query = query + "\"" + key + "\":" + str(value) + ","
    query = query[:-1]
    query = query + "})"

    print(query)


def main():
    dict_of_specs = {"winery": "sid's winery", "type": "red", "year-bottled": "1824"}
    queryCatalog("wine", dict_of_specs)


main()


##DATA IN MONGO //remake data for wine and car year

##db.products.insert({"id": 1, "category": "watch", "diameter": 44, "brand": "Tommy Hilfiger", "dial-color": "beige"})
##db.products.insert({"id": 2, "category": "watch", "diameter": 30, "brand": "Tommy Hilfiger", "dial-color": "red"})
##db.products.insert({"id": 3, "category": "watch", "diameter": 45, "brand": "Timex", "dial-color": "blue"})

##db.products.insert({"id": 1, "category": "wine", "winery": "sid's winery", "type": "red", "year-bottled": "1824"})
##db.products.insert({"id": 2, "category": "wine", "winery": "hari's winery", "type": "white", "year-bottled": "1972"})

##db.products.insert({"id": 1, "category": "car", "company": "toyota", "model": "rav-4", "year": "2007"})
##db.products.insert({"id": 2, "category": "car", "company": "honda", "model": "civic", "year": "2002"})
