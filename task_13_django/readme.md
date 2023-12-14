<h1> Модели Django: типы полей и их опции. Работа с миграциями. Связи между таблицами. <h1>


1) Прежде чем как все начать создайте свое виртуальное окружение командой:
python3 -m venv venv


2) Затем активируйте своё виртуальное окружение командой:
sourse venv/bin/activate

3) Теперь зайдите в config.settings в DATABASES укажите свой USER и PASSWORD
   затем в psql создайте такойже базу данных как под ключом NAME

4) Создайте необходимые миграции для данных моделей с помощью команды
python manage.py makemigrations

7) Примените миграции к базе данных с помощью команды 
python manage.py migrate

8) Теперь вы можете проводдить разные операции с таблицами Student и Сourse
   Зайдите в консоль питона с помощью команды 
   python3 manage.py shell

9) Можете тут использовать CRUD
>>> from student.models import Student, Course (сперва надо импортировать наши классы(базы данных))
10) создаем объект от Student с помощь команды сreate синтаксис выглядит так:
>>> student1 = Student.objects.create(first_name='student1_first_name', last_name='student1_last_name', email='user@example.com', age=18)
>>> student2 = Student.objects.create(first_name='student2_first_name', last_name='student2_last_name', email='user2@example.com', age=19)
>>> student3 = Student.objects.create(first_name='student3_first_name', last_name='student3_last_name', email='user3@example.com', age=20)

11) Теперь создадим объект от Сourse  с помощь команды сreate синтаксис выглядит так:
course1 = Course.objects.create(name='course1_name', description='course1_description')

12) важно свызь мы передаем другим ключевым словом set синтаксис выглядит так:
>>> course1.students.set([student1, student2])
>>> student1.courses.all() # если хотите просмотреть то что содержится внутри student1

13) Надо прочитать то что мы внесли с помощью командами all() u get()
<название модели>.objects.all()   # чтобы прочитать все данные 

<название модели>.objects.get(pk=1)  # получение данных по определенным критериям

14) время обновлять наши столбцы или строки
15) если хотите обновить 1 объект
>>> student1 = Student.objects.get(pk=1) # получаем по id к примеру 1
>>> student1.age = 59 # выбираем нужный атрибут
>>> student1.save() # сохряняем наши изменение

16) функция update если хотите обновить несколько объектов
  <название модели>.objects.get(field='value').update(field='new value')

17) функция delete 
1) К примеру удаляем объект от Student
>>> student1 = Student.objects.get(pk=1) # для начало нужно получить данные с помощью get запроса
>>> student1.delete()  # теперь можно удалять
2) с Course точно такие же операции
>>> course1 = Course.objects.get(pk=1)
>>> course1.delete()


<h1> Проверим всё в сервере <h1>

1) Cоздайте супер юзера с командой 
    python manage.py createsuperuser
    После выполнения этой команды, система попросит вас ввести имя пользователя (Username), 
    адрес электронной почты (Email address оно может оставаться пустым), 
    и пароль (Password) для нового суперпользователя.

2) Запустите сервер в терминале с помощью команды 
    python3 manage.py runserver
    Скопируйте свой http адрес в терминале и откройте его в браузере
    добавьте в него конец /admin и зарегистрируйтесь с теми данными когда создавали супер юзера
    теперь тут вам доступен CRUD  




<h1> В postgresql вы можете увидеть вашу базу данных и таблицы <h1>

1) Перейдите в postgresql с помощью команды psql таблицы

2) Теперь перейдите в таблицу которого создали в DATABASES должно быть task_13_django

3) В нем теперь будут храниться такие таблицы как 
    student_student (модель который существует под именем Student)
    student_course (модель который существует под именем Course)
    student_course_students  (Это третья связная таблица )

4) Проверьте содержимое своей таблицы (или моделья Student) с помощью команды 
   select * from student_student;
   Проверьте содержимое своей таблицы (или моделья Course) с помощью команды 
   select * from student_course;