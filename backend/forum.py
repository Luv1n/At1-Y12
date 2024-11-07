from flask import abort
from datetime import datetime
from classes.forum import Forum
from data import forums, users, admin_retrieve_author_name
from classes.user import User
import html

# Dictionary to store forums by their numeric ID
next_forum_id = 1  # This will serve as our auto-incrementing ID

def user_create_forum(forum_title, forum_question, session_token):
    global next_forum_id
     #input validation
    if forum_title is None: 
        abort(401, description="Forum Title cannot be empty")
    if forum_question is None:
        abort(401, description="Forum Question cannot be empty")
    
    #ESCAPE TO PREVENT XXS

    forum_question = html.escape(forum_question)
    forum_title = html.escape(forum_title)
    


    # Create a new Forum object
    author = admin_retrieve_author_name(session_token)
    new_forum = Forum(
        id=next_forum_id,
        title=forum_title,
        author=author,  # Replace with actual user logic if needed
        question_text=forum_question
    )
    # Store the new forum in the dictionary using the numeric ID
    forums[next_forum_id] = new_forum
    # Increment the ID for the next forum
    next_forum_id += 1

    return new_forum.id

def user_add_reply(forum_id, reply_text, session_token):
    target_forum = None  # Initialize target_forum as None
    #input validation
    if reply_text is None: 
        abort(401, description="Reply Text cannot be empty")
    
    #xxs scripting
    reply_text = html.escape(reply_text)

   # Loop through the forums dictionary to find the matching forum ID
    for fid, forum in forums.items():
        if fid == forum_id:
            target_forum = forum
            break  # Exit the loop once the forum is found

    if not target_forum:
        abort(404, description="Forum not found with invalid forum id")

    # Retrieve the author from the users dictionary using the session token
    author = admin_retrieve_author_name(session_token)

    if not author:
        abort(401, description="Invalid session token")

    # Add the reply to the found forum
    target_forum.add_reply_to_question(author, reply_text)
    for index, reply in enumerate(target_forum.question['replies'], start=1):
                print(f"Reply {index}:")
                print(f"  Author: {reply['author']}")
                print(f"  Time: {reply['time']}")
                print(f"  Text: {reply['text']}")
                print()  # Blank line for readability

    print(f"Reply added to forum ID: {forum_id}")
    return True
