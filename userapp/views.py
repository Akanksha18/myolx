from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from .models import ProfileImage
from userapp.forms import UserForm, UploadFileForm, ProfileImageForm

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


def loggedin(request):
    return render_to_response('loggedin.html',
                             {'full_name' " request.user.username"})
                             

def invalid_login(request):
    return render_to_response('invalid_login.html')


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

class ProfileDetailView(DetailView):
    model = ProfileImage
    template_name = 'profile_image.html'
    context_object_name = 'image'

class ProfileImageIndexView(ListView):
    model = ProfileImage
    template_name = 'profile_image_view.html'
    context_object_name= 'images'
    queryset = ProfileImage.objects.all()

def profile(request):
    return render_to_response('profile.html')