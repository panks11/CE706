body = ("""{
  "settings": {
    "similarity": {
      "scripted_tfidf": {
        "type": "scripted",
        "script": {
          "source": "double tf = Math.sqrt(doc.freq); double idf = Math.log((field.docCount+1.0)/(term.docFreq+1.0)) + 1.0; double norm = 1/Math.sqrt(doc.length); return query.boost * tf * idf * norm;"
        }
      }
    },
    "analysis": {
      "analyzer": {
        "my_english_analyzer": { 
          
          "tokenizer": "uax_url_email",
          "filter": [
            "lowercase",
            "asciifolding",
            "english_stop",
            "porter_stem"
            
          ]
        }
      },
      "filter": {
        "english_stop": { 
          "type": "stop",
          "stopwords": "_english_"
        }
      }
    }
  },
  "mappings": {
    "news":{
    "properties": {
      "id":    { "type": "keyword" },  
      "title" : {"type":"text", "similarity":"scripted_tfidf"},
      "content" : {"type":"text", "similarity":"scripted_tfidf"},
      "source" : {"type":"keyword"},
      "published":   { "type": "date"},
      "media-type":  { "type": "keyword"  }
  }}
}
  
}""")

query1 = """
{
"query": {
"bool": {
"must": {
"match": {
"media-type": "News"
}
},
"filter": {
"term": {
"source": "4 Traders"
}
}
}
},
"sort": { "published": { "order": "desc" } }
}"""

query2 ="""{
  "size":0,
  "aggs": {
    "Articles": {
      "filters": {
        "filters": {
          "Blog": {"term":{"media-type": "Blog"}},
          "News":{"term":{"media-type":"News"}}
        }
      }
    }
  }
}"""


query3 = """{
  "query": {
    "query_string": {
      "query": "Scotland^1.7",
      "default_field": "content"
    }
  }
}"""