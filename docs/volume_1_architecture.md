# RapistOps — Volume 1 Architecture

**Version:** 0.1.0

## 1. Purpose
Volume 1 establishes the first working architecture of RapistOps.

The purpose of this volume is to create a small but functional system capable of taking information from permitted public or otherwise lawfully accessible sources, preserving its origin and context, structuring the information into usable records, connecting related entities, storing the resulting data, and making that information searchable and viewable.

Volume 1 is the foundation for the larger RapistOps system described in the Master Architecture.

It is intentionally limited. The goal is not to build the complete long-term platform in the first version, but to establish the core system pattern that later capabilities can build upon.

## 2. Volume 1 Goal
The goal of Volume 1 is to establish the first complete working data path through RapistOps:
Source

Import

Preserve

Structure

Connect

Store

Search

Display

A successful Volume 1 implementation should demonstrate that a permitted source can enter the system as information, retain its provenance, become structured data, become related to other records and entities, be stored persistently, and later be retrieved through search and displayed to a user.

Volume 1 does not attempt to solve every problem represented in the Master Architecture.

## 3. Core System Flow

### 3.1 Source
A source is the origin from which information enters RapistOps.

A source may include publicly available or otherwise lawfully accessible:
- Public web pages
- Public documents
- Public databases
- Government records
- Public court records
- Public institutional records
- Authorized APIs or feeds
- User-provided records

The system must retain information about where imported information originated.

### 3.2 Import
Import is the process of bringing information from an allowed source into RapistOps.

Import may eventually occur through different mechanisms, including:
- Manual import
- API retrieval
- Document import
- Web collection
- Authorized data feeds

Volume 1 should establish the underlying import concept without requiring every possible collection mechanism.

An import should not cause the original source context to be discarded.

### 3.3 Preserve
Preservation means retaining the information necessary to understand what was collected, where it came from, and when it was collected.

RapistOps should preserve relevant provenance and source context rather than treating imported information as anonymous data.

Where appropriate, the system should retain:
- Source identity
- Source location
- Collection time
- Original record information
- Relevant document or page metadata
- The relationship between the imported information and its source

Preservation is necessary so that information stored by RapistOps can be traced back to its origin.

### 3.4 Structure
Structure is the process of transforming imported information into defined RapistOps records and entities.

Structured information may include:

- People
- Reports
- Evidence
- Events
- Cases
- Institutions
- Outcomes
- Sources

Structure should allow information from different sources to be represented consistently without erasing meaningful differences between those sources.

### 3.5 Connect
Connect is the process of representing relationships between records and entities.

Examples include:
    Person <-> Report
    Person <-> Case
    Person <-> Event
    Person <-> Institution
    Case <-> Outcome
    Evidence <-> Claim
    Record <-> Source

Relationships should represent documented or explicitly represented connections rather than automatically treating a relationship as proof of an underlying allegation.

### 3.6 Store
Store is the persistent storage of RapistOps records, entities, relationships, provenance, and other required information.

Volume 1 will use a relational database as the primary persistent storage system.

The database should preserve the structure and relationships established by the preceding stages of the pipeline.

### 3.7 Search
Search allows users to retrieve information stored within RapistOps.

Volume 1 search should provide basic retrieval capabilities for the core records represented by the system.

Search may eventually include:

- Person search
- Case search
- Record search
- Source search
- Relationship search

More advanced search and analysis capabilities belong to later development.

### 3.8 Display
Display is the presentation of stored information to a user.

Volume 1 should provide a basic web interface capable of displaying the records and relationships produced by the core pipeline.

The interface does not need to represent the complete future RapistOps dashboard.

## 4. Core Concepts
Volume 1 is built around several fundamental concepts:

### Source
The origin of information collected by RapistOps.

### Record
A structured representation of information originating from a source.

### Evidence
Information or material associated with a documented claim, event, case, or record.

### Person
A person represented within one or more records.

### Event
A documented occurrence or incident represented within the system.

### Case
A documented investigation, legal proceeding, institutional proceeding, or related matter.

### Institution
An organization or governmental body associated with a record, case, event, or person.

### Outcome
A documented result or status associated with a case, proceeding, investigation, or other record.

### Relationship
A documented connection between two or more entities or records.

### Provenance
Information describing the origin and history of information stored in RapistOps.

## 5. System Components
Volume 1 is organized around the following major components:
Source Layer

Import Layer

Evidence / Provenance Layer

Entity and Record Layer

Relationship Layer

Database

Search / API

Web Application

Each component should have a defined responsibility.

Components should remain separable enough that later versions can expand individual capabilities without requiring the entire system to be redesigned.

## 6. Data Relationships
RapistOps represents information as connected records and entities rather than isolated pieces of data.

The relationship model should be capable of representing connections such as:
Source -> Record
Record -> Person
Record -> Event
Record -> Case
Record -> Institution
Record -> Evidence
Case -> Person
Case -> Institution
Case -> Outcome
Evidence -> Claim
Person -> Person


Relationships must retain enough context to understand what the connection represents.

A relationship should not automatically be interpreted as proof of a claim simply because two entities are connected.

## 7. Evidence and Provenance
Evidence and provenance are foundational concepts in RapistOps.

Information should remain connected to its source and collection context.

The system should distinguish between:

- What a source states
- What a record documents
- What a person reports
- What an investigation establishes
- What a legal proceeding establishes
- What an adjudicated outcome establishes

RapistOps should not transform an allegation into an established fact merely because the allegation has been imported into the system.

Likewise, the absence of a conviction should not cause the existence of a documented report, investigation, proceeding, or other record to disappear.

The system should preserve distinctions between different types of information and outcomes.

## 8. Status and Case State
RapistOps must be capable of representing different documented states without collapsing them into a single outcome.

Examples include:
- Reported
- Investigated
- Charged
- Prosecuted
- Dismissed
- Acquitted
- Convicted


These states represent different documented events or outcomes.

A report is not equivalent to a conviction.

A charge is not equivalent to a conviction.

A dismissal is not equivalent to an acquittal.

An acquittal is not equivalent to a finding that no report or underlying allegation existed.

Volume 1 should establish the data model necessary to preserve these distinctions.

## 9. Search and Retrieval
Volume 1 search is intended to demonstrate that structured information stored by RapistOps can be retrieved by a user.

Initial search capabilities should focus on the core entities and records established by Volume 1.

Search should return enough context for the user to understand what a result represents and where the information originated.

Advanced analysis, ranking, automated correlation, and large-scale discovery are outside the initial search implementation.

## 10. V1 Boundaries
Volume 1 intentionally does not attempt to implement the entire RapistOps Master Architecture.

The following remain outside the initial implementation unless required by the V1 pipeline:

- Large-scale automated collection
- Extensive source coverage
- Complex automated entity resolution
- Advanced graph analysis
- Large-scale change detection
- Automated alerts
- Production-scale deployment
- Distributed architecture
- Independent graph database
- Large-scale search infrastructure
- Advanced analytics
- Full security and access-control architecture
- Full operational infrastructure

These capabilities may be addressed in later versions when their requirements become clear.

Volume 1 should remain a small, complete vertical slice rather than a partial implementation of the entire long-term system.

## 11. Future Expansion
The Volume 1 architecture establishes foundations that can later support the larger RapistOps system.

Future versions may expand:
- Source collection
- Evidence handling
- Entity resolution
- Relationship analysis
- Case tracking
- Temporal history
- Geographic context
- Search
- APIs
- Web application capabilities
- Automation
- Data quality and verification
- Security and privacy
- Deployment
- Scale
- Source ecosystem coverage

Future capabilities should be added when their requirements are understood rather than being prematurely implemented in Volume 1.

## 12. Architectural Principle
RapistOps should be built around the principle that:
**The system connects documented information without erasing the distinctions between sources, claims, records, relationships, and outcomes.**

The architecture should make information more connected and traceable while preserving the context necessary to understand what each record actually represents.