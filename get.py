from elasticsearch import Elasticsearch
from index import query1,query2,query3
import json

def get_documents(index_name, query_body, fields =[]):
    """ The function takes input the index name, query, output field in specific
        The function returns the result
    """
    results = es.search(index=index_name,body=query_body)
    print_lines = 0
    for result in results['hits']['hits']:
        print ("Score", result['_score'])
        if fields:
            for field in fields:
                print(result['_source'][field])
        else:
            print(result['_source'])
        print_lines +=1
        if print_lines:
          break
    return results

if __name__ == '__main__':
    index_name = 'articles'
    # setup Elastic Search Connection
    es = Elasticsearch("http://localhost:9200")
    print(es.info())
    print("*******************Query 1 Results ****************************")
    r = get_documents(index_name,query1)
    print("*******************Query 2 Results ****************************")
    r = get_documents(index_name,query2)
    print(r)
    print("*******************Query 3 Results ****************************")
    get_documents(index_name,query3)