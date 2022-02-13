from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import date
from . models import Post,Author,Tag
from .forms import CommentForm
from django.views import View
# Create your views here.


def startpage(request):

    latest_posts=Post.objects.all().order_by("-date")[:3]


    #sorted_posts=sorted(Posts,key=getdate)
    #latest_posts=sorted_posts[-3:]

    print(latest_posts)

    return render(request,'blog/index.html' ,{

        'posts':latest_posts
    })


def post(request):
  Posts=Post.objects.all()
  return render(request,'blog/all-posts.html',{
    'all_posts' : Posts
  })



class SinglePostView(View):

        def get(self,request,slug):

          post=Post.objects.get(slug=slug)

          context={
            "post":post,
            "tags":post.tag.all(),
            "form":CommentForm(),
            "comments":post.comments.all().order_by("-id")

          }

          return render(request,"blog/post-detail.html",context)





        def post(self,request,slug):
            form=CommentForm(request.POST)
            post=Post.objects.get(slug=slug)

            #print("slug is ",slug)

            if(form.is_valid()):
              comment=form.save(commit=False)
              comment.post=post
              comment.save()
              return HttpResponseRedirect(reverse("content",args=[slug]))

           
            context={
              "post":post,
              "tags":post.tag.all(),
              "form":CommentForm(),
              "comments":post.comments.all().order_by("-id")


            }

            return render(request,"blog/post-detail.html",context)

            



