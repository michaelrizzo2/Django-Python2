from django.http import HttpResponse
from .models import Question
from django.shortcuts import render 
#from django.template import RequestContext,loader
# Create your views here.

#def index(request):
#    return HttpResponse("Hello World you are at the polls index")
#def index(request):
#    latest_question_list=Question.objects.order_by('-pub_date')[:5]
#    template=loader.get_template('mypoll/index.html')
#    context=RequestContext(request,{'latest_question_list':latest_question_list,})
#    return HttpResponse(template.render(context))

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request,'mypoll/index.html',context)

detail =lambda request,question_id : HttpResponse("You are looking at question %s" % question_id) 

results=lambda request,question_id :HttpResponse("You are looking at the results of question %s" % question_id)

vote=lambda request,question_id:HttpResponse("You are voting on question %s" % question_id) 
