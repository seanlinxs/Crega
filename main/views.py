from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'main/home.html'


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