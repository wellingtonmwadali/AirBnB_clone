#!/usr/bin/python3
"""class BaseModel that defines all common attributes/methods
for other classes"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """class that defines common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """
        constructor of the class
        Initialize BaseModel class with provided argumets"""

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Define string representation of BaseModel object
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates 'self.updated_at' with the current datetime
        and saves the instance to the storage
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary representation of the instance:

        - by using self.__dict__, only instance attributes set will be returned
        - a key __class__ must be added to this dictionary
        - created_at and updated_at must be converted to string object in ISO
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for i, j in self.__dict__.items():
            if i in ("created_at", "updated_at"):
                j = self.__dict__[i].isoformat()
                dict_1[i] = j
        return dict_1
