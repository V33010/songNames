# ARTIST'S SONGS RECOMMENDATION APP
#### Video Demo:  <URL HERE>
#### Description:

In this **python** app, I have developed upon the ideas taught in the **APIs, requests, JSON** Chapter of the [Week 4: Libraries](https://cs50.harvard.edu/python/2022//weeks/4/).

Simply put, the app I have made, puts out song recommendations from iTunes for an artist that the user inputs.

I have implemented the following in the project:
- `for` and `while` loops
- handled exceptions
- used multiple libraries
- provided unit tests
- used `regex` for ensuring correct user input

## Motivation
I chose to do this project to **showcase my learning** from the course. I have tried to implement as much as I could from the course, to ensure all the concepts taught are used.
This project can be used by people wishing to get different song recommendations from new artists they wish to explore.

## Features
#
-  Allows users to **save** the results as a `.txt` file
- Allows the user to open song URLs directly in the browser
- User can run the progam over from the beginning without having to restart it


<br>
<br>

## FUNCTIONS USED
#
`getArtist()`
 

This function will get the name of the artist from the user as a `str`. I have implemented a **while loop** to ensure that the input cannot stay empty. Also, further implementation of **regex** is used to check the user inputs only alphanumeric charachters.

The function then splits the input at space charachters and replaces the spaces with `"+"`, as required by the iTunes API.
(Example: `"alan walker"` gets converted to `"alan+walker"`) This string is saved in variable `art`.

`artTrue` is another `str` variable which contains the name of the artist as input by the user.
The function then returns `art` and `artTrue`.


<br>

`getNums()`

This function gets the number of songs that the user wants to get recommended. A **while** loop is implemented to ensure the input does not remain empty. **regex** is implemented to ensure that the number the user inputs is an `int` in the **range 0 to 25**.

The function returns the number of songs requested as an `int`.

<br>

`printTable(t)`

This function takes an argument of a `dict`. It uses [tabulate](https://pypi.org/project/tabulate/) to convert the `dict` to a table, with the headers as the keys of the `dict`.

This table is stored in variable `table`. The function returns `table`.

<br>

`getResponse(art,artTrue,n)`

This function takes the arguments:
- `art`: Name of the artist with `"+"` instead of `" "`.
- `artTrue`: Name of the artist as provided by the user.
- `n`: The number of songs the user requests.

The function then sends a request to iTunes using `requests.get()`. The response is stored in `response` variable.
JSON formatting of the response is stored in variable `r`, which is a dict.

The list of **songs** in the results is stored in `songs`, **durations** of songs are stored in `durations`, and the **URLs** of the songs are stored in `urls`.

The value of `artTrue` is used to ensure the song which gets added to the `songs` list does not contain the name of the artist as it is.

The request made to the iTunes API is always for **100 songs**. Of these, `n` songs are appended to the `songsNew` dict.

It can happen that the song gets repeated in the responses, due to which the dict will have lesser entries than what is requested by the user. To prevent this, a `for` loop is used, which ensures that songs which are repeated aren't counted more than once while appending to the `songsNew` dict.

It can also happen that the artist does not have `n` songs available. This will raise an `IndexError` in the function. In that case, all the songs the artist has available are listed.

This function returns the `dict` variable `songsNew`.

<br>

`dictTransform(dict)`

This function is used for converting the `songsNew` dict to a more usable format for making tables.

- `nums` is a list containing the numbers from `0` to `n` (total songs requested by user) as a list.

- `times` is a list which contains the duration of each song in "m:ss" format using the `toTime()` function.

- `links` is a list which contains the URLs of each of the songs.

The above three lists are stored in a dict `trans` with the corresponding keys.

This function returns (`trans`,`links`) as a tuple.

An example of this function will help for better understanding:
```py
initialDict = {"song_1":[60000,"URL_1"],"song_2":[120000,"URL_2"]}

dictTransform(initialDict) == ({"No.":[1,2],"Songs":["song_1","song_2"],"Durations":["1:00","2:00"]},["URL_1","URL_2"])
```

<br>

`toTime(n: int)`

This function takes an `int` as argument. This `int` is treated as time in miliseconds. The use of this function is to convert this time from miliseconds to **"minutes:seconds" (m:ss)** format.

It returns the time ("m:ss") as a `str`.

<br>

`save(table)`

This function takes in `table` as an argument and saves it as a **text** file.
`table` is the table as returned in the `printTable(t)` function.
The name of the file is provided by the user as input.

<br>

`songOpen(linkList,total:int)`

This function takes in arguments `linkList`, which is a list of the URLs of the songs, and `total:int`, which is the total number of songs the user asked for.

The purpose of this function is to **open the URL of the song** as requested by the user. It asks the user for the song-number which they want to open, and opens the song corresponding to it in a browser.

`regex` is used to ensure the number input by the user is an `int` in the range 1 to 25. `total` is used to ensure the number the user inputs is in the range of number of songs which was provided earlier.

This is nested in a `while` loop to allow the user to make mistakes without breaking the program.


<br>

`askOpen(urlList,totals:int)`

This function takes in arguments `urlList` and `totals:int`
It function is the upper level function for `songOpen(linkList,total:int)`. 

This function is used to ask the user if they want to open the URL of any song in the browser or not. If they do, `songOpen(linkList,total:int)` is called, otherwise the program moves forward. This function is also nested in a `while` loop to allow the user to make errors without breaking the program.


<br>

`main()`

`main()` calls all the other functions in the correct order. 

- get the name of the artist (`getArtist()`) and the number of songs (`getSongs()`) from the user.
-  get the responses from iTunes (`getResponse(art,artTrue,n)`)

- transform the response dict to a more usable format using `dictTransform(songDict)`
- print the table of the song responses for the user
- ask if user wants to save the results as a text file 
    - if yes, ask the user for name of the file, and save it (`save(table)`)
    - if no, contiue

- ask the user if they want to open the URL of any song from the results (`askOpen(urlList,totals:int)`)
    - if yes, open URL (`songOpen(linkList,total:int)`)
    - if no, contiue
- ask the user if they want to continue the program (run the program again)
    - if yes, restart the program 
    - if no, exit the program with `sys.exit()` and an exit message

<br>

## Additional Information
#
I chose to use `dict` at a lot of places in the program because it eliminates the problem of multiple entries.

I have tried to have every task in the program as a separate function, which returns a value, so that it is more easily testable.

The unit tests provided cover 5 of the most important functions of the program. Testing of functions which required user input was done using the mock library to simulate inputs. The method used for doing this was taken from [this](https://stackoverflow.com/a/55033710) stackoverflow answer.

The program always asks for 100 song requests of each artist to the iTunes API. Instead of this I could have chosen to request for as many songs as the user requests, but that would run into problems such as repetition of songs, requiring to make another request to the API, thus reducing the efficiency. 

<br>

# Credits

- I would like to thank [CS50P](https://cs50.harvard.edu/python/2022//) for the amazing course and giving me the opportunity to make this project
- How to make a proper README <br> https://www.mygreatlearning.com/blog/readme-file/
- Simulating inputs in unit testing <br>https://stackoverflow.com/a/55033710
- iTunes API documentation <br>https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/index.html <br>
I would like to thank iTunes for the Public API, which was the backbone and highlight of this project.
- Opening a URL from python <br> https://stackoverflow.com/a/4302041


