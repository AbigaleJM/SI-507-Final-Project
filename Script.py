from requests_oauthlib import OAuth2
import json
import requests
from GoogleBooks import APIKey
#from ORCiD import orcid_works
from operator import itemgetter
import xml.etree.ElementTree as ET
import webbrowser

booksurl = 'https://www.googleapis.com/books/v1/volumes?'

param_dict = {'q': 'history+subject', 'printType': 'books', 'orderBy': 'relevance', 'maxResults': 40, 'key': APIKey}
response = requests.get(booksurl, param_dict)
historyBooksJson = json.loads(response.text)
#print(historyBooksJson)
historyBooks = historyBooksJson['items']
#print(historyBooks)

# token = ""
# loops = 0

# q_term='history+subject'
# GOOGLE_API_KEY=APIKey
# url="https://www.googleapis.com/plus/v1/volumes?query="+q_term+"&key="+GOOGLE_API_KEY+"&maxResults=50&pageToken="+token
# url=url.replace(" ", "%20")

# while loops < 10:
#     api_response = urllib2.urlopen(url).read()
#     response = requests.get(booksurl, param_dict)
#     # print(response.text)
#     # historyBooksJson = json.loads(response.text)
#     json_response = json.loads(api_response)
#     token = json_response['nextPageToken']
#     if len(json_response['items']) == 0:
#         break
#     for result in json_response['items']:
#         name = result['displayName']
#         print(name)
#         image = result['image']['url'].split('?')[0]
#     # f = open(name+'.jpg','wb+')
#     # f.write(urllib2.urlopen(image).read())
#     loops+=1

# print(len(json_response))
# Why is this only returning ten things when it says there are 4,000 results

def get_nodes(json):
    '''
    Accesses stored metadata of history books pulled from the Google Books API and returns 
    a dictionary with the book title and author(s) as a key-value pair
    Parameters:
        json(JSON): Book metadata stored in a JSON file
    Returns:
        book_titles(dict): Dictionary containing title and authors as {title: authors}
    '''
    book_titles = {}
    for book in json:
        if 'subtitle' in book['volumeInfo'].keys() and 'authors' in book['volumeInfo'].keys():
            title = book['volumeInfo']['title'] + ': ' + book['volumeInfo']['subtitle']
            authors = book['volumeInfo']['authors']
            book_titles = {title: authors}
        else:
            try:
                title = book['volumeInfo']['title']
                authors = 'None'
                book_titles = {title: authors}
            except:
                title = 'None'
                authors = 'None'
                book_titles = {title: authors}
    return book_titles
books = get_nodes(historyBooks)
print(books)

def get_people(works_ls):
    '''
    Attempts to obtain the authors and contributors located in the ORCiD Public Data 2022 XML files
    Parameters:
        works_ls(list): List of works by ORCiD users processed in the ORCiD.py file
    Returns:
        None (incomplete)
    '''
    ns = {
        'xmlns:work': 'http:///www.orcid.org/ns/work'
    }
    for file in works_ls:
        tree = ET.parse(file)
        root = tree.getroot()
        for element in root:
            control = element.find('work:title', ns)
            #incomplete

#get_people(orcid_works)


def makeRequest():
    '''
    Prompts the user to enter a book title and searches the Google Books API for the entered book title
    Parameters:
        None
    Returns:
        Numbered list of responses
    '''
    y = True
    request = input('Please enter a book title or enter exit to exit ')
    while y == True:
        books = []
        param_dict = {'term' : request}
        baseurl = 'https://books.google.com/'
        if str(request).lower() == 'exit':
            y = False
            break
        else:
            response = requests.get(baseurl, param_dict)
            response_json = json.loads(response.text)
            for x in response_json['results']:
                books.append(x)
        print(f"RESULTS")
        a = 1
        num_dict = {}
        if len(books) > 0:
            for x in books:
                print(f"{a}. {x.info()}")
                num_dict[a] = x
                a += 1
        else:
            print(f"No Results")
        request = input("Enter a number for more info, or another book title, or exit. ")
        if request.isnumeric():
            request = int(request)
            obj_inst = num_dict[request]
            webbrowser.open(obj_inst.url)
            y=False
            print("Bye!")
            break
        elif request == 'exit':
            y=False
            break
        else:
            continue


# Cache Stuff

cacheFilename = 'history_books.json'
with open(cacheFilename, "w") as fout:
    json.dump(historyBooks, fout)

def open_cache():
    """
    Opens the cache file if it exists and loads the json into a dictionary. If the cache file doesn't exist, a new cache dictionary is created
    Parameters:
        None
    Returns:
        Opened cache
    """
    try:
        cache_file = open(cacheFilename, 'r')
        cache_contents = cache_file.read()
        historyBooks_cache = json.loads(cache_contents)
        cache_file.close()
    except:
        historyBooks_cache = {}
    return historyBooks_cache

def save_cache(cache):
    """
    Saves the current state of the cache to the disk
    Parameters:
        Detroit_cache (dict): The dictionary to be saved
    Returns:
        None
    """
    dumped_json_cache = json.dumps(cache)
    fw = open(cacheFilename,"w")
    fw.write(dumped_json_cache)
    fw.close()

def historyBooks_cache(): #create cache
    pass


# Graph Stuff

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance=None
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    def setDistance(self, dis):
        self.distance=dis
    def getDistance(self):
        return self.distance

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,f,t,weight=0): 
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

def createGraph(graph):
    pass


if __name__ == "__main__":
    makeRequest()
