# README for Data Structures
## Description of Data Structures
---
**Graph**
Ideally, the graph for this project would be constructed with data from the Google Books and ORCiD API's. The graph would be weighted, and each title would 
serve as a node while the authors would serve as the edges. The more books that had been written by the same academics, the higher weight between them. 
The responses from the graph would be sorted from highest weight to lowest weight, which would effectively provide the user with results from most relevant 
to least relevant. Dissapointingly, I did not make it to this part of the project, but my concept for this graph is described below:

A user would search a book title, such as "History without a Subject," and this title would serve as a starting point. The starting point would begin a 
breadth first search to return the set of first related neighbors to the starting point node and return it in a numbered list. The numbers
would be associated with the history_books.json attribute "infoLink," which connects to the Google Books web browser record for that book. The user has the
option to exit the request cycle at that point, search for another title, or input the number of the response that they want more information on. If the user
searches for a number, the makeRequest() function would take the user to the web browser Google Books record for the selected book. For the given starting
point example, the web browser page would be this: https://www.google.com/books/edition/History_Without_A_Subject/eXNgDwAAQBAJ?hl=en 