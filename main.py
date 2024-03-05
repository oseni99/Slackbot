import os
from dotenv import load_dotenv
import slack
from pathlib import Path
from flask import Flask 
from slackeventsapi import SlackEventAdapter  #handle all the events in the slack 

load_dotenv() # activate the .env environment 
envpath = os.getenv("SLACK_TOKEN")

app = Flask(__name__)  # configure the flask app
slack_events_adapter = SlackEventAdapter(os.getenv("SIGNING_SECRET"),'/slack/events',app) #add the slackevents adapter and it allows us handle the events sent to us from the slack API 

client = slack.WebClient(envpath)  # this will load the slack wiith the api key 

client.chat_postMessage(channel="C06L783U751", text='Testing!')  # this is to ssend a message to the slack channel 



if __name__ == "__main__":
    app.run(debug=True,port=5000)
