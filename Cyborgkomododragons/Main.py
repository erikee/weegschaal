# -*- coding: utf-8 -*-

import urllib2
import json


team_id="CyborgKomodoDragons"
team_pw="9b5a321ca3f7575f1328d2ad4f02a96b"

run_id="1"
index="3"

user_info = urllib2.urlopen("http://krabspin.uci.ru.nl/getcontext.json/?i="+index+"&runid="+run_id+"&teamid="+team_id+"&teampw="+team_pw)
data = json.load(user_info)
print data

suggested_response = {"header": "5", "adtype": "skyscraper","color":"black","productid":"10","price":"20.00"}

bought_item = urllib2.urlopen("http://krabspin.uci.ru.nl/proposePage.json/?i="+index
                              +"&runid="+run_id
                              +"&header="+suggested_response["header"]
                              +"&adtype="+suggested_response["adtype"]
                              +"&color="+suggested_response["color"]
                              +"&productid="+suggested_response["productid"]
                              +"&price="+suggested_response["price"]
                              +"&teamid="+team_id
                              +"&teampw="+team_pw)
response = json.load(bought_item)
print response