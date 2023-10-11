import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import string
import spacy

nlp = spacy.load("en_core_web_sm")

# Function to extract locations from text
def extract_locations(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return locations


data = []

def is_valid_string(s):
    # Define a set of allowed characters (letters, spaces, and underscores)
    allowed_chars = set(string.ascii_letters + ' ' + '_')

    # Check if the string contains any disallowed characters
    return all(char in allowed_chars for char in s)


def read_titles():
    x = 0
    f = open("../data/all_wiki_titles.txt")
    for line in f:
        # x+= 1
        # if x > 100:
        #     break
        line = line.strip()
        if is_valid_string(line):
            actual_title = " ".join(line.split("_"))
            locations = extract_locations(actual_title)
            if len(locations) > 0:
                print(locations)
                data.append({'Name':line})
            else:
                print(f"{line}  not a location")
            print("___________________")

# Use a service account.
# cred = credentials.Certificate('/Users/rahatibnrafiq/startups/WalkWithMeDev/data/walkwithme-2d86e-firebase-adminsdk-3sysz-95b4347461.json')
# app = firebase_admin.initialize_app(cred)
# db = firestore.client()

read_titles()
print(len(data))
# for record in data:
#     try:
#         doc_ref = db.collection("titles").document(record['Name'])
#         doc_ref.set({"title": record['Name']})
#     except Exception as e:
#         print(f"Exception {e} while inserting record: {record}")


    






