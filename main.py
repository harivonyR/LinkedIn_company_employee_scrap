# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:42:08 2025

@author: Harivony RATEFIARISON
"""


from credential import x_api_key
import requests

url = "https://piloterr.com/api/v2/google/search"

query = "intext:\"Apple\" site:linkedin.com -inurl:posts/ -inurl:company/ -inurl:video/ -inurl:pulse/ -inurl:pulse/ inurl:in/"
query_test = "linkedIn data analyst"
location = "NY"
gl = "us"
page = 2
num = 10 # maximum number of result to return

payload = {
    "query": query_test,
    #"location": location,
    #"uule": "<string>", # can not be used with location param
    #"gl": gl,
    #"hl": "<string>",
    #"page": page,
    #"num": num
}

headers = {
    "x-api-key": x_api_key,
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
