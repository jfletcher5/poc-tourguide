from sqlite3 import connect
from uuid import uuid4
from services.create_embeddings import create_embeddings_for_pdf



#----------------------------------------------------------------------------------------
# create service to consume a filename string and run create_embeddings_for_pdf
def create_embeddings_with_pdf(lookup: str, filename: str):
    
    create_embeddings_for_pdf(lookup, filename)

    return {"message": f"Embeddings for {filename} created successfully with a lookup of {lookup}"}

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

# query the database for the tour name by the tourID
def get_tour_name(tourID: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # get the tour name from the database by the tourID. if the query result is empty, return message
    cursor.execute("SELECT tourName FROM tours WHERE tourID=?", (tourID,))
    tourName = cursor.fetchone()
    if tourName == None:
        return "No tour found"

    # close the connection
    connection.close()

    # set the message to the tour name
    message = tourName[0]
    

    # return the message
    return message

# get tourIDs by name search
def get_tourIDs_by_name(tourName: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # query the tourIDs from the database by the tourName using a similar search. if the query result is empty, return message
    cursor.execute("SELECT tourID, tourName FROM tours WHERE tourName LIKE ?", (f"%{tourName}%",))
    tourIDs = cursor.fetchall()
    if tourIDs == []:
        return "No tours found"

    # close the connection
    connection.close()

    # set the message to a json of the tourName and tourIDs
    message = []
    for t in tourIDs:
        message.append({"tourID": t[0], "tourName": t[1]})
    

    # return the message
    return message

# delete a tour by the tourID
def delete_tour(tourID: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # delete the tour from the database by the tourID. if something fails set the message to 'failt to delete tour'
    try:
        cursor.execute("DELETE FROM tours WHERE tourID=?", (tourID,))
    except:
        return "Failed to delete tour"

    # commit the changes and close the connection
    connection.commit()
    connection.close()

    # set the message to the tourID
    message = f"Tour {tourID} deleted successfully"
    

    # return the message
    return message