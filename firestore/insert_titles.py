import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import string
import spacy

nlp = spacy.load("en_core_web_sm")

# Function to extract locations from text
def location_using_ner(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ["LOC", "GPE", "ORG", "FAC"]]
    return locations


data = []

def is_valid_string(s):
    # Define a set of allowed characters (letters, spaces, and underscores)
    allowed_chars = set(string.ascii_letters + ' ' + '_')

    # Check if the string contains any disallowed characters
    return all(char in allowed_chars for char in s)


def filter_special_characters():
    x = 0
    f = open("../data/all_wiki_titles.txt")
    filtered_candidates = set()
    for line in f:
        x+=1
        line = line.strip()
        if is_valid_string(line):
            actual_title = " ".join(line.split("_"))
            filtered_candidates.add(actual_title)
    f.close()
    
    with open("../data/filtered_special_characters.txt", "w") as f:
        filtered_candidates = list(filtered_candidates)
        for location_candidate in filtered_candidates:
            f.write(location_candidate+"\n")
            

# Use a service account.
# cred = credentials.Certificate('/Users/rahatibnrafiq/startups/WalkWithMeDev/data/walkwithme-2d86e-firebase-adminsdk-3sysz-95b4347461.json')
# app = firebase_admin.initialize_app(cred)
# db = firestore.client()

# filter_special_characters()
# print(len(data))



# for record in data:
#     try:
#         doc_ref = db.collection("titles").document(record['Name'])
#         doc_ref.set({"title": record['Name']})
#     except Exception as e:
#         print(f"Exception {e} while inserting record: {record}")


    






