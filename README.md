# Webscrapping
Webscrapping using Python and Xpath

Python script to scrap the webpage http://www.infoplease.com/t/hist/state-of-the-union/ to create a table in a SQL server from the contents in the webpage.
The webpage comprises of multiple links consisting of 200 HTML pages, need to scrap the Name of the president, Date, Link to address and Speech and get these data stored in SQL server.
Python script consists the code to scrap these data into a CSV file and then the file had been imported into SQL server using SQL Import wizard. 

Download the combine.py into your system:
Then make these two changes:
1. Identify this line in the code, location = 'C:\\Users\\Sri Vishnu theja\\Parse\\'+temp+'.txt' # use your local address if you choose to run
2. Identify this line in the code, filepath = 'C:\\Users\\Sri Vishnu theja\\Parse\\file.txt' # use your local address if you choose to run

To run the script in cmd prompt : py  combine.py

Once you run the script, you will be able to see 220 files comprising the speech of each president over the year, a CSV file by name 'Data' comprising the list of presidents with Name of the president, Date, link to the page, Speech as a link to text file(220 files)over the year and a text file by name 'file' consisting of all the presidents with their date and their speech over the year. 
