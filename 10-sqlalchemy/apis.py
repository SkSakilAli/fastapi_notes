#SQLAlchemy APIs
"""
SQLAlchemy's functionality is divided into two main API's

#SQLAlchemy CORE
This is the lower-level API that offers a schema-centric, SQL expression
language for building and executing SL quieries. It provides:

-- Engine : The starting point of any SQLAlchemy appli9cation,
manages the connection of database

-- Connection : Represents an individual DBAPI Connection

-- MetaData : A Connection of Table Objects and their associated schema constructs

-- Table and Columns : Define Database tables and their coluns

-- SQL Expressions : Allow construction of SWL queroes using Py objects
"""
"""
#SQLAlchemy ORM ---

The ORM API enales mapping of py classes to database tables, 
allowing developers to wwork with database records as Py objects

-- Declarative Base : A base class for defining ORM models
 (Py clases mapped to tables).

-- Sesson: Manages persistence operations for ORM-mapped objects
such as add, delete and query

-- Query : Provides a high-level interface for constructing database
queries using Pythonic Syntax.

-- RelationShips : Define Relationships ( eg, one to many, many to one) b/w tables/class

"""