import pytest

from teacher_pytests.class_teacher import Teacher, DisciplineTeacher

@pytest.fixture()
def teacher():
    Teacher.teacher_dict.clear()
    teacher = Teacher('test_name', 'test_education', 99)
    return teacher

@pytest.fixture()
def discipline_teacher():
    DisciplineTeacher.discipline_teacher_dict.clear()
    discipline_teacher = DisciplineTeacher('new_name','new_education', 66, 'test_discipline', 'test_job_title')

