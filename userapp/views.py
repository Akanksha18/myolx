from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
# from django.contrib.auth.decorators import login_required

from .models import ProfileImage, UserDetail, ItemDetail, ItemUpload, User
from userapp.forms import UserForm, UploadFileForm, ProfileImageForm, UserDetailForm, ItemDetailForm, ItemUploadForm


def index(request):
    return render_to_response('index.html')

def index1(request):
    return render_to_response('index1.html')

def index2(request):
    return render_to_response('index2.html')

def app(request):
    return render_to_response('app_hello.html')

def register(request):
    if request.method == 'POST':
        print request.POST
        form = UserForm(request.POST)
        if form.is_valid():
            print form.save()

            return HttpResponseRedirect('/thanks/')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form' :form})
        
def thanks(request):
    return render_to_response('thank-you.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return  render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    print user

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

# @login_required
def loggedin(request):
    return render_to_response('loggedin.html',
                             {'full_name' " request.user.username"})
                             

def invalid_login(request):
    return render_to_response('invalid_login.html')

# @login_required
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

class ProfileImageView(FormView):
    template_name = 'profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile_image', kwargs={'pk':self.id})

# @login_required
class ProfileDetailView(DetailView):
    model = ProfileImage
    template_name = 'profile_image.html'
    context_object_name = 'image'

# @login_required
class ProfileImageIndexView(ListView):
    model = ProfileImage
    template_name = 'profile_image_view.html'
    context_object_name= 'images'
    queryset = ProfileImage.objects.all()

# @login_required
def profile(request):
    if request.method == 'POST':
        userobj = UserDetail(user=request.user)
        form = UserDetailForm(request.POST,instance=userobj)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/thanks_user/')
    else:
        form = UserDetailForm()
        print form
    return render(request, 'profile.html', {'form' :form})
    # return render_to_response('profile.html')


def item(request):
    if request.method == 'POST':
        item = ItemDetail(user=request.user)
        form = ItemDetailForm(request.POST,instance=item)    
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/thanks_user/')
    else:
        form = ItemDetailForm()
        print form
    return render(request, 'item-detail.html', {'form' :form})  


def thanks_user(request):
    return render_to_response('thank-you-user.html')

def get_category_users(category):
    return User.objects.filter(itemdetail__category=category)
 
    
def item_upload(request):
    if request.method == 'POST':
        item = ItemUpload(user=request.user)
        form = ItemUploadForm(request.POST,request.FILES, instance=item)   
        if form.is_valid():
            form.save()
 
            return HttpResponseRedirect('/thanks_user/')
    else:
        form = ItemUploadForm()
        print form
        # get the gadget users
        gadget_users = get_category_users(ItemDetail.GADGET)
    return render(request, 'item-upload.html', {'form' :form, 'gadget_users': gadget_users}) 


def seek(request):
    return render_to_response('seek.html')

# def profile(request):
#     if request.method == 'POST':
#         user_form = UserDetailForm(request.POST)
#         if user_form.is_valid():
#             newuser = user_form.save(commit=False)
#              = request.user
#             newuser.save()

#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = UserDetailForm()
#         print form
#     return render(request, 'profile.html', {'form' :form})
    