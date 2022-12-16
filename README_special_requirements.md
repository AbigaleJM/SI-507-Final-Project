# README for SI 507 Final Assignment
## Special Instructions and Required Packages

**Overview**
---
This code is for the SI 507 Final Project at the University of Michigan.
It was meant to construct a weighted graph of history books from the Google Books API,
connected by academics with ORCiD profiles. Although I ran out of time to fully complete
this project, the concepts behind the project are outlined in further README.md files 

**Special Instructions**
---
The code in its current state does not run as intended. Use function calls and print statements
to obtain some output.
Script.py contains the main code for the program.
ORCiD.py contains the XML exploration and parsing of the ORCiD Public Data Files.
history_books.json is the JSON file of Google history books metadata.

**Required Packages**
---
* xml.etree.ElementTree as ET: https://docs.python.org/3/library/xml.etree.elementtree.html 
* webbrowser: https://docs.python.org/3/library/webbrowser.html 
* API Key for Google Books is also required: https://developers.google.com/books/docs/v1/using
* ORCiD Public Data FIle 2022 XML Works Download: https://orcid.figshare.com/articles/dataset/ORCID_Public_Data_File_2022/21220892
