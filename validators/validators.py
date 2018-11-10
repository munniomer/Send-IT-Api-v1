import re

class Validators:
    """class validators"""
    def valid_name(self,name):
        """validate first name and last name"""
        regex = "^[a-zA-Z]{1,}$"
        return re.match(regex, name)
    
    def valid_email(self, email):
        """ valid email """
        regex = "^[^@]+@[^@]+\\.[^@]+$"
        return re.match(regex,email)

    def valid_password(self, password):
        """ valid email """
        regex = "^[a-zA-Z0-9]{3,}$"
        return re.match(regex,password)

    
   
 