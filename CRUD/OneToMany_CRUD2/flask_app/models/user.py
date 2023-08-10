from flask_app.config.mysqlconnection import connectToMySQL
import pprint
from flask_app.models import pet


class User:
    db = "users_and_pets"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.about = data['about']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pets = []

    #! Create
    @classmethod
    def create_user(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email, about)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(about)s)
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result
    
    #! Read_All
    @classmethod
    def get_all_users(cls):
        query = """
                SELECT *
                FROM users
                """
        results = connectToMySQL(cls.db).query_db(query)
        pprint.pp(results)
        all_users = []
        for each_user in results:
            all_users.append(cls(each_user))
        return all_users
    
    #! Update
    @classmethod
    def update_user_by_id(cls, data):
        query = """
                UPDATE users
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, about = %(about)s
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results: ", results)
        return results

    @classmethod
    def get_one_user_by_id(cls, data):
        query = """
                SELECT *
                FROM users
                WHERE id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results: ", results)
        if results:
            one_user = cls(results[0])
            return one_user
        else:
            print("User was not gettable")
            return False

    #! Delete
    @classmethod
    def delete_user_by_id(cls, data):
        query = """
                DELETE
                FROM users
                WHERE id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results: ", results)
        return results
    
    #! Read_One_With_Child
    @classmethod
    def get_one_user_with_pets(cls, data):
        query = "SELECT * FROM users LEFT JOIN pets ON user_id=users.id WHERE users.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db( query , data )
        user = cls(results[0])
        for row_from_db in results:
            pet_data = {
                "id": row_from_db["pets.id"],
                "name": row_from_db["name"],
                "species": row_from_db["species"],
                "how_many_legs": row_from_db["how_many_legs"],
                "friendly": row_from_db["friendly"],
                "created_at": row_from_db["pets.created_at"],
                "updated_at": row_from_db["pets.updated_at"],
                "user_id":row_from_db["user_id"]
            }
            user.pets.append(pet.Pet(pet_data))
        print(user.pets)
        return user
    
    @classmethod
    def get_all_users_with_pets(cls):
        query = "SELECT * FROM users LEFT JOIN pets ON user_id=users.id;"
        results = connectToMySQL(cls.db).query_db( query )

        all_users_with_pets = [ ]

        for row in results:
            # new_user = True

            one_pet_info = {
                "id": row["pets.id"],
                "name": row["name"],
                "species": row["species"],
                "how_many_legs": row["how_many_legs"],
                "friendly": row["friendly"],
                "created_at": row["pets.created_at"],
                "updated_at": row["pets.updated_at"],
                "user_id":row["user_id"]
            }

            if (len(all_users_with_pets) == 0) or (row['id'] != all_users_with_pets[len(all_users_with_pets)-1].id):
                one_user_instance = cls(row)
                print("one user instance", one_user_instance)

                if one_pet_info['id'] != None:

                    one_pet_instance = pet.Pet(one_pet_info)
                    print("one pet instance", one_pet_instance)

                    one_user_instance.pets.append(one_pet_instance)

                all_users_with_pets.append(one_user_instance)

            else:
                if one_pet_info['id'] != None:

                    one_pet_instance = pet.Pet(one_pet_info)
                    print("one pet instance", one_pet_instance)
                
                    all_users_with_pets[len(all_users_with_pets)-1].pets.append(one_pet_instance)

        return all_users_with_pets