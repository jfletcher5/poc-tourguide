from sqlite3 import connect
from uuid import uuid4

# instert a new record in to the messages table in the sqlite3 database. input variables will be role, content, and conversationID
def create_message(role: str, content: str, conversationID: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # create a new messageID
    messageID = str(uuid4())

    # insert the new message into the database. if table doesn't exist, create it. if something fails set the message to 'failt to create message'
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS messages (messageID TEXT PRIMARY KEY, role TEXT, content TEXT, conversationID TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute("INSERT INTO messages (messageID, role, content, conversationID) VALUES (?, ?, ?, ?)", (messageID, role, content, conversationID))
    except:
        return "Failed to create message"


    # commit the changes and close the connection
    connection.commit()
    connection.close()

    # set the message to the conversation name
    message = f"Message created with ID: {messageID}"
    

    # return the message
    return message


#----------------------------------------------------------------------------------------

# return all messages in a conversation by the conversationID
def get_messages_by_conversationID(conversationID: str):
    # create a connection to the database
    connection = connect("./instance/sqlite.db")
    cursor = connection.cursor()

    # get all messages from the database by the conversationID. if the query result is empty, return message. order by created_at desc
    cursor.execute("SELECT * FROM messages WHERE conversationID=? ORDER BY created_at DESC", (conversationID,))
    messages = cursor.fetchall()
    if messages == []:
        return "No messages found"

    # close the connection
    connection.close()

    # set the message to a json object of the messages
    message = []
    for m in messages:
        message.append({"messageID": m[0], "role": m[1], "content": m[2], "conversationID": m[3], "created_at": m[4]})
    

    # return the message
    return message