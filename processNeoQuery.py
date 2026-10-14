from neo4j import GraphDatabase

NEO_IP = "xxx.xxx.xxx.xxx"
NEO_PORT = "7687"

class Neo4jHandler:
    def __init__(self):
        self.driver = GraphDatabase.driver(f"bolt://{NEO_IP}:{NEO_PORT}", encrypted=False)

    def close(self):
        self.driver.close()

    def run_queries(self, queries):
        with self.driver.session() as session:
            for query in queries:
                result = session.run(query)
                print(f"Result for query: {query}")
                for record in result:
                    print(record)

queries = [
    'match(n:node1) where n.property = "ABC" set n.doc_field = "Testdoc" return count(n)',
    'match(n:node1) where n.property = "XYZ" set n.doc_field = "Newdoc" return count(n)',
    'match(n:node2) where n.field = "JKLM" set n.status = "Successful" return count(n)'    
]

neo4j_handler = Neo4jHandler()
try:
    neo4j_handler.run_queries(queries)
finally:
    neo4j_handler.close()
