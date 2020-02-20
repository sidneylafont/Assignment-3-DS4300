from pymongo import MongoClient

client = MongoClient()

db = client.catalog
pcol = db.products

# takes in the category, a string, and a dictOfSpecs, a dictionary containing desired key value pairs, returns a
# list of all matching products in the product catalog
def queryCatalog(category, dictOfSpecs):
    dictOfSpecs["category"] = category
    return list(pcol.find(dictOfSpecs))


def main():
    dict_of_specs_1 = {"diameter": 44, "brand": "Tommy Hilfiger", "dial-color": "beige"}
    print(queryCatalog("watch", dict_of_specs_1))
    # returns [{'_id': ObjectId('5e4db15311d293698b595b39'), 'id': 1.0, 'category': 'watch', 'diameter': 44.0, 'brand': 'Tommy Hilfiger', 'dial-color': 'beige'}]

    dict_of_specs_2 = {"brand": "Tommy Hilfiger"}
    print(queryCatalog("watch", dict_of_specs_2))
    # returns [{'_id': ObjectId('5e4db15311d293698b595b39'), 'id': 1.0, 'category': 'watch', 'diameter': 44.0, 'brand': 'Tommy Hilfiger', 'dial-color': 'beige'},
    # {'_id': ObjectId('5e4db19811d293698b595b3a'), 'id': 2.0, 'category': 'watch', 'diameter': 30.0, 'brand': 'Tommy Hilfiger', 'dial-color': 'red'}]

    dict_of_specs_3 = {"diameter": 100}
    print(queryCatalog("wine", dict_of_specs_3))
    # returns [] because wines don't have diameters

main()


##EXAMPLES OF OUR DATA IN MONGO DATA IN MONGO

##db.products.insert({"id": 1, "category": "watch", "diameter": 44, "brand": "Tommy Hilfiger", "dial-color": "beige", "price" : 10, is_available: true})
##db.products.insert({"id": 2, "category": "watch", "diameter": 30, "brand": "Tommy Hilfiger", "dial-color": "red", "price" : 1000, is_available: false})
##db.products.insert({"id": 3, "category": "watch", "diameter": 45, "brand": "Timex", "dial-color": "blue", "price" : 0, is_available: true})

##db.products.insert({"id": 1, "category": "wine", "winery": "sid's winery", "type": "red", "year-bottled": 1824, "price" : 20000, is_available: false})
##db.products.insert({"id": 2, "category": "wine", "winery": "hari's winery", "type": "white", "year-bottled": 1972, "price" : 1, is_available: true})

##db.products.insert({"id": 1, "category": "car", "company": "toyota", "model": "rav-4", "year": 2007, "price" : 20000, is_available: true})
##db.products.insert({"id": 2, "category": "car", "company": "honda", "model": "civic", "year": 2002, "price" : 7000000, is_available: true})
