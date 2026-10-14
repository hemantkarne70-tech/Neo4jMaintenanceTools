from neo4j import GraphDatabase

NEO_IP = "xxx.xxx.xxx.xxx"
NEO_PORT = "7687"

constraint_queries = [
    "CREATE CONSTRAINT ON (n1:node1) ASSERT n1.property IS UNIQUE",
    "CREATE CONSTRAINT ON (n2:node2) ASSERT n2.property IS UNIQUE",
    "CREATE CONSTRAINT ON (n3:node3) ASSERT n3.property IS UNIQUE"
]

def execute_query(driver, query):
    with driver.session() as session:
        session.run(query)

# Connect to Neo4j
driver = GraphDatabase.driver(f"bolt://{NEO_IP}:{NEO_PORT}", encrypted=False)

for query in constraint_queries:
    execute_query(driver, query)

driver.close()
