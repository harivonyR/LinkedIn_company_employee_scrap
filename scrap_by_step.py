# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 20:42:08 2025

@author: Harivony RATEFIARISON

"""

# Load API KEY
from credential import x_api_key

# ---------------------------
#
# 0 - Get company employee LinkedIn profile links
#
# ---------------------------


# Google dork are used to performe precise search in the google referenced page database.
# It takes advantages of the Google supercalculation power.
# Dork sample :
#   "intext:'Apple Inc.' inurl:in site:linkedin.com -inurl:posts"

# Dork syntax explained :
# intext:'Apple Inc.'   → find page that contain exactly 'Apple Inc.'
# site:linkedin.com     → limit the search in LinkedIn domain only
# inurl:in              → Profile link must contain '/in/' (avoid link that is not a link)
# -inurl:posts          → Exclude of the search all LinkedIn posts link 

# Result : Get list of Apple Inc. result only on LinkedIn


# ---------------------------
#
# I - Get company employee LinkedIn profile links
#
# ---------------------------

import requests

url = "https://piloterr.com/api/v2/google/search"  # API de recherche Google de Piloterr

# Requête à envoyer à l'API
payload = {
    "query": "intext:'Apple Inc.' inurl:in site:linkedin.com -inurl:posts",
    "page": 1  # Page 1 des résultats Google
}

headers = {
    "x-api-key": x_api_key,
    "Content-Type": "application/json"
}

# Envoi de la requête POST à l'API
response = requests.request("POST", url, json=payload, headers=headers)

# Affichage brut de la réponse JSON
print("------------")
print(f"1) google search response : {response.text}")


# ---------------------------
#
# II - Extraire un lien de profil
#
# ---------------------------
"""
# local load
import json

# Chargement d’un fichier local pour test hors ligne
with open("input/google_search_api_response.json", "r", encoding="utf-8") as f:
    data = json.load(f)
"""

data = response.json()
# Récupération des résultats organiques de la recherche
result_organic = data['organic_results']

# Récupération d’un lien de profil (ex: https://www.linkedin.com/in/...)
profil_link = result_organic[0]['link']

print("------------")
print(f"2) sample profile link : {profil_link}")


# ---------------------------
#
# III - Récupérer les infos du profil LinkedIn
#
# ---------------------------

# Requête vers l’API Piloterr pour obtenir les détails du profil
url = "https://piloterr.com/api/v2/linkedin/advanced/profile/info"

headers = {
    "x-api-key": x_api_key
}

querystring = {"query": profil_link}  # Le lien du profil comme paramètre

# Envoi de la requête GET
response = requests.request("GET", url, headers=headers, params=querystring)

# Affichage des informations détaillées du profil
print("------------")
print(f"3) sample profile info : {response.json()}")
