"""
This __init__.py file allows Python to read your package files
and compile them as a package. It is standard practice to leave 
this empty if your package's modules and subpackages do not share
any code.
(If your package is just a module, then you can put that code here.)
"""

import requests
from bs4 import BeautifulSoup
from replitapi.database import db

class LiteralObject:
  def __init__(self, object_as_dict):
    self.object_as_dict = object_as_dict
    for key in object_as_dict.keys():
      exec(f"self.{key} = object_as_dict['{key}']")
  
  def __repr__(self):
    return str(self.object_as_dict)

  def to_dict(self):
    return self.object_as_dict

def get_user_data(query, mode = "username"):
  if mode == "url":
    doc = requests.get(query)
    if doc.status_code == 404:
      raise LookupError("User was not found!")
  if mode == "username":
    doc = requests.get("https://replit.com/@" + query)
    if doc.status_code == 404:
      raise LookupError("User was not found!")
  soup = BeautifulSoup(doc.text, 'html.parser')
  languages_parent = soup.select(".profile-languages")[0]
  languages_children = languages_parent.findChildren("div" , recursive=False)
  languages = []
  for child in languages_children:
   languages.append(child.findChildren("a", recursive=False)[0].findChildren("span")[0].text )
  cycles = soup.select("[title='cycles']")[0].text
  cycles = cycles.replace("(", "")
  cycles = cycles.replace(")", "")
  profile_picture = soup.find("span", { "class": "profile-icon"})["style"]
  import re
  urls = re.findall('url\((.*?)\)', profile_picture)
  img = urls[0].replace('"', '')
  return LiteralObject({
    "favourite_langauges": languages,
    "cycles": int(cycles),
    "profile_picture": img
  })

def get_repl_data(query, user: str = "", mode = "name"):
  if mode == "url":
    doc = requests.get(query)
    if doc.status_code == 404:
      raise LookupError("Repl was not found!")
  if mode == "name":
    doc = requests.get("https://replit.com/@" + user + "/" + query + "?v=1")
    if doc.status_code == 404:
      raise LookupError("Repl was not found!")
    if user == "":
      raise TypeError("Missing required argument for name query 'user'")
  soup = BeautifulSoup(doc.text, 'html.parser')
  forks = soup.select(".count-button")[0].findChildren()[0].text
  return LiteralObject({
    "description": soup.select(".text")[0].text,
    "forks": forks
  })