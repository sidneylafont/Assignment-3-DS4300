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
    dict_of_specs = {"diameter": 44, "brand": "Tommy Hilfiger", "dial-color": "beige"}
    print(queryCatalog("watch", dict_of_specs))


main()
