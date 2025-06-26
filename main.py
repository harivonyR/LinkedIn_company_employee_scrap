# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:42:08 2025

@author: Harivony RATEFIARISON
"""

# LOAD API KEY

from credential import x_api_key

#
#
# 0 - BUILD DORK (syntax)
#
# 

# Dork : "intext:\'Apple Inc.\' inurl:in site:linkedin.com -inurl:posts"

# intext:\'Apple Inc.\' 
#site:linkedin.com 
# inurl:in 
#-inurl:posts"


#
#
# I - Get company employee linkedIn profil link List 
#
# 

import requests

url = "https://piloterr.com/api/v2/google/search"


payload = {
    "query": "intext:\'Apple Inc.\' inurl:in site:linkedin.com -inurl:posts",
    "page" : 1
}

headers = {
    "x-api-key": x_api_key,
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print("------------")
print(f"1) google search response : {response.text}")


#
#
# II - Get profil info 
#
# 

# 1 - get link

# Local json load / server temporary anavalaible
import json
with open("input/google_search_api_response.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    
#data = response.json()
result_organic = data['organic_results']       # result_organic is the search result key that contain profile link list
profil_link = result_organic[0]['link']        # sample profile link

print("------------")
print(f"2) sample profile link : {profil_link}")


# 2 - fetch profile info using API


#
#
# III - Get profil info 
#
# 

import requests

url = "https://piloterr.com/api/v2/linkedin/advanced/profile/info"

headers = {
    "x-api-key": x_api_key
}

querystring = {"query" : profil_link} 

response = requests.request("GET", url, headers=headers, params=querystring)

print(f"3) sample profile link : {response.json()}")

#
#
# IV - LOOP process - merge data
#
# 









