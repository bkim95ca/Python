from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import dog_model

class Award:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dog_id = data['dog_id']
        
    @classmethod
    def create(cls, data):
        query = "INSERT INTO awards (title, dog_id) VALUES (%(title)s, %(dog_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM awards JOIN dogs ON dogs.id = dog_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_awards = []
        for row_from_db in results:
            award_instance = cls(row_from_db)
            dog_data = {
                **row_from_db,
                'id' : row_from_db['dogs.id'],
                'updated_at' : row_from_db['dogs.updated_at'],
                'created_at' : row_from_db['dogs.created_at']
            }
            dog_instance = dog_model.Dog(dog_data)
            award_instance.recipient = dog_instance
            all_awards.append(award_instance)
        return all_awards
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM awards JOIN dogs on dogs.id = dog_id where awards.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            row_from_db = results[0]
            award_instance = cls(row_from_db)
            dog_data = {
                **row_from_db,
                'id' : row_from_db['dogs.id'],
                'updated_at' : row_from_db['dogs.updated_at'],
                'created_at' : row_from_db['dogs.created_at']
            }
            dog_instance = dog_model.Dog(dog_data)
            award_instance.recipient = dog_instance
            return award_instance
        return False
    