from django.contrib import admin
from . import models

# Register your models here.
class CatAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ['title']


class QuizAdmin(admin.ModelAdmin):
    fields= [
        'title',
        'category'
    ]
    list_display = ['id', 'title']
    
class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right'
    ]    
    
class QuestAdmin(admin.ModelAdmin) :
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
        'updated'
    ] 
    inlines = [AnswerInlineModel, ]   
    
class AnsAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question'
    ]    
      

admin.site.register(models.Category, CatAdmin)
admin.site.register(models.Quizzes, QuizAdmin)
admin.site.register(models.Question, QuestAdmin)
admin.site.register(models.Answer, AnsAdmin)