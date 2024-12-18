from teacher_pytests.class_teacher import Teacher, DisciplineTeacher

'''без использования фикстуры'''


def test_teacher_init():
    teacher = Teacher('test_name', 'test_education', 99)
    assert len(Teacher.teacher_dict) == 1
    assert Teacher.teacher_dict == {'test_name': ['test_education', 99]}


'''c фикстурой!!'''


def test_teacher_init_1(teacher):
    assert len(Teacher.teacher_dict) == 1
    assert Teacher.teacher_dict == {'test_name': ['test_education', 99]}


def test_get_name(teacher):
    assert teacher.get_name() == 'test_name'


def test_get_education(teacher):
    assert teacher.get_education() == 'test_education'


def test_get_experience(teacher):
    assert teacher.get_experience() == 99


def test_get_teacher_data(teacher):
    assert teacher.get_teacher_data() == 'Имя: test_name. Образование: test_education. Опыт работы: 99 (года/лет)'


def test_add_mark(teacher):
    assert teacher.add_mark('test_student', 5) == 'test_name поставил оценку: 5 студенту: test_student'


def test_remove_mark(teacher):
    assert teacher.remove_mark('test_student', 5) == 'test_name удалил оценку: 5 студенту: test_student'


def test_give_a_consultation(teacher):
    assert teacher.give_a_consultation('TEST') == 'test_name провел консультацию в классе: TEST'


def test_display_teacher_data(teacher):
    assert Teacher.display_teacher_data() == 'Данные успешно выведены'


def test_set_experience(teacher):
    assert teacher.set_experience(100) == 'Изменен опыт работы на 100 лет'


def test_fire_teacher(teacher):
    assert teacher.fire_teacher() == 'Учитель test_name  был уволен'
    assert teacher.fire_teacher() == 'Учителя test_name  уже уволили'
    assert Teacher.teacher_dict == {}
    assert len(Teacher.teacher_dict) == 0


def test_discipline_teacher_init(discipline_teacher):
    assert len(DisciplineTeacher.discipline_teacher_dict) == 1
    assert DisciplineTeacher.discipline_teacher_dict == {'new_name': ['test_discipline', 'test_job_title']}


def test_get_discipline(discipline_teacher):
    assert discipline_teacher.get_discipline() == 'test_discipline'


def test_get_job_title(discipline_teacher):
    assert discipline_teacher.get_job_title() == 'test_job_title'


def test_get_discipline_teacher_data(discipline_teacher):
    assert discipline_teacher.get_teacher_data() == 'Имя: new_name. Образование: new_education. Опыт работы: 66 (года/лет)\nПредмет test_discipline. Должность test_job_title'

def test_set_job_title(discipline_teacher):
    assert discipline_teacher.set_job_title('new_job_title') == 'new_job_title'

def test_give_consultation(discipline_teacher):
    assert discipline_teacher.give_a_consultation('TEST') == 'new_name провел консультацию в классе TEST\nПо предмету test_discipline как test_job_title'


def test_fire_discipline_teacher(discipline_teacher):
    assert discipline_teacher.fire_discipline_teacher() == 'Учитель new_name по дисциплине test_discipline  был уволен'
    assert discipline_teacher.fire_discipline_teacher() == 'Учителя new_name по дисциплине test_discipline уже уволили'
    assert DisciplineTeacher.discipline_teacher_dict == {}