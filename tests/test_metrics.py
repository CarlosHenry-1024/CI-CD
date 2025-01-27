from app.metrics import calculate_accuracy

def test_calculate_accuracy():
    assert calculate_accuracy([1, 0, 1], [1, 0, 1]) == 1.0
    assert calculate_accuracy([1, 0, 1], [1, 1, 0]) == 0.3333333333333333