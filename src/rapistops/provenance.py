from dataclasses import dataclass

@dataclass
class Provenance:
    source_id: int
    collected_at: str 
    collection_method: str
    source_reference: str
    collection_context: str