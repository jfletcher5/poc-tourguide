from sqlite3 import connect
from uuid import uuid4



# instert a new record in to the conversations table in the sqlite3 database. input variables will be userID, tourID, and conversationName
def create_conversation(userID: str, tourID: str, conversationName: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # create a new conversationID
    conversationID = str(uuid4())

    # insert the new conversation into the database. if table doesn't exist, create it. if something fails set the message to 'failt to create conversation'
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS conversations (conversationID TEXT PRIMARY KEY, conversationName TEXT, userID TEXT, tourID TEXT)")
        cursor.execute("INSERT INTO conversations (conversationID, conversationName, userID, tourID) VALUES (?, ?, ?, ?)", (conversationID, conversationName, userID, tourID))
    except:
        return "Failed to create conversation"


    # commit the changes and close the connection
    connection.commit()
    connection.close()

    # set the message to the conversation name
    message = f"Conversation created with ID: {conversationID}"
    

    # return the message
    return message
#----------------------------------------------------------------------------------------
# get the conversation name from the conversationID
def get_conversation_name(conversationID: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # get the conversation name from the database. if the conversationID doesn't exist, return message
    cursor.execute("SELECT conversationName FROM conversations WHERE conversationID=?", (conversationID,))
    conversationName = cursor.fetchone()
    if conversationName == None:
        return "Conversation not found"

    # close the connection
    connection.close()

    # set the message to the conversation name
    message = f"Conversation name found: {conversationName[0]}"
    

    # return the message
    return message
#----------------------------------------------------------------------------------------
# delete a conversation from the database by the conversationID
def delete_conversation(conversationID: str):

    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # delete the conversation from the database
    cursor.execute("DELETE FROM conversations WHERE conversationID=?", (conversationID,))

    # commit the changes and close the connection
    connection.commit()
    connection.close()
#----------------------------------------------------------------------------------------
# get all conversations by the userID
def get_conversations_by_userID(userID: str):

    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # get the conversation name from the database. if the conversationID doesn't exist, return message. I want the results formatted as a json object
    cursor.execute("SELECT conversationID, conversationName FROM conversations WHERE userID=?", (userID,))
    conversations = cursor.fetchall()
    if conversations == None:
        return "Conversations not found"
    
    # convert the results to a json with the names and conversationID paired
    conversations = {conversation[1]: conversation[0] for conversation in conversations}


    # close the connection
    connection.close()

    # set the message to the conversation name
    message = conversations
    

    # return the message
    return message

#----------------------------------------------------------------------------------------

