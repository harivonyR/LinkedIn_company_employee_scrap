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

print("------------")
print(f"3) sample profile info : {response.json()}")

#
#
# IV - LOOP process - merge data (this must be mooved into an entire .py file )
#
# 

# import package
import requests
from credential import x_api_key

# create global variable
X_API_KEY = x_api_key
PAGE_RANGE = 2                      # define the number of google search page to scrap
COMPANY = "Apple Inc."

# define function
def get_search_result(page=1, company= COMPANY):
    
    url = "https://piloterr.com/api/v2/google/search"

    payload = {
        "query": f"intext:\'{COMPANY}\' inurl:in site:linkedin.com -inurl:posts",
        "page" : page
    }

    headers = {
        "x-api-key": X_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()
    result_organic = data['organic_results'] 
    
    return result_organic

def get_profile_info(profile_link):
    url = "https://piloterr.com/api/v2/linkedin/advanced/profile/info"

    headers = {
        "x-api-key": X_API_KEY
    }

    querystring = {"query" : profile_link} 

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

# iterrate google search page
def main():
    
    profile_info = []
    
    for i in range(PAGE_RANGE) :
        
        profile_info_dataset = {}
        
        try :
            result_organic = get_search_result(page=i,company= COMPANY)
        except :
            print("exception on search !")
        
        if result_organic != None :
            for j in range(len(result_organic)) :
                try :
                    profile_data = get_profile_info(page=i,company= COMPANY)
                    profile_info_dataset.append(profile_data)
                except e :
                    print(f"error : {e}")
        else :
            print(f"page {}")
    
    profile_info.save("output/linkedin_dataset.json")






