from BMI import calculate_bmi

def test_underweight():
    assert calculate_bmi(45, 1.75) == -1

def test_normal_weight():
    assert calculate_bmi(68, 1.75) == 0

def test_overweight():
    assert calculate_bmi(90, 1.75) == 1
