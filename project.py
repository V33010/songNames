import webbrowser
import re
import requests
from tabulate import tabulate
import sys


def getArtist(): # will get the name of the artist from the user
    key = 0
    while key == 0:
        x = input("Artist Name: ") # gets the name of the artist
        if x != "" and re.search("^[a-zA-Z0-9 ]+$",x):
            key = 1
            pass
        else:
            print("Please input Artist Name")
    x = x.split(" ") # converts the name string to a list based on the spaces in the name
    art = "" # create an empty string (used for making artist name with "+" instead of " ", as required by the URL )
    for i in x:
        art = art + "+" + i
        art = art.strip("+")

    artTrue = "" # create an empty string, used for making sure the output of songs does not contain the actual name of the artist only
    for i in art:
        if i != "+":
            artTrue = artTrue + i
        else:
            artTrue = artTrue + " "
    return art,artTrue

def getNums(): # will give the number of songs the user asks for
    key = 0 # used for being in the while loop 
    while key == 0:
        n = (input("Number of Songs: ")) # gets the number of songs 
        if re.search("^[0-9]$|^1[0-9]$|^2[0-5]$",n):
            key = 1
        else:
            print("Please input an integer (max 25)")

    return int(n)

def main():
    print("")
    print("Please input the artist name and number of songs you want (max 25)")
    # input("presss Enter to continue...")


    art,artTrue = getArtist()
    n = getNums()

    songsDict = getResponse(art,artTrue,n)
    
    print("")
    urlList = []
    songsDictTrans,urlList = dictTransform(songsDict)


    t = printTable(songsDictTrans)
    print(t,end="\n\n")

    
    a = input("Would you like to save results to a text file? (y/n): ") 
    if (a.lower().strip() == "y"):

        save(t)
    elif (a.lower().strip() == "n"):
        print("Results not saved",end="\n\n")
        pass

    askOpen(urlList,n)
    print("")

def printTable(t): # prints the final table of songs
    table = tabulate(t,headers="keys")
    return table

def getResponse(art,artTrue,n): # this function will take the name of the artist, artTrue, and the number of songs and return the response as a dictionary with keys as songs and value as duration
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=100&term={art}")
    r = (response.json())
    # print(json.dumps(r, indent=2))
    songs = []
    durations = [] 
    urls = []
    # for i in r["results"]:
    #     print(i["trackName"])

    for result in r["results"]:
        if (result["trackName"].lower() != artTrue):
            songs.append(result["trackName"])
            durations.append(result["trackTimeMillis"])
            urls.append(result["trackViewUrl"])

    songsNew = {}

    try:
        for i in range(0,n): # this for loop will take care of when the same name of song repeats in the results again and wont get added as a new item to the dictionary
            key = 0
            while key == 0:
                if (songs[i] in songsNew.keys()):
                    i = i + 1
                    continue
                else:
                    songsNew.__setitem__(songs[i],[durations[i],urls[i]])
                    key = 1
    except IndexError:
        print(f"This artist does not have {n} songs")
        pass

    return songsNew

def dictTransform(dict):
    dictKeys = list(dict.keys())
    dictVals = list(dict.values())
    m = len(dictKeys)

    nums = [] # for the serial number of the songs
    for i in range(1,m+1):
        nums.append(i)

    times = []
    for i in range(0,m):
        t = toTime(dictVals[i][0])
        times.append(t)
        pass

    links = []
    for i in range(0,m):
        L = dictVals[i][1]
        links.append(L)

    trans = {}
    trans.__setitem__("No.",nums)
    trans.__setitem__("Songs",dictKeys)
    trans.__setitem__("Duration",times)
    return trans,links

def toTime(n: int) -> str: # for converting the miliseconds to minutes and seconds
    inSec = n/1000

    mins = int(inSec / 60)
    secs = int(inSec % 60)

    return f"{mins}:{secs:02d}"

def save(table):
    k = input("Text file name (without extension): ")
    with open(f"{k}.txt","w") as file:
        file.write(table)
    print("File saved", end="\n\n")

def songOpen(linkList,total:int):
    key = 0
    full = []
    for i in range(1,total+1):
        full.append(i)
    while key == 0:
        try:
            nth = int(input("Which song number would you like to open?: "))
            if re.search("^[0-9]$|^1[0-9]$|^2[0-5]$",str(nth)) and (nth in full):
                webbrowser.open(linkList[nth-1], autoraise=True)  # n-1 because the serial number is different from the index of the link in the list
                key = 1
            else:
                pass
        except ValueError:
            pass    

def askOpen(urlList,totals:int):
    listing = urlList

    j = input("Would you like to open any song in browser? (y/n): ")
    if j.lower().strip() == "y":
        songOpen(listing,totals)
        key = 0
        while key == 0:
                j = input("Would you like to open another song in browser? (y/n): ")
                if j.lower().strip() == "y":
                    songOpen(listing,totals)
                elif j.lower().strip() == "n":
                    key = 1
                    pass
                else:
                    askOpen(urlList,totals)
    elif j.lower().strip() == "n":
        pass
    else:
        askOpen(urlList,totals)
   

if __name__ == "__main__":
    main_key = 0
    while main_key == 0:
        main()
        x = input("Would you like to continue the program? (y/n): ")
        if x.lower().strip() == "y":
            pass    
        elif x.lower().strip() == "n":
            sys.exit("Program exited \n")


