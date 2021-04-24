import json
import pprint
import requests

ASSET_URL = "http://localhost:8098/buckets/{bucket_name}/keys/{key}"
BUCKET_NAME = "s23452"
DOCUMENT_KEY = "zadanie11"
FORMATTED_URL = ASSET_URL.format(bucket_name=BUCKET_NAME, key=DOCUMENT_KEY)

base_document = {
    "field_key": None,
    "second_key": True,
    "third_key": 123.1,
    "fourth_key": [1, 2, 3]
}


def upload_document(url, document):
    headers = {
        'Content-Type': 'application/json'
    }
    raw_doc = json.dumps(document)
    res = requests.request(method="POST",
                           url=url,
                           headers=headers,
                           data=raw_doc
                           )
    return res.status_code


def retrieve_document(url):
    res = requests.request(method="GET", url=url)
    if res.status_code == 200:
        return json.loads(res.text)
    return "Not found"


# insert the document
_ = upload_document(url=FORMATTED_URL, document=base_document)

# retrieve the document
retrieved_doc = retrieve_document(FORMATTED_URL)
pprint.pprint(retrieved_doc)

# modify and upload
retrieved_doc["new_field"] = {"key1": True, "key2": "string_value"}
_ = upload_document(url=FORMATTED_URL, document=retrieved_doc)

# retrieve once more
new_retrieved_doc = retrieve_document(FORMATTED_URL)
pprint.pprint(new_retrieved_doc)

# delete the document
_ = requests.request(method="DELETE", url=FORMATTED_URL)
not_found_doc = retrieve_document(FORMATTED_URL)
pprint.pprint(not_found_doc)
