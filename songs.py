import sys
import requests

x = input("Please enter the artist name: ")
name = x
x = x.strip()
x = x.split(" ")
a = ""
for i in range(0,len(x)):
    a = a+x[i]

# print(a)
y = input("Please input the number of songs: ")
b = int(y) # number of songs

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=100&term={a}")
o = response.json()

og = []

for result in o["results"]:
    og.append(result["trackName"])
# print(og)

for i in range(0,len(og)):
    for j in range(i + 1, len(og)):
        try:
            if(og[i] == og[j]):
                og[j] = 0
        except ValueError:
            continue
# print(og)
c = len(og)

if(b>c):
    print(f"{name} has fewer than {b} songs")
    for i in range(0,c):
        if(og[i] != 0):
            print(og[i])
        else:
            continue

else:
    i = 0
    term = b
    while(term>0):
        if(og[i] != 0):
            print(og[i])
            i += 1
            term -= 1
        else:
            i += 1
            continue    