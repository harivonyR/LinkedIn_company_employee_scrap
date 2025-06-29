# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:42:08 2025
@author: Harivony RATEFIARISON

Step-by-step tutorial to extract public LinkedIn profiles from Google search results using Piloterr API.
"""

from credential import x_api_key
import requests

# ---------------------------
# 0 - Google Dork to search for LinkedIn employee profiles
# ---------------------------

# Google Dorks are advanced search operators used to extract precise results from Google's indexed pages.

# Goal: List public LinkedIn profiles related to Apple Inc.

# Example Dork:
# intext:'Apple Inc.' inurl:in site:linkedin.com -inurl:posts

# Syntax breakdown:
# - intext:'Apple Inc.' → pages containing the exact phrase
# - site:linkedin.com   → limits search to LinkedIn domain
# - inurl:in            → targets only LinkedIn profile URLs
# - -inurl:posts        → excludes LinkedIn posts



# ---------------------------
# I - Search LinkedIn profiles using Piloterr Google Search API
# ---------------------------

search_url = "https://piloterr.com/api/v2/google/search"

search_payload = {
    "query": "intext:'Apple Inc.' inurl:in site:linkedin.com -inurl:posts",
    "page": 1
}

search_headers = {
    "x-api-key": x_api_key,
    "Content-Type": "application/json"
}

search_response = requests.post(search_url, json=search_payload, headers=search_headers)
search_data = search_response.json()

print("------------")
print("1) Google search response:")
print(search_data)

# ---------------------------
# II - Extract first profile link
# ---------------------------

organic_results = search_data.get('organic_results', [])


profile_link = organic_results[0].get('link')
print("------------")
print(f"2) Sample profile link: {profile_link}")

# ---------------------------
# III - Get LinkedIn profile details via Piloterr API
# ---------------------------

profile_url = "https://piloterr.com/api/v2/linkedin/advanced/profile/info"

profile_headers = {
    "x-api-key": x_api_key
}

profile_params = {
    "query": profile_link
}

profile_response = requests.get(profile_url, headers=profile_headers, params=profile_params)

print("------------")
print("3) Sample profile info:")
print(profile_response.json())
