# ORCiD Data
import json
import os
import os.path
import xml.etree.ElementTree as ET

orcid_dir = os.path.join('ORCID_2022_10_activities_0', '010')

def inThisArchive(dir):
    '''
    Looks inside the tar archive files from the ORCiD Public Data File and returns their contents.
    This includes the ORCiD ID of the person and their activities, including education, employment,
    qualifications, and (most importantly) works. 
    Parameters:
        dir(filepath): The filepath to the chosen directory
    Returns:
        N/A
    '''
    with os.scandir(dir) as items_list:
        works_ls = []
        for item in items_list:
            if item.is_file():
                print (item.name, 'is a file')
                continue
            if item.is_dir():
                print(item.name, 'is a directory')
                new_path = os.path.join(dir, item.name)
                with os.scandir(new_path) as entry_list:
                    for entry in entry_list:
                        print(item, 'has the following files: ', entry.name)
                        if entry.name == 'works':
                            xtra_new_path = os.path.join(new_path, entry.name)
                            with os.scandir(xtra_new_path) as works_list:
                                for work in works_list:
                                    works_ls.append(work)
                                    print(item, 'has the following works: ', work.name)
        return works_ls


orcid_works = inThisArchive(orcid_dir)
#print(orcid_works)

def get_data(works_ls):
    ns = {
        'xs:schema': 'http://www.w3.org/2001/XMLSchema'
    }
    for file in works_ls:
        tree = ET.parse(file)
        root = tree.getroot()
        toString = [ET.tostring(root)]
    print(toString)
    #return toString

orcid_data = get_data(orcid_works)
print(orcid_data)
# with open ('orcid_works.json', 'w') as fout:
#     json.dump(orcid_data, fout)










