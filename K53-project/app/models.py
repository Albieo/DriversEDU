from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LICENCE_TYPE_CHOICES = (
        ("Learner", "Learners Licence Student"),
        ("Driver", "Drivers Licence Student"),
    )

    LICENCE_CODE_CHOICES = (
        ("", "Licence Codes"),
        (1, "Code A"),
        (2, "Code B"),
        (3, "Code C"),
        (4, "Code E"),
    )

    licence_type = models.CharField(max_length=50, choices=LICENCE_TYPE_CHOICES, null=True, blank=True)
    licence_code = models.IntegerField(choices=LICENCE_CODE_CHOICES, null=True, blank=True)


class TestNumber(models.Model):
    test = models.IntegerField(default=0)

    def __str__(self):
        return str(self.test)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    test_number = models.ForeignKey(TestNumber, related_name='test_no', on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text} ({"Correct" if self.is_correct else "Incorrect"})'



class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} selected {self.selected_choice} for {self.question}'

