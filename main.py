#!/usr/bin/python3

import requests
import sys
import os

nameSet = False
choiceTaken = False
baseUrl = "https://api.github.com"
standardUsername = "rhettvankorlaar"
apiUrl = ""
name = ""

if len(sys.argv) == 2:
    name = sys.argv[1]
    nameSet = True

print("Keuzemenu:")
print("1) Gebruiker repositories")
print("2) Organisatie repositories")

while not choiceTaken:
    choice = int(input())
    if choice == 1:
        if not nameSet:
            name = input("Wat is je gebruikersnaam?")
            if len(name) == 0:
                name
        apiUrl = baseUrl + "/users/" + name + "/repos"
        choiceTaken = True
    elif choice == 2:
        name = input("Welke organisatie wil je gebruiken?")
        apiUrl = baseUrl + "/orgs/" + name + "/repos"
        choiceTaken = True
    else:
        print("Ongeldige keuze. Probeer opnieuw!")

token = input("Wat is je github token?")
headers = {
    'Accept': 'application/vnd.github.inertia-preview+json',
    'Authorization': 'token ' + token
}

r = requests.get(apiUrl, headers=headers)

allRepoObjects = r.json()

path = input("Welke directory wil je gebruiken?")

os.system("cd " + path)
for repo in allRepoObjects:
    os.system("git clone " + repo["ssh_url"])
