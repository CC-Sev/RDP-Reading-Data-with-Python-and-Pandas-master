def test_budget():
    assert movies.loc[:, 'budget'].min() == 105_000_000.0
