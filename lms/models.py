from django.core.exceptions import SuspiciousOperation
from django.db.models import (Model,
                              CharField,
                              ForeignKey, CASCADE, DO_NOTHING, IntegerField,
                              )
class Curator(Model):
    first_name = CharField(max_length=20)
    def __str__(self):
        return "курат. "+self.first_name

class Direction(Model):
    name = CharField(max_length=20)
    curator = ForeignKey(Curator,
                         on_delete=CASCADE,
                         related_name='direction')
class Group(Model):
    fancy_number = CharField(max_length=20)
    capacity = IntegerField(default=3)
    direction = ForeignKey(Direction,
                           on_delete=CASCADE,
                           related_name='group')

class Student(Model):
    fio = CharField(max_length=20)
    group = ForeignKey(Group,
                       on_delete=CASCADE,
                       related_name='student')
    def save(self):
        print('potato')
        if self.group.student.count() < self.group.capacity:
            super().save()
        else:
            raise SuspiciousOperation('safd')


