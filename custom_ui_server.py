###############################################################
#
# @copyright  Bevywise Networks Inc. info@bevywise.com  
# Initial Author - Mahesh Kumar S
#
# The UI custom server will help you customize the UI of the 
# MQTTRoute by adding your own code on the server side. 
# 
# Data Connectors
# SQL connector will be provided as cursor global variable 
# for querying the Database & Elastic Search connector for 
# querying Elastic if you have enabled custom storage option
#
# New URL Addition 
# Add your new functionality using the URL and the corresponding 
# method.  These URLs can be invoked from your User Interface 
# for manipulating data. We support GET http method in 
# this version. 
#
###############################################################

#
# SQL Connector. It will be sqlite / mssql / mysql cursor based 
# on your configuration in db.conf
# Please construct your queries accordingly. 
#
import sys
import json
global db_cursor
#username','client_send_api','topic_name','message',1,0,'10',0


# elasstic_search cursor. 

global elastic_search

import os, sys

#
#Client object. It used to send/publish message to any active clients
#Simply call the function with parameters like User_name,Client_id,Topic_name,Message,QOS,
global Client_obj

# Called on the initial call to set the SQL Connector
def setsqlconnector(conf):

    global db_cursor
    db_cursor=conf["sql"]


# Called on the initial call to set the Elastic Search Connector

def setelasticconnector(conf):
    global elastic_search
    elastic_search=conf["elastic"]

def setclientobj(obj):
    global Client_obj
    Client_obj=obj['Client_obj']



#
# Configure your additional URLs here. 
# The default URLs are currently used for the UI. 
# Please don't remove them, if you are building it over the same UI. 
#

def custom_urls():

    urllist={
        "AUTHENTICATION":'DISABLE',
        "urls":[{"/extend/Dashboard":dashboard}]
    }
    return urllist

# write your url function codes in the following methods
def dashboard():
    return ("dashboard.html")


    
