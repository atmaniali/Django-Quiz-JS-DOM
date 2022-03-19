from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        ordering = ["id"]
    
    
class Category(BaseModel):
    title = models.CharField(max_length= 255, verbose_name = _("title"))   
    
    def __str__(self) -> str:
        return f"{self.title}" 
    
    class Meta :
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        
class Quizzes(BaseModel):
    title = models.CharField(max_length=255, default= _('New Quiz'), verbose_name= _('Quiz Title'))
    category = models.ForeignKey(Category, on_delete= models.DO_NOTHING, related_name="quiz")
    
    def __str__(self):
        return f"{self.title}"
    class Meta :
        verbose_name = _("Quiz")
        verbose_name_plural = _('Quizzes')
        
class Question(BaseModel):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    ) 
    
    TYPE = (
        (0, _('Multiple Choice')),
    )   
    
    
    title = models.CharField(max_length= 255, verbose_name = _('Title'))
    technique = models.IntegerField(choices= TYPE, default = 0, verbose_name= _("Type of Question"))
    difficulty = models.IntegerField(choices= SCALE, default = 0, verbose_name = 'Difficulty')
    quiz = models.ForeignKey(Quizzes, on_delete=models.DO_NOTHING, related_name = 'question', default = 1) 
    is_active = models.BooleanField(default = False, verbose_name = _("Active Status"))   
    
    class Meta :
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')  
    
    def __str__(self):
        return self.title     
            
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete= models.DO_NOTHING, related_name = 'answer')
    answer_text = models.CharField(max_length= 255, verbose_name = _('Answer Text'))
    is_right = models.BooleanField(default = False, verbose_name= _('is Right'))
    
    class Meta :
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')  
    
    def __str__(self):
        return self.answer_text   