Проект на Джанго

1 Чтобы приложение заработало как надо в config/settings указать в DATABASES свои данные

2 активировать виртуальное окружение

CRUD

create: <название модели>.objects.create( field='value', field2 = value )

<название модели>.objects.all() - получение всеч данных retrieve: <название модели>.objects.get(pk=1) - получение данных по определенным критериям

delete: obj = <название модели>.objects.get(field=value) obj.delete

update: функция update если хотите обновить несколько объектов <название модели>.objects.get(field='value').update(field='new value')

обращение к атрибуту если хотите обновить 1 объект item.field = 'new field' item.save()







синтаксис создание superuser
 python manage.py createsuperuser - вводим эту команду в терминале когда активна витрю окр
Username (leave blank to use 'hello'): admin  имя юзера
Email address: он не обьязателен
Password: пароль
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: если пароль слишком прост то просит потверждение
Superuser created successfully. усрешно создан юзер
