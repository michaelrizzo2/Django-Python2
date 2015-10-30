from django.shortcuts import render

# Create your views here.
post_list=lambda request: render(request,'myblog/post_list.html',{})
