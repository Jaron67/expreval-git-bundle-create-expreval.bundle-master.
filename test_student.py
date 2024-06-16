import student

def test_student_info():
    assert student.matriculation_number() == '00152102'
    assert student.first_name() == 'Jaron'
    assert student.last_name() == 'Saw'

if __name__ == "__main__":
    test_student_info()
    print("test_student.py passed")
