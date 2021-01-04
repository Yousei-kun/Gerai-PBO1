import database_connector as db_con
import parent_model_file

class Person_Model(parent_model_file.Parent_Model):
    def __init__(self):
        super().__init__('tb_persons', ['PersonID', 'PersonName', 'Username', 'Password', 'PersonAge', 'PersonAddress', 'LevelID'])

    def login_verification(self, username, __password, level):
        query = "SELECT p.Password FROM tb_persons p join tb_level l on p.LevelID = l.LevelID "+ "WHERE Username = '" + username +"' and l.LevelID = "+ level
        if self.get_result(query) == [] or __password != self.get_result(query)[0][0]:
            return False
        elif __password == self.get_result(query)[0][0]:
            return True



