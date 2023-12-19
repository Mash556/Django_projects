 давайте выполним каждый из ваших пунктов в Django shell:

     Запустите Django shell
python manage.py shell


     Импорт модели
from your_app.models import Person

     1. Получение всех объектов модели

Person.objects.all()


     2. Фильтрация объектов по условиям

Person.objects.filter(age__lt=30)


     3. Использование связанных моделей с related_name и related_query_name
     Предположим, у Person есть связь OneToOne с моделью Address с related_name='address'
person_with_address = Person.objects.get(name='John')
address = person_with_address.address  # Используем related_name

     4. Создание новых объектов
new_person = Person.objects.create(name='Alice', age=25)

     5. Обновление существующих объектов
person_to_update = Person.objects.get(name='Alice')
person_to_update.age = 26
person_to_update.save()

     6. Удаление объектов
person_to_delete = Person.objects.get(name='Alice')
person_to_delete.delete()

     7. Использование агрегирующих функций
from django.db.models import Count, Sum, Avg
total_people = Person.objects.count()
average_age = Person.objects.aggregate(average_age=Avg('age'))

     8. Использование операторов сравнения
people_with_age_gt_30 = Person.objects.filter(age__gt=30)
name_contains_j = Person.objects.filter(name__contains='J')

     9. Работа с ManyToManyField и OneToOneField
     Предположим, у Person есть связь ManyToMany с моделью Hobby
person_with_hobbies = Person.objects.get(name='John')
hobbies = person_with_hobbies.hobbies.all()

     10. Завершение работы в оболочке
exit()