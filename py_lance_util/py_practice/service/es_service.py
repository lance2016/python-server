from py_lance_util.utils.es_util import ElasticsearchUtils


def search_es():
    es = ElasticsearchUtils.get_es(ip="49.234.42.199", port=9200)
    print(es.search("index1", query={'query': {'match_all': {}}}))


search_es()
