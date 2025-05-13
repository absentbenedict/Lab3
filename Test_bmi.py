from Lab2 import bmi  # Assuming bmi.py is inside your lab2 submodule

def test_bmi_under_weight():
    # Example: weight = 50kg, height = 1.8m → BMI = 15.43
    result = bmi.calculate_bmi(1.8, 50)
    assert result == "Under Weight"

def test_bmi_normal_weight():
    # Example: weight = 68kg, height = 1.75m → BMI = 22.2
    result = bmi.calculate_bmi(1.75, 68)
    assert result == "Normal Weight"

def test_bmi_over_weight():
    # Example: weight = 90kg, height = 1.7m → BMI = 31.1
    result = bmi.calculate_bmi(1.7, 90)
    assert result == "Over Weight"
