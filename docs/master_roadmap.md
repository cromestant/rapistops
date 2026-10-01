# RapistOps — Master Roadmap

## Phase 0 — Project Foundation
Goal: Establish the software project and engineering foundation.

- [ ] Define project identity and scope
- [ ] Establish repository structure
- [ ] Configure Python environment
- [ ] Configure project dependencies
- [ ] Establish testing framework
- [ ] Establish Git workflow
- [ ] Establish development configuration
- [ ] Document engineering standards

## Phase 1 — Data Foundation
Goal: Define how RapistOps represents information.

- [ ] Define source
- [ ] Define record
- [ ] Define evidence
- [ ] Define person/entity
- [ ] Define institution
- [ ] Define event
- [ ] Define case
- [ ] Define claim
- [ ] Define relationship
- [ ] Define status
- [ ] Define location
- [ ] Define time
- [ ] Define provenance
- [ ] Define change/history

## Phase 2 — Database
Goal: Persist and organize RapistOps data.

- [ ] Design database schema
- [ ] Implement core tables
- [ ] Implement relationships
- [ ] Implement provenance
- [ ] Implement temporal/history records
- [ ] Implement indexes
- [ ] Implement database migrations
- [ ] Establish backup strategy

## Phase 3 — Source Collection
Goal: Bring information into RapistOps from permitted public and authorized sources.

- [ ] Define source types
- [ ] Define source adapters
- [ ] Implement public API collection
- [ ] Implement permitted web collection
- [ ] Implement document import
- [ ] Implement structured-data import
- [ ] Implement user-submitted information
- [ ] Record collection metadata
- [ ] Preserve original source references
- [ ] Handle collection failures

## Phase 4 — Evidence & Provenance
Goal: Preserve where information came from and what it actually represents.

- [ ] Store source provenance
- [ ] Store original records
- [ ] Store collection timestamps
- [ ] Track evidence versions
- [ ] Distinguish claims from verified records
- [ ] Preserve source context
- [ ] Track evidence relationships
- [ ] Implement evidence integrity checks

## Phase 5 — Entity & Record Processing
Goal: Convert collected information into structured entities and records.

- [ ] Parse records
- [ ] Normalize fields
- [ ] Identify entities
- [ ] Resolve duplicate entities
- [ ] Associate records with entities
- [ ] Associate evidence with claims
- [ ] Associate cases with people
- [ ] Associate institutions with records
- [ ] Preserve uncertainty

## Phase 6 — Case & Status Model
Goal: Represent what happened to a report or case without collapsing different outcomes.

- [ ] Define report state
- [ ] Define investigation state
- [ ] Define charging state
- [ ] Define court/proceeding state
- [ ] Define dismissal state
- [ ] Define acquittal state
- [ ] Define conviction state
- [ ] Define other outcomes
- [ ] Track status changes over time
- [ ] Preserve the distinction between allegation, record, and adjudicated outcome

## Phase 7 — Relationship Graph
Goal: Connect people, records, events, institutions, cases, and evidence.

- [ ] Define graph entities
- [ ] Define relationship types
- [ ] Implement person relationships
- [ ] Implement person/event relationships
- [ ] Implement person/institution relationships
- [ ] Implement evidence/claim relationships
- [ ] Implement case relationships
- [ ] Implement source/record relationships
- [ ] Implement graph queries
- [ ] Implement relationship history

## Phase 8 — Temporal & Change Tracking
Goal: Understand how information changes over time.

- [ ] Track record creation
- [ ] Track record updates
- [ ] Track source changes
- [ ] Detect changes
- [ ] Preserve previous states
- [ ] Build historical timelines
- [ ] Compare record versions
- [ ] Track entity history

## Phase 9 — Geographic Context
Goal: Represent geographic information at appropriate public-source granularity.

- [ ] Define geographic entities
- [ ] Define jurisdictions
- [ ] Associate records with jurisdictions
- [ ] Associate institutions with locations
- [ ] Support region/area information
- [ ] Preserve geographic provenance
- [ ] Support geographic queries

## Phase 10 — Search
Goal: Make the collected information discoverable.

- [ ] Entity search
- [ ] Name search
- [ ] Record search
- [ ] Evidence search
- [ ] Case search
- [ ] Institution search
- [ ] Relationship search
- [ ] Timeline search
- [ ] Geographic search
- [ ] Filter and refinement
- [ ] Search result provenance

## Phase 11 — Analysis
Goal: Allow users to examine connections and patterns in the available records.

- [ ] Cross-source comparison
- [ ] Relationship analysis
- [ ] Timeline analysis
- [ ] Case-history analysis
- [ ] Institutional analysis
- [ ] Evidence/claim analysis
- [ ] Change analysis
- [ ] Data-quality analysis

## Phase 12 — APIs
Goal: Make RapistOps data and capabilities accessible programmatically.

- [ ] Design API architecture
- [ ] Implement data API
- [ ] Implement entity API
- [ ] Implement search API
- [ ] Implement case API
- [ ] Implement evidence API
- [ ] Implement relationship/graph API
- [ ] Implement source API
- [ ] Implement authentication and authorization
- [ ] Implement API documentation

## Phase 13 — Web Application
Goal: Provide a usable interface for interacting with RapistOps.

- [ ] Design application interface
- [ ] Implement search interface
- [ ] Implement entity view
- [ ] Implement evidence view
- [ ] Implement case view
- [ ] Implement timeline view
- [ ] Implement relationship graph view
- [ ] Implement institution view
- [ ] Implement source view
- [ ] Implement change/history view
- [ ] Implement geographic views where appropriate

## Phase 14 — Automation
Goal: Reduce repetitive collection and processing work.

- [ ] Scheduled source collection
- [ ] Automated parsing
- [ ] Automated normalization
- [ ] Automated deduplication
- [ ] Automated change detection
- [ ] Automated processing pipelines
- [ ] Source health monitoring
- [ ] Alerts for relevant source changes

## Phase 15 — Data Quality & Verification
Goal: Make the system's information reliable, traceable, and understandable.

- [ ] Validation rules
- [ ] Duplicate detection
- [ ] Conflict detection
- [ ] Source reliability metadata
- [ ] Provenance verification
- [ ] Data-quality reporting
- [ ] Human review workflows
- [ ] Correction workflows

## Phase 16 — Security & Privacy
Goal: Protect the system, its users, and information that should not be exposed.

- [ ] Authentication
- [ ] Authorization
- [ ] Access controls
- [ ] Secure configuration
- [ ] Secret management
- [ ] Audit logging
- [ ] Data protection
- [ ] Abuse prevention
- [ ] Privacy controls
- [ ] Appropriate data-retention rules

## Phase 17 — Testing & Reliability
Goal: Make RapistOps dependable as the system grows.

- [ ] Unit tests
- [ ] Integration tests
- [ ] Database tests
- [ ] API tests
- [ ] Collection tests
- [ ] Data validation tests
- [ ] End-to-end tests
- [ ] Regression tests
- [ ] Failure/recovery testing
- [ ] Performance testing

## Phase 18 — Deployment & Operations
Goal: Make RapistOps deployable and maintainable.

- [ ] Containerize application
- [ ] Establish deployment environments
- [ ] Configure CI/CD
- [ ] Configure production database
- [ ] Configure logging
- [ ] Configure monitoring
- [ ] Configure backups
- [ ] Configure recovery procedures
- [ ] Establish release process

## Phase 19 — Scale
Goal: Support substantially larger datasets and source ecosystems.

- [ ] Optimize database performance
- [ ] Optimize collection pipelines
- [ ] Improve search performance
- [ ] Improve graph queries
- [ ] Introduce specialized search infrastructure if required
- [ ] Introduce specialized graph infrastructure if required
- [ ] Scale workers
- [ ] Scale API services
- [ ] Scale storage

## Phase 20 — Mature Source Ecosystem
Goal: Expand the breadth of legally accessible information sources.

- [ ] Expand public-record integrations
- [ ] Expand government data integrations
- [ ] Expand court-record sources
- [ ] Expand institutional sources where legally accessible
- [ ] Expand public registries
- [ ] Expand public-document sources
- [ ] Expand authorized data feeds
- [ ] Establish source monitoring and maintenance

## Phase 21 — Mature Platform
Goal: Bring the complete RapistOps system together into a mature accountability intelligence platform.

- [ ] Unified search
- [ ] Unified entity profiles
- [ ] Unified evidence system
- [ ] Unified case timelines
- [ ] Unified relationship graph
- [ ] Cross-source analysis
- [ ] Historical change tracking
- [ ] Public-source monitoring
- [ ] APIs and integrations
- [ ] Web application
- [ ] Operational infrastructure
- [ ] Long-term maintenance and governance