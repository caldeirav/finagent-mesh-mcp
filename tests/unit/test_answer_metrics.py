from finagent_mesh.metrics.answer import normalized_exact_match, token_f1


def test_normalized_em():
    assert normalized_exact_match("Hello, World!", "hello world") == 1.0
    assert normalized_exact_match("a", "b") == 0.0


def test_token_f1():
    score = token_f1("market credit risk", "market and credit risk discussed")
    assert 0.0 < score <= 1.0
