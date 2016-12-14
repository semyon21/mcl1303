from django.db import models

class Item(models.Model):
    """Тема, которую изучает пользователь"""
    theme = models.CharField(max_length = 100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        """Возвращает строковое представление темы"""
        return self.theme


class Student(models.Model):
    """Ученик"""

    mail = models.EmailField(max_length = 100)
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20) 
    course = models.CharField(max_length = 5, choices = (('V', 'Вокал'), ('T', 'Театр')))
    form = models.IntegerField(choices=((9, 9), (10, 10), (11, 11)))
    part = models.CharField(max_length = 3, choices = (('FM', 'ФМ'), ('CHE', 'ХИМ')))
    
    def __str__(self):
        return self.name + ' ' + self.surname
