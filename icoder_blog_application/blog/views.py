from django.core.checks import messages
from django.shortcuts import redirect, render, HttpResponse
from blog.models import Post, BlogComment
from django.contrib import messages
# Create your views here.

def blog_home(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request, 'blog/bloghome.html',context)

def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comment = BlogComment.objects.filter(post = post)
    context = {'post':post, 'comments':comment, 'user': request.user}
    return render(request, 'blog/blogpost.html',context)

def Post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        if parentSno == "":
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request, 'Your comment has been posted successfully!!')
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post, parent=parent)
            comment.save()
            messages.success(request, 'Your reply has been posted successfully')

    return redirect(f"/blog/post/{post.slug}")









