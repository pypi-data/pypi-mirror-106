from elasticsearch import Elasticsearch

class Searchengine:
    def __init__(self, url, port):
        self.cursor = Elasticsearch([url + ":" + str(port)])

    def match(self, ind, layer, query, size, source):
        q = {
            "query": {
                "match": {
                    layer: query,
                    }
                    },
                    "size" : size,
                    "_source": source
                    }
        res = self.cursor.search(index=ind, request_timeout=30, body=q)
        results = []
        for record in res["hits"]["hits"]:
            results.append(record["_source"]["subcorpus"])
        return results

    def matchPhrase(self, ind, layer, query, slop, size, source):
        q = {
            "query": {
                "match_phrase": {
                    layer : {
                        "query" : query,
                    "slop" : slop
                    }
                }
                    },
                    "size" : size,
                    "_source": source
                    }
        res = self.cursor.search(index=ind, request_timeout=30, body=q)
        results = []
        for record in res["hits"]["hits"]:
            results.append(record["_source"]["subcorpus"])
        return results


if __name__ == "__main__":
    se = Searchengine("http://wp-elasticsearch.fritz.box", 9200)
    seresults = se.matchPhrase("wp", "token", "Salz und Pfeffer", 0,  1000, True)
    print(seresults)
    print("Number of results: ", len(seresults))
    print("Done.")