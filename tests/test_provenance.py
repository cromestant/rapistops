from rapistops.provenance import Provenance


def test_class_provenance():
    provenance = Provenance(
        source_id=1,
        collected_at="2024-06-01",
        collection_method="Test Method",
        source_reference="Test Reference",
        collection_context="Test Context",
    )

    assert provenance.source_id == 1
    assert provenance.collected_at == "2024-06-01"
    assert provenance.collection_method == "Test Method"
    assert provenance.source_reference == "Test Reference"
    assert provenance.collection_context == "Test Context"