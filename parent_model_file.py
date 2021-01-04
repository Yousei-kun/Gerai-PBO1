import database_connector as db_con

class Parent_Model:
    def __init__(self,table,column):
        self.table = table
        self.column = column
        self.database_var = db_con.Database_Connect()
        self.database_var.prepare_database()
    
    def get_all_data(self):
        query = "SELECT * from "+ self.table
        result = self.database_var.execute_query(query)
        return result

    def get_one_column(self, value):
        query = "SELECT "+value +"from "+ self.table
        result = self.database_var.execute_query(query)
        return result

    def get_result(self, query):
        result = self.database_var.execute_query(query)
        return result


    def get_column(self):
        return self.column
    
    def get_table(self):
        return self.table
        