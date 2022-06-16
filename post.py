from elasticsearch import Elasticsearch
from index import body
import json



def post_documents(index_name, doc_type, document_list):
    """ The function takes input the index name, document type and list of documents in dictionary format
        The function post the documents iteratively using es.index() method
    """
    for i in range(100000,1000000):
        print(i)
        result = json.loads(document_list[i])
        doc = {"id":result['id'],
            "content":result['content'],
            "title":result['title'],
            "media-type":result['media-type'],
            "source":result['source'],
            "published":result['published']}
        resp = es.index(index = index_name, id = result['id'], body = doc, doc_type = doc_type)
        print("Posted doc : ", result['id'])

if __name__ == '__main__':
    index_name = 'articles'
    doc_type = 'news'
    # setup Elastic Search Connection
    es = Elasticsearch("http://localhost:9200")
    print(es.info())
    # es.indices.create("articles",body=body)
    with open('../../sample-1M.jsonl', 'r') as json_file:
        json_list = list(json_file)
    post_documents(index_name,doc_type,json_list)