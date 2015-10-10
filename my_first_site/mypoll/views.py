from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World you are at the polls index")

detail =lambda request,question_id : HttpResponse("You are looking at question %s" % question_id) 

results=lambda request,question_id :HttpResponse("You are looking at the results of question %s" % question_id)

vote=lambda request,question_id:HttpResponse("You are voting on question %s" % question_id) 
