#!/usr/bin/env python
# coding: utf-8

# In[195]:


from dotenv import load_dotenv
load_dotenv()

import os

DARKSKY_API_KEY = os.getenv("DARKSKY_API_KEY")


# In[196]:


import requests
api_key = DARKSKY_API_KEY


# In[197]:


response = requests.get(f'https://api.darksky.net/forecast/{api_key}/40.7128,-74.0060')
data = response.json()


# In[198]:


import datetime
right_now = datetime.datetime.now()

date_string = right_now.strftime("%I %p weather forecast: %B %d, %Y")
text = (f"Right now it is {data['currently']['temperature']} degrees out and {data['currently']['summary']}. Today will feel like {data['hourly']['data'][0]['apparentTemperature']} degrees with a high of {data['daily']['data'][0]['temperatureHigh']} and a low of {data['daily']['data'][0]['temperatureLow']}. There is a {data['daily']['data'][0]['precipProbability']*100}% chance of rain.")


# In[199]:


import requests 

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox30eb7daf1bf14cbca4105a0ba0e2e7f5.mailgun.org/messages",
        auth=("api", "{secret_API}"),
        data={"from": "Excited User <mailgun@sandbox30eb7daf1bf14cbca4105a0ba0e2e7f5.mailgun.org>",
            "to": ["amy.okruk@gmail.com"],
            "subject": date_string,
            "text": text})

send_simple_message()


# In[189]:





# In[ ]:





# In[ ]:




