# RapistOps — Volume 1 Roadmap

## Volume 1 Goal

Build the first working RapistOps system capable of importing permitted public-source records, preserving their provenance, structuring the information, connecting related entities, storing it in a database, and searching the resulting records through a basic web application.

# Phase 0 — Project Foundation

Goal: Establish the RapistOps development environment.

- [x] Create project repository
- [x] Create project structure
- [x] Configure Python 3.12
- [x] Configure pyproject.toml
- [x] Install initial dependencies
- [x] Configure pytest
- [x] Create initial Git repository
- [x] Establish .gitignore
- [x] Create initial README
- [x] Verify development environment

# Phase 1 — Core Data Model
Goal: Define the smallest set of objects RapistOps needs to represent, preserve, and connect information.

## 1.1 — Source & Provenance
Goal: Define where information comes from and how its origin is preserved.
- [ ] Define Source
- [ ] Define Provenance

## 1.2 — Records & Evidence
Goal: Define the information being preserved and the evidence associated with it.
- [ ] Define Record
- [ ] Define Evidence

## 1.3 — People & Institutions
Goal: Define the people and organizations represented in records.
- [ ] Define Person
- [ ] Define Institution

## 1.4 — Events & Cases
Goal: Define the things that happened and the cases/proceedings that organize them.
- [ ] Define Event
- [ ] Define Case

## 1.5 — Status
Goal: Define how RapistOps represents the state or outcome of a record, case, or proceeding.
- [ ] Define Status

## 1.6 — Relationships
Goal: Define how objects in the system are explicitly connected.
- [ ] Define Relationship

## 1.7 — Core Model Integration
Goal: Verify that the core objects form a coherent model before moving into the database phase.
- [ ] Identify required relationships between core objects
- [ ] Identify required fields for each object
- [ ] Identify objects that depend on other objects
- [ ] Check that the model preserves provenance and context
- [ ] Check that reported information remains distinguishable from established outcomes
- [ ] Review the complete core data model
- [ ] Confirm Phase 1 is complete

# Phase 2 — Database

Goal: Persist the core RapistOps data.

- [ ] Configure PostgreSQL
- [ ] Create initial database schema
- [ ] Create Source storage
- [ ] Create Record storage
- [ ] Create Evidence storage
- [ ] Create Person storage
- [ ] Create Institution storage
- [ ] Create Event storage
- [ ] Create Case storage
- [ ] Create Relationship storage
- [ ] Create Status storage
- [ ] Create Provenance storage
- [ ] Test database operations

# Phase 3 — Source Import

Goal: Bring a real permitted public-source record into the system.

- [ ] Define source-import interface
- [ ] Implement first source importer
- [ ] Retrieve source data
- [ ] Preserve original source reference
- [ ] Record collection timestamp
- [ ] Store imported record
- [ ] Handle invalid source data
- [ ] Test successful import
- [ ] Test failed import

# Phase 4 — Evidence & Provenance

Goal: Make every imported piece of information traceable to its source.

- [ ] Associate records with sources
- [ ] Associate evidence with records
- [ ] Store provenance metadata
- [ ] Store collection history
- [ ] Preserve original source information
- [ ] Distinguish source record from interpretation
- [ ] Distinguish allegation/report from adjudicated outcome
- [ ] Test provenance relationships

# Phase 5 — Entity Processing

Goal: Turn imported records into structured entities.

- [ ] Extract people
- [ ] Extract institutions
- [ ] Extract events
- [ ] Extract cases
- [ ] Normalize entity fields
- [ ] Associate entities with records
- [ ] Handle incomplete information
- [ ] Preserve uncertainty
- [ ] Test entity creation

# Phase 6 — Relationships

Goal: Connect the entities represented by the records.

- [ ] Define initial relationship types
- [ ] Connect people to cases
- [ ] Connect people to events
- [ ] Connect people to institutions
- [ ] Connect records to cases
- [ ] Connect evidence to records
- [ ] Connect sources to records
- [ ] Query relationships
- [ ] Test relationship creation

# Phase 7 — Case & Status Tracking

Goal: Represent the state of information without collapsing different outcomes.

- [ ] Implement reported status
- [ ] Implement investigation status
- [ ] Implement charged status
- [ ] Implement dismissal status
- [ ] Implement acquittal status
- [ ] Implement conviction status
- [ ] Implement other relevant statuses
- [ ] Associate statuses with cases
- [ ] Preserve status history
- [ ] Test status transitions

# Phase 8 — Search

Goal: Make the stored information discoverable.

- [ ] Implement person search
- [ ] Implement case search
- [ ] Implement record search
- [ ] Implement institution search
- [ ] Implement evidence search
- [ ] Implement basic filtering
- [ ] Return source/provenance information with results
- [ ] Test search behavior

# Phase 9 — API

Goal: Expose the core RapistOps functionality through an API.

- [ ] Create FastAPI application
- [ ] Create health endpoint
- [ ] Create person endpoints
- [ ] Create case endpoints
- [ ] Create record endpoints
- [ ] Create evidence endpoints
- [ ] Create search endpoint
- [ ] Create relationship endpoint
- [ ] Add API validation
- [ ] Test API endpoints

# Phase 10 — Basic Web Application

Goal: Provide a usable browser interface for the V1 system.

- [ ] Create React/TypeScript application
- [ ] Connect frontend to API
- [ ] Create search interface
- [ ] Create search results view
- [ ] Create person view
- [ ] Create case view
- [ ] Create record/evidence view
- [ ] Display source/provenance information
- [ ] Display relationships
- [ ] Display case status

# Phase 11 — V1 Integration

Goal: Connect the complete V1 pipeline.

- [ ] Source
- [ ] Import
- [ ] Record
- [ ] Evidence
- [ ] Entity processing
- [ ] Relationships
- [ ] Case/status
- [ ] Database
- [ ] API
- [ ] Web application

The complete V1 flow should work:

**Public Source → Import → Preserve → Structure → Connect → Store → Search → Display**

# Phase 12 — V1 Testing & Release

Goal: Verify that Volume 1 actually works as a complete system.

- [ ] Unit tests
- [ ] Database integration tests
- [ ] Import tests
- [ ] Provenance tests
- [ ] Entity tests
- [ ] Relationship tests
- [ ] Status tests
- [ ] Search tests
- [ ] API tests
- [ ] Frontend integration test
- [ ] End-to-end test
- [ ] Local deployment test
- [ ] Document V1
- [ ] Tag RapistOps V1 release