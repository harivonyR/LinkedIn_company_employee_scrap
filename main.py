# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:58:48 2025

@author: BEST

Loop scrap and merge data

"""

import json
import requests
from credential import x_api_key

# API KEY
X_API_KEY = x_api_key          # valid api key from piloterr.com

COMPANY = "Apple Inc."         # Campany name on LinkedIn

PAGE_RANGE = 2                 # number of google search page to scrape
LIMIT = 20                     # limit of result (link) to scrape on each page



def get_search_results(page=1, company=COMPANY, organic_results=True):
    """
    set organic_results=False if a raw response is needed
    
    """
    url = "https://piloterr.com/api/v2/google/search"
    
    payload = {
        "query": f"intext:\'{company}\' inurl:in site:linkedin.com -inurl:posts",
        "page": page,
        "num" : LIMIT
    }
    headers = {
        "x-api-key": X_API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if organic_results:
        return response.json().get('organic_results', [])
    
    else :
        return response.json()
    
def get_profile_info(profile_link):
    url = "https://piloterr.com/api/v2/linkedin/advanced/profile/info"
    
    headers = {
        "x-api-key": X_API_KEY
    }
    querystring = {"query": profile_link}
    
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def save_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def test():
    """
    Pipeline function test (Optional)
    """
    # Get search result
    organic_results = get_search_results(page=2)

    # Get profile links
    profile_list = [r.get("link") for r in organic_results if r.get("link")]

    # Get profile info
    all_profiles = []
    profile_info = get_profile_info(profile_list[2])
    
    all_profiles.append(profile_info)
    # Export
    save_json([profile_info], "output/linkedin_profile_dataset_test.json")

    
def main():
    all_profiles = []

    for i in range(PAGE_RANGE):
        
        print(f"Page : {i+1}")                            
        try:
            results = get_search_results(page=i + 1)

            for result in results:
                
                link = result.get('link')
                print(f"link : {link}")                   
                
                if link:
                    try:
                        profile_data = get_profile_info(link)
                        all_profiles.append(profile_data)
                        
                    except Exception as e:
                        print(f"Error fetching profile info: {e}")
                        
        except Exception as e:
            print(f"Exception during search: {e}")

    save_json(all_profiles, "output/linkedin_profile_dataset.json")
    return all_profiles

# run pipeline
if __name__ == "__main__":
    all_profiles = main()