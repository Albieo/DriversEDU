from django.contrib import admin

from .models import Role, Category, Question, Choice, Answer, TestNumber


admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)
admin.site.register(TestNumber)
