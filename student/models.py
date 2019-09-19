from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from teacher.models import Classroom

# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    classrooms = models.ManyToManyField(
        Classroom,
        blank = True,
        related_name = 'students'
    )

class Item(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete = models.CASCADE,
    )
    dateTimeAdded = models.DateTimeField(
        auto_now_add = True,
    )
    title = models.CharField(
        max_length = 256,
        blank = True,
    )
    description = models.TextField(
        max_length = 1024,
        blank = True,
    )
    itemType = models.ForeignKey(
        ContentType,
        limit_choices_to = models.Q(app_label = 'student', model = 'link') | models.Q(app_label = 'student', model = 'gallery'),
        on_delete = models.CASCADE,
    )
    itemId = models.PositiveIntegerField()
    item = GenericForeignKey('itemType', 'itemId')

class Link(models.Model):
    url = models.URLField(
        max_length = 512,
    )

class Gallery(models.Model):
    tempLocation = models.CharField(
        max_length = 512,
    )

