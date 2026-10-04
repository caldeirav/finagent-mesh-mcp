from finagent_mesh.clients.open_decision import OpenDecisionClient


def test_mock_systemone_response_shape():
    client = OpenDecisionClient("http://localhost:8000", "http://localhost:8001", mock=True)
    resp = client.decide(
        "choice",
        "revenue risks",
        [{"id": "10-K", "text": "10-K"}, {"id": "10-Q", "text": "10-Q"}],
    )
    assert resp["primitive"] == "choice"
    assert "ranking" in resp and "distribution" in resp
    assert {r["id"] for r in resp["ranking"]} == {"10-K", "10-Q"}
