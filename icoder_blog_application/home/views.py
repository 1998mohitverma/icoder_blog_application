from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home_page(reques):
    return render(reques, 'home/home.html')

def about_page(request):
    return render(request, 'home/about.html')

def contact_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        #apply some validation:
        if len(name) < 3 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, 'Please Fill form correctly !')
        else:                
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your Message has been successfully sent !!')

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query) > 70:
        # allposts = []
        allposts = Post.objects.none()
    else:    
        allpoststitle = Post.objects.filter(title__icontains = query)
        allpostscontent = Post.objects.filter(content__icontains = query)
        allposts = allpoststitle.union(allpostscontent)

    if allposts.count() == 0:
        messages.warning(request,'No search result found. Please refined you query!!')    
    context = {'allposts':allposts,'query':query}
    return render(request, 'home/search.html',context)

def signup_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # check some eeror code:
        if len(username) > 10:
            messages.error(request,'Username must be under 10 character')
            return redirect('home')
        
        elif not username.isalnum():
            messages.error(request,'Username should contain only letter and number')
            return redirect('home')  

        elif pass1 != pass2:
            messages.error(request, 'Your password did not match ! Please Enter similar password')    
            return redirect('home')
        #create user:
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your iCoder account has been successfully created!")
        return redirect('home')
    else:
        return render(request,'home/signup.html')

def login_form(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['pass']
        user = authenticate(username=uname,password=pwd)
        if user is not None:
            login(request,user)
            messages.success(request, 'Successfully Login')
            return redirect('home')
        else:
            messages.error(request, 'Your Credentials are Invalid ! Try Again !')
            return redirect('home')    
    else:
        return render(request,'home/login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'you have successfully logout!')
    return redirect('home')