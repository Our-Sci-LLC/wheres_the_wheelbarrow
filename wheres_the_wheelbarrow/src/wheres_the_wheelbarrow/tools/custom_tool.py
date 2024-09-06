#from crewai_tools import BaseTool
#from PIL import Image
#import glob

#class DatabaseInitializer(BaseTool):
#    name: str = "Database Initializer"
#    description: str = (
#        "This tool is useful for creating a database."
#    )
#
#    def _run(self, argument: str) -> str:
#        connection = sqlite3.connect("database.db")
#        cursor = connect.cursor()
#        cursor.execute('''
#            CREATE TABLE IF NOT EXISTS inventory (
#                id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                object_name TEXT, 
#                location TEXT
#            )
#        ''')
#        connection.commit()
#        connection.close()
#        return "Database initally created"

#class DatabaseInsert(BaseTool):
#    name: str = "Database Inserter"
#    description: str = (
#        "This tool is useful for inserting values into a database."
#    )

#    def _run(self, object_name: str, location: str) -> str:
#        connection = sqlite3.connect("database.db")
#        cursor = connect.cursor()
#        query = '''
#            INSERT INTO inventory (object_name, location) VALUES (?, ?)
#        '''
#        #cursor.executemany(query, [(item[object_name], item[location]) for item in data["objects"]])
#        cursor.execute(query, (object_name, location))
#        connection.commit()
#        connection.close()
#        return "Database updated with object: {} at location: {}".format(object_name, location)

#class DatabaseRetrieval(BaseTool):
#    name: str = "Database Retriever"
#    description: str = (
#        "This tool is useful for retrieving values from a database."
#    )

#    def _run(self, argument: dict) -> dict:
#        connection = sqlite3.connect("database.db")
#        cursor = connect.cursor()
#        query = '''
#            SELECT id, object_name, location FROM inventory
#        '''
#        cursor.execute(query)
#        rows = cursor.fetchall()
#        connection.close()
#
#        inventory_data = [{"id": row[0], "object_name": row[1], "location": row[2]} for row in rows]
#
#        return inventory_data

#class ImageRetrievalTool(BaseTool):
#    name: str = "ImageRetrieval"
#    description: str = "Prompts the user for an image path and preprocesses the image."
#
#    def _run(self, input: str = None) -> str:
#        if input is None:
#            return "Please provide the image path."
#        else:
#            filename = glob.glob(input + '*.png')
#            image = Image.open(file_path)
#            return image