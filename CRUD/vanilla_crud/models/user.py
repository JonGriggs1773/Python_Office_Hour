from config.mysqlconnection import connectToMySQL
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
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result
    
    #! Read
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