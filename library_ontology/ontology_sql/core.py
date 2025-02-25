import sqlite3
import networkx as nx

class Ontology:
    def __init__(self):
        self.entities = set()
        self.relations = []

    def add_entity(self, name):
        self.entities.add(name)

    def add_relation(self, from_entity, to_entity, relation_type):
        if from_entity in self.entities and to_entity in self.entities:
            self.relations.append((from_entity, relation_type, to_entity))
        else:
            raise ValueError("Entities must exist before adding relations.")

    def get_relations(self):
        return self.relations


class OntologyStorage:
    def __init__(self, db_path="ontology.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS Entities (id INTEGER PRIMARY KEY, name TEXT UNIQUE)"""
            )
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS Relations 
                (id INTEGER PRIMARY KEY, from_entity TEXT, to_entity TEXT, type TEXT)"""
            )

    def insert_entity(self, name):
        with self.conn:
            self.conn.execute("INSERT OR IGNORE INTO Entities (name) VALUES (?)", (name,))

    def insert_relation(self, from_entity, to_entity, relation_type):
        with self.conn:
            self.conn.execute(
                "INSERT INTO Relations (from_entity, to_entity, type) VALUES (?, ?, ?)",
                (from_entity, to_entity, relation_type),
            )


class OntologyQuery:
    def __init__(self, ontology):
        self.graph = nx.DiGraph()
        for entity in ontology.entities:
            self.graph.add_node(entity)
        for from_entity, relation_type, to_entity in ontology.relations:
            self.graph.add_edge(from_entity, to_entity, relation=relation_type)

    def shortest_path(self, start, end):
        return nx.shortest_path(self.graph, start, end)
