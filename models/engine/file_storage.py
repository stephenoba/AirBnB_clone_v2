#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = FileStorage.__objects
        if cls:
            filtered_objs = {}

            for k, v in objs.items():
                if isinstance(v, cls):
                    filtered_objs[k] = v
            return filtered_objs
        return objs

    def new(self, obj):
        """Adds new object to storage dictionary"""
        _key = self.build_obj_key(obj)
        self.all().update({_key: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls = self.get_class(val['__class__'])
                    self.all()[key] = cls(**val)
        except (FileNotFoundError, KeyError):
            pass

    def delete(self, obj=None):
        """delete an object from __objects"""
        if obj:
            key = self.build_obj_key(obj)
            self.all().pop(key)
            del obj
            self.save()

    # HELPER METHODS
    # =============================================

    def get_class(self, cls_name):
        """get corresponding class from string"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
        }

        return classes[cls_name]

    def build_obj_key(self, obj):
        """Build or retrieve obj key in __objects"""
        _key = obj.to_dict()['__class__'] + '.' + obj.id
        return _key
