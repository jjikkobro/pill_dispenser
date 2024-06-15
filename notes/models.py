from django.db import models
from django.shortcuts import reverse,redirect
from django.contrib.auth.models import User
# Create your models here.

REPEAT_CHOICES = (
    ('daily', '매일'),
    ('mon', '월'),
    ('tue', '화'),
    ('wed', '수'),
    ('thu', '목'),
    ('fri', '금'),
    ('sat', '토'),
    ('sun', '일'),
)
CONTAINER_CHOICES =(
    (1, '1'),
    (2, '2'),
    (3, '3')
)


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    medicine = models.CharField(max_length=100, null=False)
    dosing_time = models.TimeField(null=False, default='08:00')
    repetition = models.TextField(default='daily')
    container = models.IntegerField(null=True)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.medicine

    def get_finish_item_url(self):
        return reverse("finish-note-item",kwargs={
            'id':self.id
        })
    def get_recover_item_url(self):
        return reverse("recover-note-item",kwargs={
            'id':self.id
        })
    def get_delete_item_url(self):
        return reverse("delete-note-item",kwargs={
            'id':self.id
        })
    def get_repeat_display(self):
        repeat_dict = dict(REPEAT_CHOICES)
        repeats = self.repeat.split(',')
        return ', '.join([repeat_dict[repeat] for repeat in repeats])