from elasticsearch import Elasticsearch
from index import body
import json



query_body = """{
  "query": {
    "query_string": {
      "query": "Scotland^1.7",
      "default_field": "title"
    }
  }
}"""


def get_documents(index_name, query_body, fields =[]):
    """ The function takes input the index name, query, output field in specific
        The function returns the result
    """
    results = es.search(index=index_name,body=query_body)
    for result in results['hits']['hits']:
        print(15*'*',"Query Output",15*'*')
        print ("Score", result['_score'])
        if fields:
            for field in fields:
                print(result['_source'][field])
        else:
            print(result['_source'])

if __name__ == '__main__':
    index_name = 'articles'
    # setup Elastic Search Connection
    es = Elasticsearch("http://localhost:9200")
    print(es.info())
    get_documents(index_name,query_body)