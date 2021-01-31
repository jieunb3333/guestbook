from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import GuestForm,CommentForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            post = Post()
            post.writer = form.cleaned_data['writer']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('index')  
            

    else:
        posts = Post.objects
        comments=Comment.objects
        form = GuestForm()
        return render(request,'guestbook/index.html',{'posts':posts,'comments':comments,'form':form})


def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('index')

def c_delete(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect('index')


def comment(request, post_id):
    post_detail = Post.objects.get(id=post_id)
    comments = Comment.objects
    posts = Post.objects
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_detail
            comment.save()
            f=GuestForm()
            return redirect(index)

    else:
        form = CommentForm()
        return render(request,'guestbook/comment.html',{'posts':posts,'comments':comments,'form':form})
    
