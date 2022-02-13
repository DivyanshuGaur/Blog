from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.



class Author(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()


    def full_name(self):
        
        return f'{self.firstname} {self.lastname}'

    def __str__(self) -> str:
        return self.full_name()



class Tag(models.Model):
    caption=models.CharField(max_length=50)



    
    def cap(self):
        
        return f'{self.caption}'

    def __str__(self) -> str:
        return self.cap()



class Post(models.Model):

        title=models.CharField(max_length=100)
        excerpt=models.CharField(max_length=100)
        image=models.ImageField(upload_to="posts",null=True)
        date=models.DateField(auto_now=True)
        slug=models.SlugField(unique=True , db_index= True)
        content=models.TextField()
        author=models.ForeignKey(Author,on_delete=models.SET_NULL,
        
        null=True,related_name="posts")
        tag=models.ManyToManyField(Tag)



class Comment(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField()
    text=models.TextField()
    post=models.ForeignKey(Post ,
        on_delete=models.CASCADE,related_name='comments' )

    







