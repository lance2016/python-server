import elasticsearch


class ElasticsearchUtils:
    def __init__(self, host='localhost', port=9200):
        self.es = elasticsearch.Elasticsearch([{'host': host, 'port': port}])

    def search(self, index, query):
        """
        Search documents in the specified index.
        """
        return self.es.search(index=index, body=query)

    def create_document(self, index, doc_type, doc_id, body):
        """
        Create a new document in the specified index.
        """
        return self.es.create(index=index, doc_type=doc_type, id=doc_id, body=body)

    def update_document(self, index, doc_type, doc_id, body):
        """
        Update an existing document in the specified index.
        """
        return self.es.update(index=index, doc_type=doc_type, id=doc_id, body=body)

    def delete_document(self, index, doc_type, doc_id):
        """
        Delete a document from the specified index.
        """
        return self.es.delete(index=index, doc_type=doc_type, id=doc_id)

    @classmethod
    def get_es(self, ip: str, port: int = 9200):
        return ElasticsearchUtils(host=ip, port=port)
