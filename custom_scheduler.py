###############################################################
#
# @copyright  Bevywise Networks Inc. info@bevywise.com  
# Initial Author - Mahesh Kumar S
#
# The  Custom Sheduler will help you create  your own schedule in
# MQTTRoute by adding your own code on the server side. 
# 
# Data Connectors
# SQL connector will be provided as cursor global variable 
# for querying the Database & Elastic Search connector for 
# querying Elastic if you have enabled custom storage option
#

###############################################################
from datetime import datetime
import time
import json

def schedule_conf():

# ENABLE/DISABLE YOUR SCHEDULE 
#Add your schedule time in MINUTES in 'OnceIn'
#Add your method to call on schedule in 'methodtocall'
	
	schedules={}

	schedules={
	'STATUS':'ENABLE',
	'SCHEDULES':[
	{'OnceIn':1,'methodtocall':oneminschedule},
	{'OnceIn':1,'methodtocall':fiveminschedule}]}
	
	return schedules

#
# SQL Connector. It will be sqlite / mssql / mysql cursor based 
# on your configuration in db.conf
# Please construct your queries accordingly. 
global db_cursor

#
#Client object. It used to send/publish message to any active clients
#Simply call the function with parameters like User_name,Client_id,Topic_name,Message,QOS,
global Client_obj

#
# elasstic_search cursor. 
#
global elastic_search
# Called on the initial call to set the SQL Connector

global web_socket
# Web_socket 
def setsqlconnector(conf):
    global db_cursor
    db_cursor=conf["sql"]

def setelasticconnector(conf):
    global elastic_search
    elastic_search=conf["elastic"]

def setwebsocketport(conf):
    global web_socket
    web_socket=conf["websocket"]

def setclientobj(obj):
	global Client_obj
	Client_obj=obj['Client_obj']

def oneminschedule():
	now = datetime.now()
	lt = time.mktime(now.timetuple())
	t=5*60*1000

	gt=(lt-t)
	query={"query":{"bool":{"must":[{"range":{"unixtime":{"gt":gt,"lt":lt}}}],"must_not":[],"should":[]}},"from": 0,"size": 10000,}
	available = elastic_search.search(index='mqtt',doc_type="sent_payload",body=query)
	avg_value=[]
	for i in range(available['hits']['total']):
		data= json.loads(available['hits']['hits'][i]['_source']['message'])
		avg_value.append(data[0]['msg']['message'][0])
	avg=((sum(avg_value)/len(avg_value)))
	now=datetime.now()
	lt = time.mktime(now.timetuple())
	cur_time=str(now.hour) + ":" + str(now.minute)
	data={
	"avg":"avg",
	"value":avg,
	"time":cur_time,
	"unixtime":lt
	}
	tc1=elastic_search.index(index="history", doc_type="payload", body=data, refresh=True)
	query1={"sort":[{"unixtime":"desc"}],"query":{"bool":{"must":[{"match_all":{}}],"must_not":[],"should":[]}},"from":0,"size":10000}
	avg_value_ui=available = elastic_search.search(index='history',doc_type="payload",body=query1)
	list1=[]
	bar_graph_data={}
	for i in range(avg_value_ui['hits']['total']):
		data12=json.dumps(avg_value_ui['hits']['hits'][i]['_source'])
		send_ui= json.loads(data12)
		list1.append({
		"avg":send_ui['avg'],
		"value":send_ui['value'],
		"time1":send_ui['time'],
		"timestamp": lt
		})
	bar_graph_data={
	"data":"bar",
	"value":list1

	}
	web_socket.send_message_to_all(json.dumps(bar_graph_data))

def fiveminschedule():
	now = datetime.now()
	lt = time.mktime(now.timetuple())
	t=10*60*1000
	gt=(lt-t)
	query={"query":{"bool":{"must":[{"range":{"unixtime":{"gt":gt,"lt":lt}}}],"must_not":[],"should":[]}},"from": 0,"size": 10000,}
	available = elastic_search.search(index='mqtt',doc_type="sent_payload",body=query)
	avg_value=[]
	for i in range(available['hits']['total']):
		data= json.loads(available['hits']['hits'][i]['_source']['message'])
		avg_value.append(data[0]['msg']['message'][0])
	avg=((sum(avg_value)/len(avg_value)))
	alert={}
	alert={
	"data":"alert",
	"value":avg
	}
	web_socket.send_message_to_all(json.dumps(alert))
