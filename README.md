# Programming Task 2

Welcome to your first programming task 
  - You have to clone this repo to your account, you should be seeing this on your account, if someone elses name is listed call an instructor for help.
  - Use the Ubuntu VM to write the progrm.
  - Use git add, commit and push to send the code back. 
  - Don't forget to add user name and email on git. 
  - You are allowed to use any form of searching and documentation reading and book reading is promoted
  - You cannot talk to your other people or ask for help!

# Halifax Open Data

You are given a csv file from [Halifax's open data](https://www.halifax.ca/home/open-data). 

  - The file is a csv (comma seperated values); i.e, it's like a excel spreadsheet but simple
  - You can read the file without modification to it.
  - You are asked to extract some information from it. 

### Crime count

The CSV you are given has details of the location and type of crime that has happened in halifax in the last 7 days. You are to list the total unique types of crimes that occured and the total number of them as user friendly as possible, also, list the crime ID to the type of crime.

This is the origianl source  -> https://www.arcgis.com/home/item.html?id=f6921c5b12e64d17b5cd173cafb23677

A list like this will be good: 

| Crime Type  | Crime ID  | Crime Count |
| ------ | ------ |------ |
| Assault | 1430 |10 |
| Robbery | 2142 |17 |

### Hints
This url has the meta data: https://services2.arcgis.com/11XBiaBYA9Ep0yNJ/arcgis/rest/services/Crime/FeatureServer/0
In the fields section notice RUCR_EXT_D that has the detilas of the crime. Where is this in your file?
Also, RUCR

### Development

Use with open to open file:
```py
with open(file, 'r') as myfile
```
Use string functions to seperate the values and extract the interesting value to a data structure of your choice!

### Bonus

Can you list the crimes according to the dates? Can you order them by most recent crime first and display it? (Write this as seperate code files)

License
----

MIT
https://www.halifax.ca/home/open-data/open-data-license


**Final Time for submission is Thusday midnight**


