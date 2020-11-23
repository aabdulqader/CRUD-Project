from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentRegistration()
        student = User.objects.all()
        context = {'form':form, 'student':student}
        return context
    def post(self, request):
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            ps = form.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            return redirect ('home')

class UpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
        context = {'form':form}
        return render(request, 'update.html',context)
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return redirect('home')

class DeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
