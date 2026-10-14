# 🔷 Neo4j Maintenance Tools

**Python Utilities for Neo4j Database Administration and Data Management**

Neo4jMaintenanceTools is a collection of Python utilities designed to simplify Neo4j database maintenance, record updates, bulk deletions, constraint management, and the execution of multiple Cypher queries.

The repository provides separate scripts for common database operations, helping developers manage graph data and perform maintenance tasks more efficiently.

## ✨ Features

- 🔐 **Constraint Management** — Create single or multiple constraints for Neo4j nodes.
- 📦 **Chunk-Wise Updates** — Update records in manageable batches.
- 🗑️ **Chunk-Wise Deletion** — Delete records in batches to support large-scale data cleanup.
- 🔗 **Flexible Deletion Methods** — Support standard deletion and detach deletion.
- ⚡ **Multi-Query Processing** — Execute multiple Cypher queries against specified nodes.
- 🕸️ **Multi-Node Query Processing** — Process queries involving multiple node types or labels, depending on the implemented query logic.
- 🐍 **Python-Based Automation** — Perform database maintenance tasks using Python scripts.

## 📂 Project Structure

```text
Neo4jMaintenanceTools/
│
├── ConstraintQuery.py          # Constraint creation and management
├── Neo_Chunk_Size_Update.py    # Chunk-wise record updates
├── Neo_ChunkSize_Delete.py     # Chunk-wise record deletion
├── processNeoQuery.py          # Multiple Cypher query processing
└── README.md                   # Project documentation
```

## 🧰 Requirements

- Python 3
- Access to a Neo4j database
- Neo4j Python driver
- Valid database connection details
- Appropriate permissions for the intended database operations

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hemantkarne70-tech/Neo4jMaintenanceTools.git
cd Neo4jMaintenanceTools
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

**Windows — Git Bash**

```bash
source .venv/Scripts/activate
```

**Linux / Ubuntu**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the Neo4j Python driver:

```bash
pip install neo4j
```

Install any additional dependencies required by the individual scripts.

### 4. Configure Neo4j Connection

Configure the connection details required by the scripts, including:

- Neo4j connection URI.
- Database username.
- Authentication credentials.
- Database name, if applicable.
- Node labels, properties, and query parameters as required.

**Security:** Never commit database passwords, access tokens, or confidential connection details to GitHub. Use environment variables or another secure configuration method.

## 📘 Scripts Overview

### 🔐 `ConstraintQuery.py`

Designed to create constraints for nodes in a Neo4j database.

**Key capabilities:**

- Create a constraint for a particular node label and property.
- Create multiple constraints for different node labels or properties.
- Help enforce configured data integrity rules in the graph.

The supported constraint types and exact query-generation behavior depend on the script implementation and Neo4j version.

### 📦 `Neo_Chunk_Size_Update.py`

Designed to update Neo4j records in manageable chunks.

**Key capabilities:**

- Process records in batches rather than attempting to update all records in a single batch.
- Support bulk record maintenance.
- Help manage large update operations through configurable chunk sizes, where supported.

The actual update logic, batch size, and selection criteria depend on the script implementation.

### 🗑️ `Neo_ChunkSize_Delete.py`

Designed to delete Neo4j records in manageable chunks.

**Supported deletion approaches:**

- **DELETE** — Delete nodes or relationships that have no remaining relationships requiring removal.
- **DETACH DELETE** — Delete nodes together with their attached relationships.

**Key capabilities:**

- Perform chunk-wise deletion of matching records.
- Support standard deletion and detach deletion methods.
- Help manage large cleanup operations in smaller batches.

Use caution with `DETACH DELETE`, as it also removes relationships attached to the targeted nodes. Review the selection criteria before executing deletion operations.

### ⚡ `processNeoQuery.py`

Designed to process multiple Cypher queries against specified nodes or multiple node types.

**Key capabilities:**

- Execute multiple configured queries.
- Process additional operations on particular nodes.
- Support query processing across multiple node labels, depending on the query definitions.
- Organize repeatable database operations into a reusable processing workflow.

The exact query configuration, execution sequence, and supported parameters depend on the implementation.

## ⚠️ Important Considerations

- Test all queries against a development database before production use.
- Review constraint definitions before applying them to existing data.
- Ensure the data satisfies a new constraint before creating it.
- Use an appropriate chunk size for large update and deletion operations.
- Validate the selected nodes and relationships before deletion.
- Remember that `DETACH DELETE` removes relationships attached to targeted nodes.
- Handle database transactions and exceptions appropriately.
- Use database accounts with only the permissions required for the task.

## 🔮 Future Enhancements

- [ ] Add a `requirements.txt` file.
- [ ] Support environment-based database configuration.
- [ ] Add configurable logging and error handling.
- [ ] Add dry-run options for deletion operations.
- [ ] Add execution summaries and record-count validation.
- [ ] Add automated tests for Cypher query generation.
- [ ] Document command-line arguments and usage examples.

## 👨‍💻 Author

**Hemant Karne**

Software Engineer | Python | Neo4j | Graph Databases | Data Engineering

GitHub: [@hemantkarne70-tech](https://github.com/hemantkarne70-tech)

---

*Reusable Python utilities for Neo4j constraint management, batch data maintenance, and Cypher query processing.*
