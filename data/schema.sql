CREATE TABLE source (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    organization TEXT,
    location TEXT,
    access_reference TEXT
);

CREATE TABLE provenance (
    id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES source(id),
    collected_at TIMESTAMP NOT NULL,
    collection_method TEXT NOT NULL,
    source_reference TEXT,
    collection_context TEXT
);

CREATE TABLE record (
    id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL REFERENCES source(id),
    provenance_id INTEGER NOT NULL REFERENCES provenance(id),
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    source_reference TEXT,
    created_at TIMESTAMP,
    published_at TIMESTAMP,
    collected_at TIMESTAMP
);

CREATE TABLE evidence (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    source_id INTEGER NOT NULL REFERENCES source(id),
    provenance_id INTEGER NOT NULL REFERENCES provenance(id),
    record_id INTEGER NOT NULL REFERENCES record(id),
    reference TEXT,
    description TEXT
);

CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    identifiers TEXT,
    description TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE institution (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    jurisdiction TEXT,
    location TEXT,
    description TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE event (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    occurred_at TIMESTAMP,
    location TEXT,
    description TEXT
);

CREATE TABLE cases (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    identifier TEXT,
    description TEXT,
    opened_at TIMESTAMP,
    closed_at TIMESTAMP
);

CREATE TABLE status (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    entity_id INTEGER NOT NULL,
    effective_at TIMESTAMP,
    source_id INTEGER REFERENCES source(id),
    record_id INTEGER REFERENCES record(id),
    description TEXT
);

CREATE TABLE relationship (
    id INTEGER PRIMARY KEY,
    source_entity_id INTEGER NOT NULL,
    target_entity_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    source_id INTEGER REFERENCES source(id),
    record_id INTEGER REFERENCES record(id),
    effective_at TIMESTAMP,
    description TEXT
);