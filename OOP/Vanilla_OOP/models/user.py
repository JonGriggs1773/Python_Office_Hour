from config.mysqlconnection import connectToMySQL
from flask import session
import pprint

class User:
    db = "users_practice_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.about = data['about']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #! Create
    @classmethod
    def create_user(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email, about)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(about)s)
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        print("New User's ID: ", results)
        session['user_id'] = results
        return results







    #! Read
    @classmethod
    def get_all_users(cls):
        query = """
                SELECT *
                FROM users
                """
        all_users = []
        results = connectToMySQL(cls.db).query_db(query)
        pprint.pp(results)
        for each_user in results:
            all_users.append(cls(each_user))
        return all_users





    #! Update





    #! Delete