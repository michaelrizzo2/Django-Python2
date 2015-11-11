from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .forms import PostForm
from .models import Post

# Create your views here.
#post_list=lambda request: render(request,'myblog/post_list.html',{}
def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'myblog/post_list.html',{'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'myblog/post_detail.html',{'post':post})

def post_new(request):
    form=PostForm()
    return render(request,'myblog/post_edit.html',{"form":form})

