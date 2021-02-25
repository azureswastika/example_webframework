# from abc import ABC, abstractclassmethod

from typing import Union
from patterns import Singleton


class Index:
    auto_id = 0

    def __init__(self) -> None:
        self.id = self.__class__.auto_id
        self.__class__.auto_id += 1


class User(Index):
    def __init__(
        self, username: str, last_name: str, first_name: str, *args, **kwargs
    ) -> None:
        self.username = username
        self.last_name = last_name
        self.first_name = first_name
        super().__init__()


class Teacher(User):
    data = list()

    def __init__(
        self, username: str, last_name: str, first_name: str, *args, **kwargs
    ) -> None:
        self.supervises = list()
        self.__class__.data.append(self)
        super().__init__(username, last_name, first_name, *args, **kwargs)


class Student(User):
    data = list()

    def __init__(
        self, username: str, last_name: str, first_name: str, *args, **kwargs
    ) -> None:
        self.studying = list()
        self.__class__.data.append(self)
        super().__init__(username, last_name, first_name, *args, **kwargs)


class UserFactory(Singleton):
    types = dict(
        [(subclass.__name__.lower(), subclass) for subclass in User.__subclasses__()]
    )

    @classmethod
    def create(
        cls, obj: str, username: str, last_name: str, first_name: str, *args, **kwargs
    ):
        return cls.types[obj.lower()](username, last_name, first_name, *args, **kwargs)


class Category(Index):
    data = list()

    def __init__(self, category: str, *args, **kwargs) -> None:
        self.category = category
        self.courses = list()
        self.__class__.data.append(self)
        super().__init__()


class Course(Index):
    data = list()

    def __init__(self, name: str, category: Category, *args, **kwargs) -> None:
        self.name = name
        self.category = category
        self.__class__.data.append(self)
        super().__init__()


class OfflineCourse(Course):
    def __init__(
        self, name: str, category: Category, address: str = "г. Москва", *args, **kwargs
    ) -> None:
        self.address = address
        super().__init__(name, category, *args, **kwargs)


class InteractiveCourse(Course):
    def __init__(
        self, name: str, category: Category, system: str = "youtube.com", *args, **kwargs
    ) -> None:
        self.system = system
        super().__init__(name, category, *args, **kwargs)


class CourseFactory(Singleton):
    types = dict(
        [(subclass.__name__.lower(), subclass) for subclass in Course.__subclasses__()]
    )

    @classmethod
    def create(cls, obj: str, name: str, category: Category, *args, **kwargs):
        return cls.types[obj.lower()](name, category, *args, **kwargs)


class SiteAdmin:
    @staticmethod
    def create_user(
        role: str, username: str, last_name: str, first_name: str, *args, **kwargs
    ):
        return UserFactory.create(role, username, last_name, first_name)

    @staticmethod
    def create_category(category: str, *args, **kwargs):
        return Category(category)

    @staticmethod
    def create_course(type_: str, name: str, category: Category, *args, **kwargs):
        return CourseFactory.create(type_, name, category)

    @staticmethod
    def get(obj: Union[User, Category, Course], **kwargs):
        if kwargs:
            data = list()
            for u in obj.data:
                for values, index in zip(kwargs.items(), range(len(kwargs))):
                    if values not in u.__dict__.items():
                        break
                    if index + 1 == len(kwargs):
                        data.append(u)
            return data
        return obj.data
