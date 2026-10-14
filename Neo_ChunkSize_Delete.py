from neo4j import GraphDatabase

NEO_IP = "xxx.xxx.xxx.xxx"
NEO_PORT = "7687"

start_skip = 0
end_skip = 500000
limit = 10000

def update_nodes_with_skip(tx, skip):
    query = f"""match(n:node) where n.property = "ABC" with n skip {skip} limit {limit} detach delete n"""
    result = tx.run(query)
    # count = result.single()[0]
    print(f"Updated nodes with skip {skip}")

neo_driver = GraphDatabase.driver(f"bolt://{NEO_IP}:{NEO_PORT}", encrypted=False)

for skip in range(start_skip, end_skip + 1, limit):
    with neo_driver.session() as session:
        session.write_transaction(update_nodes_with_skip, skip)

neo_driver.close()
