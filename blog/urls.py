from django.urls import path
from . import views 

urlpatterns = [
        path('',views.startpage,name='startpage'),
        path('posts',views.post,name='posts-page'),
        path('post/<slug:slug>',views.SinglePostView.as_view(),
        name='content')
]
