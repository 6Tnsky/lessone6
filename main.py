class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'стандарт'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__users_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__users_list.append(user)
            print(f"Бездельник {user.get_name()} добавлен.")
        else:
            print("Сотрудник не добавлен.")

    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f"Бездельник {user.get_name()} уволен.")
                return
        print("сотрудник не найден.")

    def list_users(self):
        print("У нас работает:")
        for user in self.__users_list:
            print(f"ID: {user.get_user_id()}, Зовут: {user.get_name()}, Уровень: {user.get_access_level()}")

# Тест
admin = Admin(1, "Коля")
user1 = User(2, "Марат")
user2 = User(3, "Ежик")
user3 = User(3, "Ленин")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.list_users()

admin.remove_user(2)
admin.list_users()