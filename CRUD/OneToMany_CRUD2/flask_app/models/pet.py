from config.mysqlconnection import connectToMySQL
import pprint
from flask_app.models import user


class Pet:
    db = "users_and_pets_office_hour"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.species = data['species']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.owner = None

    #! Create
    @classmethod
    def create_pet(cls, data):
        query = """
                INSERT INTO pets (name, species, user_id)
                VALUES (%(name)s, %(species)s, %(user_id)s)
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result
    
    #! Read_All
    @classmethod
    def get_all_pets(cls):
        query = """
                SELECT *
                FROM pets
                """
        results = connectToMySQL(cls.db).query_db(query)
        pprint.pp(results)
        all_pets = []
        for each_pet in results:
            all_pets.append(cls(each_pet))
        return all_pets
    
    #! Update
    @classmethod
    def update_pet_by_id(cls, data):
        query = """
                UPDATE pets
                SET name = %(name)s, species = %(species)s
                WHERE id = %(id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results: ", results)
        return results

    @classmethod
    def get_one_pet_by_id(cls, data):
        query = """
                SELECT *
                FROM pets
                WHERE id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results: ", results)
        if results:
            one_pet = cls(results[0])
            return one_pet
        else:
            print("Pet was not gettable")

    #! Delete
    @classmethod
    def delete_pet_by_id(cls, data):
        query = """
                DELETE
                FROM pets
                WHERE id = %(id)s
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("Results: ", results)
        return results
    
    #! Read_One_With_Child
    @classmethod
    def get_one_user_with_pets(cls, data):
        query = "SELECT * FROM users LEFT JOIN pets ON user_id=user.id WHERE user.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db( query , data )
        user = cls(results[0])
        
        for row_from_db in results:
            pet_data = {
                "id": row_from_db["pets.id"],
                "name": row_from_db["name"],
                "species": row_from_db["species"],
                "friendly": row_from_db["friendly"],
                "created_at": row_from_db["pets.created_at"],
                "updated_at": row_from_db["pets.updated_at"],
                "user_id":row_from_db["user_id"]
            }
            user.pets.append(pet.Pet(pet_data))
        print(user.pets)
        return user