users = []

class UserModel(object):
    """Class user models."""

    def __init__(self):
      self.db = users 

    def add_user(self,fname,lname,email,phone,password,city):
        """ Method for saving user to the dictionary """
        payload = {
            "userId": len(self.db)+1,
            "fname" : fname,
            "lname" : lname,
            "email" :  email,
            "phone":  phone,
            "password" : password,
            "city": city
         
        }

        self.db.append(payload)
    
    
    def get_all_uers(self):
        """ Method for getting all available users in the dictionary """
        return self.db
        
    
    def get_user(self,userId):
        """ Method for getting a user by userId"""
        user = [user for user in self.db if userId==user["userId"]]
        return user
    

    



    