from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views import generic
from .models import Question,Choice
from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
#from django.template import RequestContext,loader
# Create your views here.

#def index(request):
#    return HttpResponse("Hello World you are at the polls index")
#def index(request):
#    latest_question_list=Question.objects.order_by('-pub_date')[:5]
#    template=loader.get_template('mypoll/index.html')
#    context=RequestContext(request,{'latest_question_list':latest_question_list,})
#    return HttpResponse(template.render(context))

#def index(request):
#    latest_question_list=Question.objects.order_by('-pub_date')[:5]
#    context={'latest_question_list':latest_question_list}
#    return render(request,'mypoll/index.html',context)

#detail =lambda request,question_id : HttpResponse("You are looking at question %s" % question_id) 

#def detail(request,question_id):
#    try:
#        question=Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request,'mypoll/details.html',{'question':question})

#def detail(request,question_id):
#    question=get_object_or_404(Question,pk=question_id)
#    return render(request,'mypoll/details.html',{'question':question})


#results=lambda request,question_id :HttpResponse("You are looking at the results of question %s" % question_id)

#vote=lambda request,question_id:HttpResponse("You are voting on question %s" % question_id) 

#Final version of vote view 
def vote(request,question_id):
    p=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'mypoll/details.html',{'question':p,'error_message':"you didn't select a choice",})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('mypoll:result',args=(p.id,)))

#Final version of results view
#def result(request,question_id):
#    question=get_object_or_404(Question,pk=question_id)
#    return render(request,'mypoll/results.html',{'question':question})
#We will implement the generic views built into Django

class IndexView(generic.ListView):
    template_name='mypoll/index.html'
    context_object_name='latest_question_list'

    #get_queryset=lambda self : Question.objects.order_by('-pub_date')[:5]
    #This will return the last five published questions,this does not include future questions
    get_queryset=lambda self:Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name='mypoll/details.html'

class ResultsView(generic.DetailView):
    model=Question
    template_name='mypoll/results.html'
