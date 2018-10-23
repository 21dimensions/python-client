import requests
import json


class Client:
    def __init__(self, key, root_url="http://easyeasy.io/v1/rest"):
        self.rootUrl = root_url
        self.key = key

    def __get_entity_name(self, entity_class, entity_name):
        if entity_class is None and entity_name is None:
            raise Exception("specify entity_class or entity_name parameters")
        elif entity_name is not None:
            return entity_name
        elif entity_class is not None:
            return entity_class.__name__.lower()

    def __get_url(self, entity_name):
        return self.rootUrl+"/"+entity_name

    def __get_headers(self):
        return {"Authorization": "Key " + self.key, "Content-Type": "application/json"}

    def add(self, entity, entity_name=None):
        """
        add new entity. Entity name will be inferred from entity class name(class Cat - cat) or you can specify entity_name explicitly
        """
        response = requests.post(self.__get_url(self.__get_entity_name(type(entity), entity_name)),
                                 json.dumps(entity.__dict__), json=True, headers=self.__get_headers())

        response.raise_for_status()
        response_obj = response.json()
        return response_obj["id"]

    def get_one(self, id, entity_class=None, entity_name=None):
        """
        get one object by id. Entity name will be inferred from entity class name(class Cat - cat) or you can specify entity_name explicitly. At least one of them should be specified
        """
        response = requests.get(self.__get_url(self.__get_entity_name(entity_class, entity_name)) + "/"+id,
                                headers=self.__get_headers())

        response.raise_for_status()
        response_obj = response.json()

        result = response_obj

        if entity_class is not None:
            result = entity_class()
            result.__dict__ = response_obj

        return result

    def update(self, entity, entity_name=None):
        """
        update object. Object must have id property to distinguish which object is being updated. entity_name can be specified explicitly
        """
        if 'id' not in entity.__dict__:
            raise Exception('updated object must have id property')

        response = requests.put(self.__get_url(self.__get_entity_name(type(entity), entity_name)) + "/" + entity.id,
                                json.dumps(entity.__dict__), json=True, headers=self.__get_headers())

        response.raise_for_status()

    def get(self, entity_class=None, entity_name=None, query=None):
        """
        get objects collection. Entity name will be inferred from entity class name(class Cat - cat) or you can specify entity_name explicitly. At least one of them should be specified.
        """
        filtering_str = ""
        if query is not None:
            filtering_str = "&".join(
                [str(k)+"="+str(query[k]) for k in query])

        response = requests.get(self.__get_url(self.__get_entity_name(entity_class, entity_name)) + "?" + filtering_str,
                                headers=self.__get_headers())

        response.raise_for_status()
        response_obj = response.json()

        items = []

        if entity_class is not None:
            for response_item in response_obj['items']:
                item = entity_class()
                item.__dict__ = response_item
                items.append(item)
        else:
            items = response_obj['items']

        class ItemsCollections:
            pass

        result = ItemsCollections()
        result.total = response_obj['total']
        result.items = items

        return result

    def delete(self, id, entity_class=None, entity_name=None):
        """
        delete object by id. Specify entity_class or entity_name
        """
        response = requests.delete(self.__get_url(self.__get_entity_name(entity_class, entity_name)) + "/" + id,
                                headers=self.__get_headers())

        response.raise_for_status()
