# RapistOps — Master Architecture

**Project:** RapistOps  
**Version:** 0.1.0  
**Status:** Long-term architecture

## 1. System Identity
RapistOps is a public-source accountability intelligence system designed to collect, preserve, structure, connect, search, and analyze information relating to documented reports, records, people, events, cases, institutions, evidence, and outcomes.

The system is designed around the idea that relevant information may exist across many disconnected sources.

RapistOps provides infrastructure for connecting those records while preserving their provenance, context, status, and history.

The Master Architecture describes the long-term system.

It is not a statement that every component will exist in Version 0.1.0.

# 2. Core Problem
Information relevant to accountability may be distributed across many independent systems and sources.

Examples include:
- Police departments
- Courts
- Prosecutors and district attorneys
- Schools and educational institutions
- Employers and organizations
- Public registries
- Government databases
- Public documents
- Public web sources
- Authorized APIs and feeds
- User-submitted records

These sources may use different identifiers, terminology, formats, structures, and levels of detail.

The same person, event, or case may therefore appear across multiple records without those records being connected.

The central architectural problem is:
**How can information existing across disconnected sources be collected, preserved, connected, searched, and understood as a coherent documented record?**

# 3. Architectural Goal
The long-term goal of RapistOps is to create a system capable of transforming fragmented information into a connected, traceable information network.

The system should be capable of:
    Collect
    Preserve
    Structure
    Connect
    Track
    Search
    Analyze
    Present

Each stage should preserve the information required by the stages that follow.

# 4. Master System Architecture
                                      RAPISTOPS
                    Public-Source Accountability Intelligence System
                                              │
                                              ▼
                              ┌──────────────────────────┐
                              │     SOURCE ECOSYSTEM     │
                              │                          │
                              │ Police / Courts / DAs    │
                              │ Institutions / Schools   │
                              │ Registries / Public DBs  │
                              │ Public Web / Documents   │
                              │ Survivor/User Reports    │
                              └────────────┬─────────────┘
                                           │
                                           ▼
                              ┌──────────────────────────┐
                              │   COLLECTION & INGESTION  │
                              │                          │
                              │ APIs / Scrapers / Import │
                              │ Validation / Normalizing │
                              │ Deduplication            │
                              └────────────┬─────────────┘
                                           │
                                           ▼
                              ┌──────────────────────────┐
                              │      EVIDENCE CORE       │
                              │                          │
                              │ Evidence / Documents     │
                              │ Reports / Records        │
                              │ Source / Provenance      │
                              │ Collection History       │
                              └────────────┬─────────────┘
                                           │
                         ┌─────────────────┼─────────────────┐
                         │                 │                 │
                         ▼                 ▼                 ▼
                ┌────────────────┐ ┌───────────────┐ ┌────────────────┐
                │     PEOPLE     │ │    EVENTS     │ │  INSTITUTIONS  │
                │                │ │               │ │                │
                │ Victims        │ │ Incidents     │ │ Police         │
                │ Reported       │ │ Investigations│ │ Courts         │
                │ Accused        │ │ Cases         │ │ DA Offices     │
                │ Charged        │ │ Proceedings   │ │ Schools        │
                │ Convicted      │ │ Outcomes      │ │ Organizations  │
                └───────┬────────┘ └───────┬───────┘ └───────┬────────┘
                        │                  │                 │
                        └──────────────────┼─────────────────┘
                                           │
                                           ▼
                              ┌──────────────────────────┐
                              │    RELATIONSHIP GRAPH    │
                              │                          │
                              │ Person ↔ Person          │
                              │ Person ↔ Event           │
                              │ Person ↔ Institution     │
                              │ Evidence ↔ Claim         │
                              │ Case ↔ Outcome           │
                              │ Source ↔ Record          │
                              └────────────┬─────────────┘
                                           │
                         ┌─────────────────┼─────────────────┐
                         │                 │                 │
                         ▼                 ▼                 ▼
                ┌────────────────┐ ┌───────────────┐ ┌────────────────┐
                │  STATUS /      │ │   TEMPORAL    │ │   GEOGRAPHIC   │
                │  CASE STATE    │ │    HISTORY    │ │     CONTEXT    │
                │                │ │               │ │                │
                │ Reported       │ │ What changed? │ │ Area / Region  │
                │ Investigated   │ │ When?         │ │ Jurisdiction   │
                │ Charged        │ │ What existed  │ │ Publicly       │
                │ Dismissed      │ │ previously?   │ │ available      │
                │ Acquitted      │ │ What exists   │ │ location data  │
                │ Convicted      │ │ now?          │ │                │
                └───────┬────────┘ └───────┬───────┘ └───────┬────────┘
                        │                  │                 │
                        └──────────────────┼─────────────────┘
                                           │
                                           ▼
                              ┌──────────────────────────┐
                              │    SEARCH & ANALYSIS     │
                              │                          │
                              │ Name / Entity Search     │
                              │ Evidence Search          │
                              │ Case Search              │
                              │ Relationship Search      │
                              │ Timeline Search          │
                              │ Geographic Search        │
                              │ Cross-source Analysis    │
                              └────────────┬─────────────┘
                                           │
                                           ▼
                              ┌──────────────────────────┐
                              │        DASHBOARD         │
                              │                          │
                              │ Person View              │
                              │ Evidence View             │
                              │ Relationship Graph        │
                              │ Case / Timeline View      │
                              │ Geographic View           │
                              │ Source View               │
                              │ Change / Update View      │
                              └────────────┬─────────────┘
                                           │
                                           ▼
                              ┌──────────────────────────┐
                              │           APIs           │
                              │                          │
                              │ Data API                  │
                              │ Search / Query API        │
                              │ Graph API                 │
                              │ Integration Interfaces    │
                              └────────────┬─────────────┘
                                           │
                                           ▼
                              ┌──────────────────────────┐
                              │     AUTOMATION LAYER     │
                              │                          │
                              │ Scheduled Collection      │
                              │ Change Detection          │
                              │ Data Processing           │
                              │ Source Updates            │
                              │ Alerts / Notifications    │
                              └────────────┬─────────────┘
                                           │
                                           └───────────────┐
                                                           ▼
                                                   SOURCE ECOSYSTEM


        ╔══════════════════════════════════════════════════════════════════╗
        ║                    ENGINEERING FOUNDATION                       ║
        ║                                                                  ║
        ║ Git • Tests • CI/CD • Containers • Deployment • Logging        ║
        ║ Security • Configuration • Backups • Observability             ║
        ╚══════════════════════════════════════════════════════════════════╝

# 5. Source Ecosystem
The Source Ecosystem represents the external systems and information sources from which RapistOps may obtain information.

Potential source categories include:
- Government records
- Police records
- Court records
- Prosecutorial records
- Institutional records
- Public registries
- Public databases
- Public websites
- Public documents
- Authorized APIs
- Authorized feeds
- User-submitted information

RapistOps should only interact with sources through methods that are publicly available, authorized, or otherwise lawfully accessible.

The source layer should preserve information about the source itself so that downstream records retain provenance.

# 6. Collection and Ingestion
The Collection and Ingestion layer moves information from external sources into RapistOps.

Possible collection mechanisms include:
- API clients
- Authorized web collection
- Document imports
- Structured data imports
- Manual imports
- Authorized feeds

The ingestion process may include:
    Acquire
    Validate
    Normalize
    Deduplicate
    Preserve

Collection mechanisms should remain separate from the underlying data model where practical.

This allows new source types to be introduced without redesigning the entire system.

# 7. Evidence Core
The Evidence Core is responsible for preserving the information entering the system.

It provides the foundation for:
- Records
- Documents
- Reports
- Evidence
- Sources
- Provenance
- Collection history

The Evidence Core should preserve enough information to determine:
- Where information originated
- What was collected
- When it was collected
- How it entered the system
- What record it belongs to
- What later changes occurred

The Evidence Core should not silently replace historical information when a source changes.

# 8. People
People are entities represented within RapistOps records.

The system may represent different roles associated with a record, including:
- Survivors
- Victims
- Reported persons
- Accused persons
- Charged persons
- Convicted persons
- Witnesses
- Officials
- Investigators
- Attorneys
- Institutional personnel
- Other documented participants

A person's role in one record should not automatically determine their role in every other record.

Person identity and entity resolution are separate architectural concerns from the existence of individual records.

# 9. Events
Events represent documented occurrences relevant to the information represented by the system.

Possible events include:
- Reported incidents
- Investigations
- Arrests
- Charges
- Court proceedings
- Institutional proceedings
- Decisions
- Other documented developments

Events should retain their relationship to their source and associated records.

# 10. Cases and Proceedings
A case represents a documented matter that may involve one or more people, events, institutions, records, and outcomes.

Cases may include:
- Criminal cases
- Investigations
- Civil proceedings
- Institutional proceedings
- Administrative matters
- Other documented case types

A case may contain multiple events and multiple documented outcomes over time.

# 11. Institutions
Institutions represent organizations or governmental bodies involved in documented records.

Examples include:
- Police departments
- Courts
- Prosecutor offices
- Schools
- Universities
- Employers
- Organizations
- Government agencies

Institutions may be connected to people, cases, events, records, and sources.

# 12. Relationship Graph
The Relationship Graph represents explicit connections between entities and records.

Examples include:
    Person <-> Person
    Person <-> Event
    Person <-> Case
    Person <-> Institution
    Evidence <-> Claim
    Case <-> Outcome
    Source <-> Record
    Record <-> Record

The graph exists to make relationships discoverable.

A relationship must retain enough context to explain what the relationship means and what source or record supports it.

A connection between two entities must not automatically be interpreted as proof of an allegation.

# 13. Status and Case State
RapistOps must represent different documented states without collapsing them into a single category.

Possible states include:
    Reported
    Investigated
    Charged
    Prosecuted
    Dismissed
    Acquitted
    Convicted

These states may exist at different points in the history of a case.

The system must distinguish:
- The existence of a report
- The content of a report
- The existence of an investigation
- The existence of charges
- The outcome of a proceeding
- The existence of a conviction

A lack of conviction must not cause a documented report or proceeding to disappear from the system.

Likewise, a report must not automatically be represented as a proven fact.

# 14. Temporal History
RapistOps must be capable of representing change over time.

The system should be able to answer questions such as:
- When was information collected?
- When did a record appear?
- What changed?
- When did it change?
- What information existed previously?
- What information exists now?
- Which source produced the change?

Historical information should not be silently destroyed merely because a newer version exists.

# 15. Geographic Context
Geographic information provides context for records, events, cases, and institutions.

Geographic information may include:
- Country
- State or province
- County
- City
- Jurisdiction
- Region
- Other appropriate geographic areas

The system should use the minimum geographic precision necessary for the documented purpose.

Private or unnecessary precise location information should not be exposed merely because it exists in a source.

# 16. Search and Analysis
The Search and Analysis layer provides methods for finding and understanding connected information.

Potential capabilities include:

### Entity Search
Search for people, institutions, cases, events, and other entities.

### Evidence Search
Search records and source material.

### Relationship Search
Identify documented relationships between entities.

### Timeline Search
Examine information chronologically.

### Geographic Search
Examine information by jurisdiction or region.

### Cross-Source Analysis
Compare and connect information originating from different sources.

Analysis should distinguish between source facts, documented claims, relationships, and conclusions derived from multiple records.

# 17. Dashboard
The dashboard is the primary user-facing interface for exploring RapistOps.

Potential views include:

- Person View
- Evidence View
- Case View
- Timeline View
- Relationship Graph View
- Geographic View
- Source View
- Change / Update View

The dashboard should provide context and provenance alongside information rather than presenting isolated conclusions without their supporting records.

# 18. APIs
The API layer provides programmatic access to RapistOps capabilities.

Potential interfaces include:
- Data API
- Search API
- Query API
- Graph API
- Integration APIs

The API layer should enforce the same data, provenance, security, and privacy rules as the user-facing application.

# 19. Automation Layer
The Automation Layer performs recurring or scheduled system operations.

Potential capabilities include:

- Scheduled collection
- Source monitoring
- Change detection
- Data processing
- Source updates
- Notifications
- Alerts

Automation should operate within the same source-access and privacy boundaries as manual collection.

# 20. Data Quality and Verification
Data quality is a cross-system concern.

RapistOps should eventually provide mechanisms for:
- Validation
- Duplicate detection
- Entity resolution
- Source comparison
- Conflict detection
- Record verification
- Provenance validation
- Data correction

Conflicting records should not automatically be resolved by silently selecting one source as correct.

The system should preserve the existence of meaningful conflicts and identify their sources.

# 21. Security and Privacy
Security and privacy are architectural concerns rather than optional additions.

The system should eventually provide appropriate mechanisms for:
- Authentication
- Authorization
- Access control
- Audit logging
- Data protection
- Secure configuration
- Secrets management
- Abuse prevention
- Backup protection
- Sensitive-data handling

The system should minimize unnecessary collection and exposure of sensitive information.

RapistOps must not be designed as a mechanism for harassment, threats, stalking, doxxing, retaliation, or unauthorized surveillance.

# 22. Engineering Foundation
The Engineering Foundation supports every layer of the system.

It includes:
    Git
    Tests
    CI/CD
    Configuration
    Logging
    Observability
    Containers
    Deployment
    Backups
    Security

These concerns should support the application without becoming coupled to individual domain concepts.

# 23. Architectural Boundaries
RapistOps should maintain clear boundaries between:
    External Sources

    Collection

    Evidence / Provenance

    Domain Records

    Relationships

    Storage

    Search / Analysis

    APIs

    User Interface

No individual component should silently assume responsibilities belonging to another layer.

For example:
- Collection should not determine whether a claim is true.
- Storage should not determine legal outcomes.
- Search should not create facts.
- The dashboard should not replace source provenance.
- A relationship should not automatically become a conclusion.
- Automation should not bypass source-access restrictions.

# 24. Local and Web Deployment
RapistOps is intended to support both local and web-based operation.

The core system should be capable of running locally for development, research, testing, and other appropriate uses.

The same core application can eventually be deployed as a web service.

The architecture should therefore avoid unnecessary coupling between the core data and processing systems and a single deployment environment.

# 25. Long-Term Architectural Direction
The system should begin as a relatively small application and grow as actual requirements emerge.

The initial implementation does not require every component represented in this architecture.

Future expansion should be driven by demonstrated requirements rather than complexity for its own sake.

Potential future infrastructure may include specialized search systems, graph infrastructure, distributed processing, additional services, or other technologies if the scale and requirements justify them.

Such technologies are implementation decisions, not architectural requirements of Version 0.1.0.

# 26. Core Architectural Principles
RapistOps is built around the following principles:

### Preserve the Record
Documented information should remain traceable rather than disappearing because it lacks a particular outcome.

### Preserve Provenance
Information should remain connected to its source and collection history.

### Preserve Context
Records should retain the context necessary to understand what they represent.

### Distinguish Claims From Facts
The existence of a report or allegation is distinct from independently established or adjudicated facts.

### Connect Fragmented Information
Related records should be capable of being connected across sources.

### Preserve History
Changes should be trackable rather than silently overwriting the past.

### Minimize Harm
The system should be designed to reduce unnecessary exposure and prevent misuse.

### Use Lawful Information
Collection and access mechanisms must remain within applicable legal and authorization boundaries.

### Build Incrementally
The architecture describes the long-term system, but implementation should proceed in small, testable stages.

# 27. Relationship Between Master Architecture and Volumes
The Master Architecture defines the long-term system.

Individual development volumes define bounded implementations of portions of that architecture.

Master Architecture
    Volume 1
    Future Volume
    Future Volume
    Future Volume

A volume may implement only a subset of the Master Architecture.

The existence of a component in the Master Architecture does not require that component to exist in the current version.

# 28. Architectural Completion
The Master Architecture is intentionally a living document.

As RapistOps develops, architectural decisions may become more precise.

Changes should be documented rather than silently changing the meaning of existing components.

The architecture should remain a record of what the system is intended to become and why major structural decisions were made.