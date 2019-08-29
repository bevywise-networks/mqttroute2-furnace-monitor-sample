# Furnace Monitoring Application over MQTTRoute

This is an outcome of a hackathon of building an IoT Application in a day.  One of the developers built an applicaton for the Furnace temperature monitoring using the MQTTRoute.

# About MQTTRoute 

[MQTTRoute](https://bevywise.com/mqtt-broker/) is an IoT Application development platform that has an inbuilt MQTT Broker and extensions of User Interface & embedding your AI & ML alogrithms. The Broker can be run on windows, linux & Mac and available for a [free download](https://bevywise.com/mqtt-broker/download.html).

### How to set up the system. 
* Download and install MQTTRoute form the [Download page](https://bevywise.com/mqtt-broker/download.html)
* Clone this repository or download the files as zip. 
* move *dashborad.html* to   */Bevywise/Mqttroute/ui*
* move *custom_ui_server.py, custom_scheduler.py, cutom_store.py* to */Bevywise//Mqttroute/extension*
* start the broker now.
* Go to browser and load [http://localhost:8080/extend/Dashboard](http://localhost:8080/extend/Dashboard) to the see the new Dashboard.
* You have to publish the temperature data to **/furnace/temperature** a random number for the dashboards to show the data.
