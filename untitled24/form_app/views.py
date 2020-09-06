from django.shortcuts import render
from . import forms
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'form_app/index.html'
def form_page_view(request):
    form=forms.FormName()
    my_dic={'forms':form}
    return render(request,'form_app/form_page.html',my_dic)
# Create your views here.
