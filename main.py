import json
import requests
import datetime
import server
import mysql.connector
from mysql.connector import MySQLConnection, Error


TOKEN = "913721237:AAEuGNRDAnDfiwT74qoknJ3qCGHjbTmHrV0"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_chat_id(updates,i):
    num_updates = len(updates["result"])
    chat_id = updates["result"][i]["message"]["chat"]["id"]
    return (chat_id)

def no_subscribers(updates):
    num_subs = len(updates["result"])
    return(num_subs)

def send_message(tt,chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(tt, chat_id)
    get_url(url)

if __name__ == '__main__':

    final_data=[]
    user_ids=[]

    now = datetime.datetime.now()
    day=now.strftime("%A")

    # ask which class

    # ask whether counsellor or subject teacher

    #if entity == "counsellor":
    	# get all counsellors and iterate in the list of counsellors and call schedule(counsellor_name)

    #else if entity == "subject":
    	# ask which subject

    	# list all subject teachers

    	# ask which subject teaacher (int)

    	# call schedule(teacher_name)

    for i in range(no_subscribers(get_updates())):
        user_ids.append(get_chat_id(get_updates(),i))

    for i in range(no_subscribers(get_updates())):
        for j in range(len(final_data)):
            tt=final_data[j][0]
            chat = user_ids[i]
            send_message(tt, chat)
