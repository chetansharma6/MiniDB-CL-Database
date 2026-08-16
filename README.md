# MiniDB

MiniDB is a command-line database built from scratch in Python. The purpose of this project is to understand how databases work internally by implementing the core concepts myself instead of relying on an existing database engine, ORM, framework, or third-party library. The project will start with a simple JSON-backed database and progressively evolve into a more advanced system involving custom storage, parsing, indexing, HTTP, networking, and eventually C.

> **Build it. Break it. Understand it. Improve it.**

---

## Project Goals

The main goal of MiniDB is learning through implementation.

I want to understand:

- How databases store data
- How records and tables work
- How data is persisted to disk
- How queries are parsed
- How records are searched
- How updates and deletes work
- How databases handle invalid input
- Why databases need indexes
- How binary storage works
- How databases communicate over a network
- How higher-level Python concepts map to lower-level C concepts

This is not intended to compete with SQLite, PostgreSQL, or other production database systems.

It is a learning project designed to remove some of the abstraction and expose the underlying concepts.

---

## Example

The first version of MiniDB is intended to work like this:

    $ python minidb.py

    MiniDB v1.0

    > create users
    Table 'users' created.

    > insert users name=John age=21
    Inserted record #1.

    > insert users name=Sarah age=24
    Inserted record #2.

    > select users
    ID    name     age
    1     John     21
    2     Sarah    24

    > find users name=Sarah
    ID    name     age
    2     Sarah    24

    > update users 1 age=22
    Updated record #1.

    > delete users 2
    Deleted record #2.

    > exit

---

## Current Status

 Early development

The project is being built incrementally.

The initial version will focus on:

- [ ] Command-line interface
- [ ] JSON storage
- [ ] Table creation
- [ ] Record insertion
- [ ] Record selection
- [ ] Record searching
- [ ] Record updating
- [ ] Record deletion
- [ ] Automatic record IDs
- [ ] Input validation
- [ ] Error handling
- [ ] Automated tests

---

# Architecture

The initial architecture is intentionally simple.

    User
     |
     v
    CLI
     |
     v
    Parser
     |
     v
    Database
     |
     v
    Storage
     |
     v
    JSON File

Each component has a specific responsibility.

### CLI

Responsible for interacting with the user.

### Parser

Responsible for turning commands such as:

    insert users name=John age=21

into structured information the database can understand.

### Database

Responsible for the actual database operations:

- Create
- Insert
- Select
- Find
- Update
- Delete

### Storage

Responsible for saving and loading database data.

The database should not need to know whether the data is stored as JSON, binary data, or something else.

This separation will become important as the project evolves.

---

# Project Structure

The initial project structure will look like:

    minidb/
    |
    +-- minidb.py
    +-- database.py
    +-- storage.py
    +-- parser.py
    |
    +-- tests/
    |   +-- test_database.py
    |   +-- test_storage.py
    |   +-- test_parser.py
    |
    +-- data/
    |   +-- database.json
    |
    +-- README.md
    +-- .gitignore

The structure may change as the project grows.

---

# Storage

The first version will use JSON for persistence.

For example:

    {
        "users": [
            {
                "id": 1,
                "name": "John",
                "age": 21
            }
        ]
    }

The basic data flow will be:

    Python Objects
          |
          v
    Serialization
          |
          v
        JSON
          |
          v
         Disk

When MiniDB starts again:

         Disk
          |
          v
        JSON
          |
          v
    Deserialization
          |
          v
    Python Objects

This will provide a practical introduction to:

- File I/O
- Serialization
- Deserialization
- JSON
- Persistence
- Error handling

JSON is intentionally being used first because it makes the storage system easy to understand.

The project will eventually explore why real databases use more specialized storage formats.

---

# Database Concepts

## Tables

A table is a collection of records.

Example:

    users

    +----+-------+-----+
    | id | name  | age |
    +----+-------+-----+
    | 1  | John  | 21  |
    | 2  | Sarah | 24  |
    +----+-------+-----+

Questions to understand:

- How should tables be represented internally?
- How are tables identified?
- What happens if a table already exists?
- What should an empty table look like?

---

## Records

A record represents one row of data.

Example:

    {
        "id": 1,
        "name": "John",
        "age": 21
    }

Questions to understand:

- How are records represented in memory?
- How are records stored?
- How are records identified?
- Can records have different fields?

---

## Primary Keys

Each record will have an ID.

Example:

    id = 1
    id = 2
    id = 3

The ID will initially act as the record's unique identifier.

Questions to understand:

- How should IDs be generated?
- Should IDs be reused after deletion?
- How do we guarantee uniqueness?
- How would a real database handle this?

---

# Commands

The initial command language will support:

## Create

    create users

Creates a new table.

---

## Insert

    insert users name=John age=21

Adds a record to the table.

---

## Select

    select users

Returns all records in the table.

---

## Find

    find users name=Sarah

Searches for records matching a field value.

---

## Update

    update users 1 age=22

Updates record `1`.

---

## Delete

    delete users 2

Deletes record `2`.

---

# Development Roadmap

## Phase 1 — Project Foundation

Build the basic application.

Learn:

- Python modules
- Functions
- Classes
- Imports
- Type hints
- Exceptions
- Command-line input
- Program entry points

Goal:

    $ python minidb.py

    MiniDB v1.0

    >

---

## Phase 2 — JSON Storage

Implement persistent storage.

Learn:

- `json`
- `pathlib`
- File reading
- File writing
- Serialization
- Deserialization
- File exceptions

Goal:

Data should survive restarting the program.

For example:

    $ python minidb.py

    > insert users name=John age=21
    Inserted record #1.

    > exit

Then:

    $ python minidb.py

    > select users

    ID    name    age
    1     John    21

---

## Phase 3 — Tables

Implement table creation.

Commands:

    create users
    create products
    create orders

Learn:

- Dictionaries
- Lists
- Data organization
- Validation
- Duplicate detection

---

## Phase 4 — Records

Implement record insertion and IDs.

Example:

    insert users name=John age=21

Learn:

- Dictionaries
- Lists
- Unique identifiers
- Record lookup
- ID generation

---

## Phase 5 — CRUD

Implement the complete set of basic operations:

    CREATE
    INSERT
    SELECT
    FIND
    UPDATE
    DELETE

At the end of this phase, MiniDB should be a functional small database.

---

## Phase 6 — Command Parser

Build a parser for commands such as:

    insert users name=John age=21

The parser needs to determine:

    command = insert
    table = users
    fields = name=John, age=21

Start simple.

Use Python string operations first.

Eventually explore:

- Tokenization
- Parsing
- Validation
- Command grammars
- Interpreters

This phase is an opportunity to understand how a small language works.

---

## Phase 7 — Validation and Error Handling

MiniDB should handle bad input without crashing.

Examples:

    > insert

    Usage: insert <table> <field=value>...

    > select products

    Table 'products' does not exist.

    > delete users 999999

    Record #999999 does not exist.

    > create users

    Table 'users' already exists.

Test cases should include:

- Missing arguments
- Invalid commands
- Missing tables
- Missing records
- Duplicate tables
- Invalid values
- Invalid JSON
- Corrupted storage files

Learn:

- Exceptions
- Custom exceptions
- Validation
- Defensive programming
- Error messages

---

## Phase 8 — Testing

Once the core functionality works, add automated tests.

Tests should cover:

### Database

- Creating tables
- Creating duplicate tables
- Inserting records
- Selecting records
- Finding records
- Updating records
- Deleting records

### Storage

- Creating database files
- Loading data
- Saving data
- Missing files
- Invalid JSON
- Corrupted data

### Parser

- Valid commands
- Invalid commands
- Missing arguments
- Invalid arguments
- Unexpected input

The purpose of testing is to understand how to verify that changes do not break existing functionality.

---

# Phase 9 — Improve the Storage Engine

The JSON implementation will intentionally have limitations.

For example, changing one record may require rewriting the entire JSON file.

That leads to an important question:

> Why don't real databases simply store everything as JSON?

This phase will explore:

- Binary data
- Serialization formats
- File offsets
- Fixed-size records
- Variable-size records
- Append-only storage
- Free space
- Corruption
- Checksums
- Recovery

---

# Phase 10 — Binary Storage

Replace JSON storage with a custom binary format.

A possible file structure could eventually look like:

    Database File
    |
    +-- Header
    +-- Metadata
    +-- Records
    +-- Indexes
    +-- Other metadata

Learn:

- `bytes`
- Binary encoding
- `struct`
- `seek()`
- `read()`
- `write()`
- File offsets
- Serialization
- Deserialization

The goal is to understand how data is represented physically on disk.

---

# Phase 11 — Indexes

The initial `find` implementation will probably scan every record.

For example:

    Search
      |
      +-- Record 1
      +-- Record 2
      +-- Record 3
      +-- Record 4
      +-- ...
      |
      +-- Find match

This works, but becomes inefficient as the database grows.

An index could eventually provide something more like:

    Search
      |
      v
    Index
      |
      v
    Record Location
      |
      v
    Record

Topics to explore:

- Hash tables
- Hash functions
- B-trees
- B+ trees
- Search complexity
- Index maintenance
- Storage overhead

---

# Phase 12 — HTTP API

Once the database engine is stable, expose it through HTTP.

Possible endpoints:

    GET    /users
    GET    /users/1
    POST   /users
    PUT    /users/1
    DELETE /users/1

Architecture:

    HTTP Client
         |
         v
    HTTP Server
         |
         v
    MiniDB Engine
         |
         v
       Storage

The HTTP layer should communicate with the database engine rather than implementing database logic itself.

Learn:

- HTTP
- Requests
- Responses
- HTTP methods
- Status codes
- Headers
- JSON APIs
- Networking
- Client/server architecture

The initial implementation can use Python's standard library.

---

# Phase 13 — MiniDB Client

Build a separate Python client:

    client.py

Architecture:

    +-------------+
    |   client.py |
    +------+------+
           |
           | HTTP
           v
    +-------------+
    | MiniDB API  |
    +------+------+
           |
           v
    +-------------+
    |   Database  |
    |    Engine   |
    +------+------+
           |
           v
    +-------------+
    |   Storage   |
    +-------------+

This creates a complete client/server system.

---

# Phase 14 — C Implementation

After the Python implementation is understood, selected parts of MiniDB can be rebuilt in C.

The goal is not to rewrite everything just for the sake of using another language.

The goal is to understand what Python abstracts away.

Potential areas:

- Record representation
- Binary storage
- Serialization
- File management
- Index structures

For example:

    struct Record {
        int id;
        char name[50];
        int age;
    };

Topics to explore:

- Structs
- Pointers
- Arrays
- Memory management
- File operations
- Binary files
- Memory layout
- Data representation

The C implementation comes later so that the database concepts are already understood.

---

# Technology

## Initial Technology

- Python
- Python Standard Library
- JSON
- File I/O
- `pathlib`
- `json`
- `argparse`
- Type hints
- `unittest`

## Future Technology

- Binary file formats
- HTTP
- Networking
- Indexing
- C
- Systems programming

Third-party libraries will be avoided during the early stages unless there is a specific reason to introduce one.

---

# Git Workflow

Git will be used throughout development.

The project will be developed using feature branches instead of putting every change directly into `main`.

Example:

    main
     |
     +-- feature/storage
     |
     +-- feature/tables
     |
     +-- feature/parser
     |
     +-- feature/crud
     |
     +-- feature/tests

Example commits:

    Initial project structure
    Implement JSON storage
    Add database class
    Add table creation
    Add record insertion
    Add record selection
    Add record search
    Add record updates
    Add record deletion
    Add command parser
    Add validation
    Add automated tests
    Improve error handling

The Git history should show the development process rather than one large final commit.

---

# Learning Philosophy

One of the main goals of MiniDB is to learn by solving problems rather than copying implementations.

When I encounter a problem, the intended process is:

    Identify the problem
            |
            v
    Research the concept
            |
            v
    Read documentation
            |
            v
    Experiment
            |
            v
    Make mistakes
            |
            v
    Debug
            |
            v
    Understand
            |
            v
    Implement
            |
            v
    Test

For example, instead of searching for:

    "give me Python code for a database"

I want to research individual concepts:

    "Python write dictionary to JSON"
    "Python FileNotFoundError"
    "Python parse command line input"
    "What is serialization?"
    "How does a file offset work?"
    "How does HTTP POST work?"
    "What is a hash table?"
    "Why do databases use indexes?"

The goal is not simply to make MiniDB work.

The goal is to understand why it works.

---

# What I Expect to Learn

## Python

- Functions
- Classes
- Dictionaries
- Lists
- Exceptions
- Modules
- File I/O
- JSON
- `pathlib`
- `argparse`
- Type hints
- Testing
- Package structure

## Databases

- Tables
- Records
- Primary keys
- CRUD operations
- Persistence
- Storage engines
- Serialization
- Data integrity
- Searching
- Indexing
- Query processing

## Computer Science

- Data structures
- Searching
- Algorithmic complexity
- Parsing
- Serialization
- File formats
- Binary data
- Memory representation

## Networking

- HTTP
- Client/server architecture
- Requests
- Responses
- APIs
- Sockets

## Systems Programming

Eventually:

- C
- Pointers
- Structs
- Memory
- Binary files
- File offsets
- Memory layout
- Data representation

## Software Engineering

- Git
- Branching
- Commits
- Testing
- Debugging
- Error handling
- Documentation
- Modular design

---

# Engineering Principles

## Keep Dependencies Minimal

The early versions should rely primarily on Python's standard library.

This keeps the focus on understanding the implementation instead of learning a framework.

## Separate Responsibilities

The CLI should not contain database logic.

The parser should not handle storage.

The storage layer should not care how the user entered a command.

The architecture should remain approximately:

    CLI
     |
     v
    Parser
     |
     v
    Database
     |
     v
    Storage

## Build Incrementally

Each phase should produce something functional.

    Small Feature
         |
         v
        Test
         |
         v
      Understand
         |
         v
       Improve
         |
         v
    Next Feature

## Understand Before Abstracting

Avoid creating abstractions simply because they look professional.

An abstraction should exist because it solves a real problem in the project.

---

# Success Criteria

The first major milestone is being able to explain the entire data flow:

    User enters command
            |
            v
    CLI receives input
            |
            v
    Parser interprets command
            |
            v
    Database validates operation
            |
            v
    Database modifies records
            |
            v
    Storage serializes data
            |
            v
    Data is written to disk

When the program starts again:

    Disk
     |
     v
    Storage reads data
     |
     v
    Data is deserialized
     |
     v
    Database loads state
     |
     v
    CLI becomes available

Later versions will replace parts of this system with more sophisticated implementations.

---

# Long-Term Vision

The long-term architecture may eventually look like:

                         MiniDB
                            |
              +-------------+-------------+
              |             |             |
             CLI        HTTP API       Client
              |             |             |
              +-------------+-------------+
                            |
                     Database Engine
                            |
              +-------------+-------------+
              |             |             |
           Parser        Indexes      Transactions
              |             |             |
              +-------------+-------------+
                            |
                       Storage Engine
                            |
                  +---------+---------+
                  |                   |
                JSON                Binary
                  |                   |
                  +---------+---------+
                            |
                           Disk

This is a long-term direction, not the starting architecture.

The project will grow only when the previous layer is understood.

---

# Final Goal

MiniDB is not about creating another database.

It is about taking something that normally feels like a black box and gradually opening it up.

The project starts with:

    Python
      +
    Dictionaries
      +
    Lists
      +
    JSON
      +
    Files

Then progresses toward:

    Parsing
       |
       v
    Storage
       |
       v
    Indexes
       |
       v
    Binary Formats
       |
       v
    HTTP
       |
       v
    Client/Server Systems
       |
       v
    C
       |
       v
    Memory and Systems Programming

The project starts as a small command-line program and is intentionally designed to grow into a deeper exploration of databases, software engineering, networking, and computer systems.

> Build it. Break it. Understand it. Improve it.
