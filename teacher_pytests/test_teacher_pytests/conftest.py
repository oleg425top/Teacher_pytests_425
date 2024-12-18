import pytest

from teacher_pytests.class_teacher import Teacher, DisciplineTeacher

@pytest.fixture()
def teacher():
    Teacher.teacher_dict.clear()
    teacher = Teacher('test_name', 'test_education', 99)
    return teacher