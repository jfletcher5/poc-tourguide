from sqlite3 import connect
from uuid import uuid4

# insert a new record in to the tours table in the sqlite3 database. input variables will be tourName, tourDescription, and tourCategory
def create_tour(tourName: str, tourDescription: str, tourCategory: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # create a new tourID
    tourID = str(uuid4())

    # insert the new tour into the database. if table doesn't exist, create it. if something fails set the message to 'failt to create tour'
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS tours (tourID TEXT PRIMARY KEY, tourName TEXT, tourDescription TEXT, tourCategory TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute("INSERT INTO tours (tourID, tourName, tourDescription, tourCategory) VALUES (?, ?, ?, ?)", (tourID, tourName, tourDescription, tourCategory))
    except:
        return "Failed to create tour"


    # commit the changes and close the connection
    connection.commit()
    connection.close()

    # set the message to the conversation name
    message = f"Tour created with ID: {tourID, tourName, tourDescription, tourCategory}"
    

    # return the message
    return message