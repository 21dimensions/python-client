from easyeasy.client import Client


class Cat:
    def __init__(self):
        self.id = None
        self.name = None
        self.interests = []
        self.age = None


cat = Cat()
cat.name = "Sam"
cat.age = 1.5
cat.interests = ["play", "eat", "discover"]

# initialize client
client = Client("bc420813-17d9-47fa-9d29-8bd6a1207f8a")

# add object. entity name will be inferred from class name
id = client.add(cat)

# or specify entity name explicitly
id = client.add(cat, "cat")

# get one object by id. Specify entity type. Entity name will be inferred
cat = client.get_one(id, Cat)

# or specify entity name explicitly
cat = client.get_one(id, Cat, "cat")
# at least one should be specified(entity_class or entity_name). In case entity_class not specified, dict object will be returned


# update object
cat.age = 2.0
cat.interests = ["eat", "sleep", "play"]

# object must have id property to distinguish which object is being updated. entity_name can be specified explicitly
client.update(cat)

# get all objects. entity_name can be specified explicitly
cats_collection = client.get(Cat)

# filtering
cats_collection = client.get(Cat, filters={'age': 1.5})  # get 1.5 years old cats
cats_collection = client.get(Cat, filters={'age_gt': 1.0})  # cats older than 1 year
cats_collection = client.get(Cat, filters={"name_like": "Sa*"})  # wildcard

# paging
cats_collection = client.get(Cat, filters={"_start": "10", "_count": 10})  # wildcard

# learn more about filtering operators at: http://easyeasy.io/docs#/operators

# delete object by id
client.delete(cat.id, Cat)
