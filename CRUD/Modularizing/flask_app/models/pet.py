from flask_app.config.mysqlconnection import connectToMySQL
import pprint
from flask_app.models import user


class Pet:
    db="users_and_pets"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.species = data['species']
        self.how_many_legs = data['how_many_legs']
        self.friendly = data['friendly']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        # self.owner = None

    @classmethod
    def create_pet(cls, data):
        query = """
                INSERT INTO pets (name, species, how_many_legs, friendly, user_id)
                VALUES (%(name)s, %(species)s, %(how_many_legs)s, %(friendly)s, %(user_id)s)
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        print("create pet method in pet model",result)
        return result