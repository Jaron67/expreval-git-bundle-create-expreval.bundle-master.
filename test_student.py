import student

def test_student_info():
    assert student.matriculation_number() == '1234567'
    assert student.first_name() == 'John'
    assert student.last_name() == 'Doe'

if __name__ == "__main__":
    test_student_info()
    print("test_student.py passed")
