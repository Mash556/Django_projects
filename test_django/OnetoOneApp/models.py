from django.db import models

# Create your models here.

class Brain(models.Model):
    iq = models.IntegerField()
    weignt = models.IntegerField()

class Human(models.Model):
    SEX = (
        ('male', 'мужской'),
        ('female', 'женский'),
        ('think', 'неопределённый'),
        ('fight helicopter', 'боевой вертолет')
    )
    name = models.CharField(max_length=50, default='John')
    sex = models.CharField(max_length=20, choices=SEX) # choices - он позвольяет 
    brain = models.OneToOneField(
        Brain, 
        on_delete=models.CASCADE,
        related_name='human'  # обратная связь
        )
    


# brain1 = Brain.objects.create(iq=110, weignt=2)
# human1 = Human.objects.create(sex='male', brain=brain1)
# human1.brain
# <Brain: Brain object (1)>
# brain1.human
# <Human: Human object (1)>
# brain1.human.all()