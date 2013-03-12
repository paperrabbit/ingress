# -*- coding: utf-8 -*-
#Author: rayman.mobile@gmail.com
#Create:2013-03-09
#Last:2013-03-09
#
#ingress intel api 

#import urllib
#import urllib2
#import re
import json
import requests
import config


class  Intel:

	def __init__(self):
		self.mapid=config.mapid		

		
	def request(self,url,params={},method="POST"):
		headers={
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding':'gzip,deflate,sdch',
		'Accept-Language':'en-US,en;q=0.8',
		'Content-Length':'231',
		'Content-Type':'application/json; charset=UTF-8',
		'Host':'www.ingress.com',
		'Origin':'https://www.ingress.com',
		'Proxy-Connection':'keep-alive',
		'Referer':'https://www.ingress.com/intel',
		'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17',
		'X-Requested-With':'XMLHttpRequest',
		'X-CSRFToken':config.csrftoken,
		'Cookie':config.cookie,
		}
		payload=json.dumps(params)
		request=requests.post(url,data=payload,headers=headers,verify=False)
		return request.text

	
	def fetchMap(self):
		url='https://www.ingress.com/rpc/dashboard.getThinnedEntitiesV2'
		payload={
		"minLevelOfDetail":0,
		"boundsParamsList":[{"id":config.mapid,
				"minLatE6":config.minLat,
				"minLngE6":config.minLng,
				"maxLatE6":config.maxLat,
				"maxLngE6":config.maxLng,
				"qk":config.mapid}],
		"method":"dashboard.getThinnedEntitiesV2"
		}
		return json.loads(self.request(url,params=payload,method="POST")) 
	
	
	def fetchCOMM(self):
		url='https://www.ingress.com/rpc/dashboard.getPaginatedPlextsV2'
		payload={
		"desiredNumItems":50,
		"minLatE6":config.minLat,
		"minLngE6":config.minLng,
		"maxLatE6":config.maxLat,
		"maxLngE6":config.maxLng,
		"minTimestampMs":-1,
		"maxTimestampMs":-1,
		"method":"dashboard.getPaginatedPlextsV2"
		}
		return json.loads(self.request(url,params=payload,method="POST")) 


	def fetchPlayer(self,pid):
		url='http://www.ingress.com/rpc/dashboard.getPlayersByGuids'
		payload={"guids":["%s"%pid],"method":"dashboard.getPlayersByGuids"}
		return json.loads(self.request(url,params=payload,method="POST")) 


	def sendMsg(self,msg):
		lat=(config.minLat+config.maxLat)/2
		lng=(config.minLng+config.maxLng)/2
		url='https://www.ingress.com/rpc/dashboard.sendPlext'
		payload={"message":msg,"latE6":lat,"lngE6":lng,"method":"dashboard.sendPlext"}
		return json.loads(self.request(url,params=payload,method="POST"))


	def getReward(self,passcode):
		url='https://www.ingress.com/rpc/dashboard.redeemReward'
		payload={"passcode":passcode,"method":"dashboard.redeemReward"}
		return json.loads(self.request(url,params=payload,method="POST"))
	


	
			
		
