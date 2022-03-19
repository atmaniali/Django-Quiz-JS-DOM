from django.shortcuts import render
from .models import Question, Answer
import json

# Create your views here.
def getQuestion(request, title):
    dic = {}
    dic1 = {}
    # question = Question.objects.filter(quiz__title = title).order_by('?')[:1]
    # answer = Answer.objects.filter(question = question)
    ques = Question.objects.filter(quiz__title = title).order_by('?')
    li = []
    # methode 01
    # for q in ques :
    #     print(type(q), q.id)
    #     ans = Answer.objects.filter(question = q).values_list('answer_text','is_right')
    #     dic[q.title] = list(ans)
    # methode 02
    for q in ques :
        qu  = q.answer.all().values_list('id','answer_text','is_right') 
        dic1[q.title] = list(qu)   
    # json_object = json.dumps(dic) 
    json_object_1 = json.dumps(dic1) 
    # print(json_object)
    print(json_object_1)
    context = {
            # 'question': question, 
            # 'answer': answer, 
            "dic" : dic, 
            "js" : json_object_1
            }
    return render(request,'quiz/home.html', context)
