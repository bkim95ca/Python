from curses import flash
from BK_UsersCR.config.mysqlconnection import connectToMySQL
from BK_UsersCR import DATABASE
from flask import Flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results)
        all_users = []
        for row_from_db in results:
            user_instance = cls(row_from_db)
            all_users.append(user_instance)
        return all_users
    
    #adds a user to the database
    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    
    #fetches one user from database
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            return False
        user_instance = cls(results[0])
        return user_instance
        
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def validate_registration(data:dict)->bool:
        is_valid = True
        
        if len(data['first_name']) <= 0:
            flash("first_name is required")
            is_valid = False
        
        if len(data['last_name']) <= 0:
            flash("last_name is required")
            is_valid = False
        
        if len(data['email']) <= 0:
            flash("email is required")
            is_valid = False
            
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        
        if len(data['pw']) <= 0:
            flash("pw is required")
            is_valid = False
        
        if len(data['confirm_pw']) <= 0:
            flash("confirm_pw is required")
            is_valid = False
        
        if data['pw'] != data["confirm_pw"]:
            flash("passwords do not match")
            is_valid = False
        
        return is_valid