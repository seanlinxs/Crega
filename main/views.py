from django.views.generic import TemplateView
from main.models import *


class Home(TemplateView):
    template_name = 'main/home.html'
    

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        page = Page.objects.get(pk=1)
        textblocks = page.textblock_set;
        primary_box_text = textblocks.get(name='Text block #1')
        context['page_name'] = page.name
        context['primary_box_text'] = primary_box_text.content

        return context


class About(TemplateView):
    template_name = 'main/about.html'


class Product1(TemplateView):
    template_name = 'main/product1.html'


class Enquiry(TemplateView):
    template_name = 'main/enquiry.html'


class Contact(TemplateView):
    template_name = 'main/contact.html'


class Privacy(TemplateView):
    template_name = 'main/privacy.html'


class Terms(TemplateView):
    template_name = 'main/terms.html'