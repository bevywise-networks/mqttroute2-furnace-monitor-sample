#!/usr/bin/python2.7

################################################################
# @Bevywise.com IOT Initiative. All rights reserved 
# www.bevywise.com Email - support@bevywise.com
#
# custom_store.py
#
# The custom data store hook for the Big Data Storage. 
# The Custom data hook can be enabled in the broker.conf 
# inside conf/ folder.
# 
# The parameter data will be in dict format and the keys are 'sender','topic', 'message', 'unixtime', 'timestamp'
#
################################################################


#
# SQL Connector. It will be sqlite / mssql / mysql cursor based 
# on your configuration in db.conf
# Please construct your queries accordingly. 
#
global db_cursor

#
# elasstic_search cursor. 
#
global elastic_search
import os, sys

global datasend

#
#Client object. It used to send/publish message to any active clients
#Simply call the function with parameters like User_name,Client_id,Topic_name,Message,QOS,

global Client_obj

sys.path.append(os.getcwd()+'/../extensions')

# Called on the initial call to set the SQL Connector

def setsqlconnector(conf):

    global db_cursor
    db_cursor=conf["sql"]
# Called on the initial call to set the Elastic Search Connector

def setelasticconnector(conf):
    global elastic_search
    elastic_search=conf["elastic"]
def setwebsocketport(conf):
    global web_socket
    web_socket=conf["websocket"]

def setclientobj(obj):
	global Client_obj
	Client_obj=obj['Client_obj']
	#Client_obj('Mahesh','clientno1','test','jsvkvlkdsvbkvcksdhvcksdvcsdkjvcs',1)

# Importing the custom class into the handler

from customimpl import DataReceiver

datasend = DataReceiver()

def handle_Received_Payload(data):

	#
	# Write your code here. Use your connection object to 
	# Send data to your data store

	print "print in the handle_received_payload",data

	result = datasend.receive_data(data)

	# if result is none then write failed
def handle_Sent_Payload(data):

	#
	# Write your code here. Use your connection object to 
	# Send data to your data store

	print "print in the handle_Sent_payload",data

	result = datasend.sent_data(data)
