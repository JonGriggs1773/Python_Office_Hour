from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import pet
from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)
import pprint
import re


class User:
    db = "users_and_pets"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.about = data['about']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.pets = []

    #! Create

    #todo This is a boring create method, so let's add some things to it.
    @classmethod
    def create_user(cls, data):
        if not cls.user_validations(data):
            return False
        parsed_data = cls.parse_user_data(data)
        query = """
                INSERT INTO users (first_name, last_name, email, about, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(about)s, %(password)s)
                """
        user_id = connectToMySQL(cls.db).query_db(query, parsed_data)
        print(user_id)
        session['user_id'] = user_id
        session['full_name'] = f"{parsed_data['first_name']} {parsed_data['last_name']}"
        return True
    
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
        
    @classmethod
    def get_one_user_by_email(cls, email):
        data = {"email": email}
        query = """
                SELECT *
                FROM users
                WHERE email = %(email)s
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
    
    #todo Add Validations
    

    @staticmethod
    def user_validations(form_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if len(form_data['first_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid = False
        if len(form_data['last_name']) < 2:
            flash("Last name must be at least 2 characters")
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']):
            flash('Email must be in proper format')
            is_valid = False
        if User.get_one_user_by_email(form_data['email']):
            flash('Email is already in our system, please try again')
            is_valid = False
        if form_data['password'] != form_data['confirm_password']:
            flash('Password and Confirm Password do not match')
            is_valid = False
        if len(form_data['password']) <= 8:
            flash('Password must be at least 8 characters')
            is_valid = False
        return is_valid
    
    @staticmethod
    def parse_user_data(form_data):
        parsed_data = {}
        parsed_data['first_name'] = form_data['first_name']
        parsed_data['last_name'] = form_data['last_name']
        parsed_data['email'] = form_data['email']
        parsed_data['about'] = form_data['about']
        parsed_data['password'] = bcrypt.generate_password_hash(form_data['password'])
        return parsed_data
    
    @staticmethod
    def login_user(data):
        this_user = User.get_one_user_by_email(data['email'])
        if this_user:
            print('Got this boi/goi')
            if bcrypt.check_password_hash(this_user.password, data['password']):
                session['user_id'] = this_user.id
                session['full_name'] = f"{this_user.first_name} {this_user.last_name}"
                return True
            else:
                flash('Your login failed')
                return False
        else:
            flash('Your login failed')
            return False

