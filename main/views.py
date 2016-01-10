from django.views.generic import TemplateView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse
from urllib.parse import urlencode

from main.models import Website, Page, TextBlock, PageImage, VideoLink, News
from main.forms import EnquiryForm
from crega.settings import MEDIA_HOST


def missing_page(name):
    return 'Please add page [{0}]'.format(name)


def missing_textblock(name):
    return 'Please add text block: [{0}]'.format(name)


def missing_image(name, size):
    return 'Please add image: [{0}] with size [{1}]'.format(name, size)


def missing_videolink(name):
    return 'Please add video link: [{0}]'.format(name)


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['media_url'] = MEDIA_HOST

        return context


class Home(BaseView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='Home')
            context['page_name'] = page.name
        except Page.DoesNotExist:
            context['page_name'] = missing_page('Home')
            return context

        textblocks = page.textblock_set
        pageimages = page.pageimage_set

        try:
            primary_box_text = textblocks.get(name='Primary box text')
            context['primary_box_text'] = primary_box_text.content
        except TextBlock.DoesNotExist:
            context['primary_box_text'] = missing_textblock('Primary box text')

        try:
            primary_box_image_1 = pageimages.get(name='Primary box image 1')
            context['primary_box_image_1'] = primary_box_image_1.image
        except PageImage.DoesNotExist:
            context['primary_box_image_1'] = missing_image('Primary box image 1', '1920×288')

        try:
            primary_box_image_2 = pageimages.get(name='Primary box image 2')
            context['primary_box_image_2'] = primary_box_image_2.image
        except PageImage.DoesNotExist:
            context['primary_box_image_2'] = missing_image('Primary box image 2', '1920×288')

        try:
            primary_box_image_3 = pageimages.get(name='Primary box image 3')
            context['primary_box_image_3'] = primary_box_image_3.image
        except PageImage.DoesNotExist:
            context['primary_box_image_3'] = missing_image('Primary box image 3', '1920×288')

        try:
            primary_box_image_4 = pageimages.get(name='Primary box image 4')
            context['primary_box_image_4'] = primary_box_image_4.image
        except PageImage.DoesNotExist:
            context['primary_box_image_4'] = missing_image('Primary box image 4', '1920×288')

        try:
            secondary_box_text_1 = textblocks.get(name='Secondary box text 1')
            context['secondary_box_text_1'] = secondary_box_text_1.content
        except TextBlock.DoesNotExist:
            context['secondary_box_text_1'] = missing_textblock('Secondary box text 1')

        try:
            secondary_box_image_1 = pageimages.get(name='Secondary box image 1')
            context['secondary_box_image_1'] = secondary_box_image_1.image
        except PageImage.DoesNotExist:
            context['secondary_box_image_1'] = missing_image('Secondary box image 1', '350×248')

        try:
            secondary_box_text_2 = textblocks.get(name='Secondary box text 2')
            context['secondary_box_text_2'] = secondary_box_text_2.content
        except TextBlock.DoesNotExist:
            context['secondary_box_text_2'] = missing_textblock('Secondary box text 2')

        try:
            secondary_box_image_2 = pageimages.get(name='Secondary box image 2')
            context['secondary_box_image_2'] = secondary_box_image_2.image
        except PageImage.DoesNotExist:
            context['secondary_box_image_2'] = missing_image('Secondary box image 2', '350×248')

        try:
            secondary_box_text_3 = textblocks.get(name='Secondary box text 3')
            context['secondary_box_text_3'] = secondary_box_text_3.content
        except TextBlock.DoesNotExist:
            context['secondary_box_text_3'] = missing_textblock('Secondary box text 3')

        try:
            secondary_box_image_3 = pageimages.get(name='Secondary box image 3')
            context['secondary_box_image_3'] = secondary_box_image_3.image
        except PageImage.DoesNotExist:
            context['secondary_box_image_3'] = missing_image('Secondary box image 3', '350×248')

        context['news'] = site.news_set.all()

        return context


class About(BaseView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='About')
            context['page_name'] = page.name
        except Page.DoesNotExist:
            context['page_name'] = missing_page('About')
            return context

        try:
            textblock_1 = page.textblock_set.get(name='Text block 1')
            context['textblock_1'] = textblock_1.content
        except TextBlock.DoesNotExist:
            context['textblock_1'] = missing_textblock('Text block 1')

        try:
            pageimage_1 = page.pageimage_set.get(name='Page image 1')
            context['pageimage_1'] = pageimage_1.image
        except PageImage.DoesNotExist:
            context['pageimage_1'] = missing_image('Page image 1', '455×280')

        try:
            textblock_2 = page.textblock_set.get(name='Text block 2')
            context['textblock_2'] = textblock_2.content
        except TextBlock.DoesNotExist:
            context['textblock_2'] = missing_textblock('Text block 2')

        try:
            pageimage_2 = page.pageimage_set.get(name='Page image 2')
            context['pageimage_2'] = pageimage_2.image
        except PageImage.DoesNotExist:
            context['pageimage_2'] = missing_image('Page image 2', '455×280')

        try:
            textblock_3 = page.textblock_set.get(name='Text block 3')
            context['textblock_3'] = textblock_3.content
        except TextBlock.DoesNotExist:
            context['textblock_3'] = missing_textblock('Text block 3')

        try:
            pageimage_3 = page.pageimage_set.get(name='Page image 3')
            context['pageimage_3'] = pageimage_3.image
        except PageImage.DoesNotExist:
            context['pageimage_3'] = missing_image('Page image 3', '455×280')

        return context


class Product1(BaseView):
    template_name = 'main/product1.html'

    def get_context_data(self, **kwargs):
        context = super(Product1, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='Product1')
            context['page_name'] = page.name
            context['page_title'] = page.title
        except Page.DoesNotExist:
            context['page_name'] = missing_page('Product1')
            return context

        try:
            textblock_1 = page.textblock_set.get(name='Text block 1')
            context['textblock_1'] = textblock_1.content
        except TextBlock.DoesNotExist:
            context['textblock_1'] = missing_textblock('Text block 1')

        try:
            videolink_1 = page.videolink_set.get(name='Video link 1')
            context['videolink_1'] = videolink_1.link
        except VideoLink.DoesNotExist:
            context['missing_videolink_1'] = True
            context['videolink_1'] = missing_videolink('Video link 1')

        try:
            pageimage_1 = page.pageimage_set.get(name='Page image 1')
            context['pageimage_1'] = pageimage_1.image
        except PageImage.DoesNotExist:
            context['pageimage_1'] = missing_image('Page image 1', '455×280')

        try:
            textblock_2 = page.textblock_set.get(name='Text block 2')
            context['textblock_2'] = textblock_2.content
        except TextBlock.DoesNotExist:
            context['textblock_2'] = missing_textblock('Text block 2')

        try:
            pageimage_2 = page.pageimage_set.get(name='Page image 2')
            context['pageimage_2'] = pageimage_2.image
        except PageImage.DoesNotExist:
            context['pageimage_2'] = missing_image('Page image 2', '455×280')

        try:
            textblock_3 = page.textblock_set.get(name='Text block 3')
            context['textblock_3'] = textblock_3.content
        except TextBlock.DoesNotExist:
            context['textblock_3'] = missing_textblock('Text block 3')

        return context


class Product2(BaseView):
    template_name = 'main/product2.html'

    def get_context_data(self, **kwargs):
        context = super(Product2, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='Product2')
            context['page_name'] = page.name
            context['page_title'] = page.title
        except Page.DoesNotExist:
            context['page_name'] = missing_page('Product2')
            return context

        try:
            textblock_1 = page.textblock_set.get(name='Text block 1')
            context['textblock_1'] = textblock_1.content
        except TextBlock.DoesNotExist:
            context['textblock_1'] = missing_textblock('Text block 1')

        try:
            videolink_1 = page.videolink_set.get(name='Video link 1')
            context['videolink_1'] = videolink_1.link
        except VideoLink.DoesNotExist:
            context['missing_videolink_1'] = True
            context['videolink_1'] = missing_videolink('Video link 1')

        try:
            pageimage_1 = page.pageimage_set.get(name='Page image 1')
            context['pageimage_1'] = pageimage_1.image
        except PageImage.DoesNotExist:
            context['pageimage_1'] = missing_image('Page image 1', '455×280')

        try:
            textblock_2 = page.textblock_set.get(name='Text block 2')
            context['textblock_2'] = textblock_2.content
        except TextBlock.DoesNotExist:
            context['textblock_2'] = missing_textblock('Text block 2')

        try:
            pageimage_2 = page.pageimage_set.get(name='Page image 2')
            context['pageimage_2'] = pageimage_2.image
        except PageImage.DoesNotExist:
            context['pageimage_2'] = missing_image('Page image 2', '455×280')

        try:
            textblock_3 = page.textblock_set.get(name='Text block 3')
            context['textblock_3'] = textblock_3.content
        except TextBlock.DoesNotExist:
            context['textblock_3'] = missing_textblock('Text block 3')

        return context


class Product3(BaseView):
    template_name = 'main/product3.html'

    def get_context_data(self, **kwargs):
        context = super(Product3, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='Product3')
            context['page_name'] = page.name
            context['page_title'] = page.title
        except Page.DoesNotExist:
            context['page_name'] = missing_page('Product3')
            return context

        try:
            textblock_1 = page.textblock_set.get(name='Text block 1')
            context['textblock_1'] = textblock_1.content
        except TextBlock.DoesNotExist:
            context['textblock_1'] = missing_textblock('Text block 1')

        try:
            videolink_1 = page.videolink_set.get(name='Video link 1')
            context['videolink_1'] = videolink_1.link
        except VideoLink.DoesNotExist:
            context['missing_videolink_1'] = True
            context['videolink_1'] = missing_videolink('Video link 1')

        try:
            pageimage_1 = page.pageimage_set.get(name='Page image 1')
            context['pageimage_1'] = pageimage_1.image
        except PageImage.DoesNotExist:
            context['pageimage_1'] = missing_image('Page image 1', '455×280')

        try:
            textblock_2 = page.textblock_set.get(name='Text block 2')
            context['textblock_2'] = textblock_2.content
        except TextBlock.DoesNotExist:
            context['textblock_2'] = missing_textblock('Text block 2')

        try:
            pageimage_2 = page.pageimage_set.get(name='Page image 2')
            context['pageimage_2'] = pageimage_2.image
        except PageImage.DoesNotExist:
            context['pageimage_2'] = missing_image('Page image 2', '455×280')

        try:
            textblock_3 = page.textblock_set.get(name='Text block 3')
            context['textblock_3'] = textblock_3.content
        except TextBlock.DoesNotExist:
            context['textblock_3'] = missing_textblock('Text block 3')

        return context


class Product4(BaseView):
    template_name = 'main/product4.html'

    def get_context_data(self, **kwargs):
        context = super(Product4, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='Product4')
            context['page_name'] = page.name
            context['page_title'] = page.title
        except Page.DoesNotExist:
            context['page_name'] = missing_page('Product4')
            return context

        try:
            textblock_1 = page.textblock_set.get(name='Text block 1')
            context['textblock_1'] = textblock_1.content
        except TextBlock.DoesNotExist:
            context['textblock_1'] = missing_textblock('Text block 1')

        try:
            videolink_1 = page.videolink_set.get(name='Video link 1')
            context['videolink_1'] = videolink_1.link
        except VideoLink.DoesNotExist:
            context['missing_videolink_1'] = True
            context['videolink_1'] = missing_videolink('Video link 1')

        try:
            pageimage_1 = page.pageimage_set.get(name='Page image 1')
            context['pageimage_1'] = pageimage_1.image
        except PageImage.DoesNotExist:
            context['pageimage_1'] = missing_image('Page image 1', '455×280')

        try:
            textblock_2 = page.textblock_set.get(name='Text block 2')
            context['textblock_2'] = textblock_2.content
        except TextBlock.DoesNotExist:
            context['textblock_2'] = missing_textblock('Text block 2')

        try:
            pageimage_2 = page.pageimage_set.get(name='Page image 2')
            context['pageimage_2'] = pageimage_2.image
        except PageImage.DoesNotExist:
            context['pageimage_2'] = missing_image('Page image 2', '455×280')

        try:
            textblock_3 = page.textblock_set.get(name='Text block 3')
            context['textblock_3'] = textblock_3.content
        except TextBlock.DoesNotExist:
            context['textblock_3'] = missing_textblock('Text block 3')

        return context


class Service1(BaseView):
    template_name = 'main/service1.html'

    def get_context_data(self, **kwargs):
        context = super(Service1, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='Service1')
            context['page_name'] = page.name
            context['page_title'] = page.title
        except Page.DoesNotExist:
            context['page_name'] = missing_page('Service1')
            return context

        try:
            textblock_1 = page.textblock_set.get(name='Text block 1')
            context['textblock_1'] = textblock_1.content
        except TextBlock.DoesNotExist:
            context['textblock_1'] = missing_textblock('Text block 1')

        try:
            videolink_1 = page.videolink_set.get(name='Video link 1')
            context['videolink_1'] = videolink_1.link
        except VideoLink.DoesNotExist:
            context['missing_videolink_1'] = True
            context['videolink_1'] = missing_videolink('Video link 1')

        try:
            pageimage_1 = page.pageimage_set.get(name='Page image 1')
            context['pageimage_1'] = pageimage_1.image
        except PageImage.DoesNotExist:
            context['pageimage_1'] = missing_image('Page image 1', '455×280')

        try:
            textblock_2 = page.textblock_set.get(name='Text block 2')
            context['textblock_2'] = textblock_2.content
        except TextBlock.DoesNotExist:
            context['textblock_2'] = missing_textblock('Text block 2')

        try:
            pageimage_2 = page.pageimage_set.get(name='Page image 2')
            context['pageimage_2'] = pageimage_2.image
        except PageImage.DoesNotExist:
            context['pageimage_2'] = missing_image('Page image 2', '455×280')

        try:
            textblock_3 = page.textblock_set.get(name='Text block 3')
            context['textblock_3'] = textblock_3.content
        except TextBlock.DoesNotExist:
            context['textblock_3'] = missing_textblock('Text block 3')

        return context


class Service2(BaseView):
    template_name = 'main/service2.html'

    def get_context_data(self, **kwargs):
        context = super(Service2, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')

        try:
            page = site.page_set.get(name='Service2')
            context['page_name'] = page.name
            context['page_title'] = page.title
        except Page.DoesNotExist:
            context['page_name'] = missing_page('Service2')
            return context

        try:
            textblock_1 = page.textblock_set.get(name='Text block 1')
            context['textblock_1'] = textblock_1.content
        except TextBlock.DoesNotExist:
            context['textblock_1'] = missing_textblock('Text block 1')

        try:
            videolink_1 = page.videolink_set.get(name='Video link 1')
            context['videolink_1'] = videolink_1.link
        except VideoLink.DoesNotExist:
            context['missing_videolink_1'] = True
            context['videolink_1'] = missing_videolink('Video link 1')

        try:
            pageimage_1 = page.pageimage_set.get(name='Page image 1')
            context['pageimage_1'] = pageimage_1.image
        except PageImage.DoesNotExist:
            context['pageimage_1'] = missing_image('Page image 1', '455×280')

        try:
            textblock_2 = page.textblock_set.get(name='Text block 2')
            context['textblock_2'] = textblock_2.content
        except TextBlock.DoesNotExist:
            context['textblock_2'] = missing_textblock('Text block 2')

        try:
            pageimage_2 = page.pageimage_set.get(name='Page image 2')
            context['pageimage_2'] = pageimage_2.image
        except PageImage.DoesNotExist:
            context['pageimage_2'] = missing_image('Page image 2', '455×280')

        try:
            textblock_3 = page.textblock_set.get(name='Text block 3')
            context['textblock_3'] = textblock_3.content
        except TextBlock.DoesNotExist:
            context['textblock_3'] = missing_textblock('Text block 3')

        return context


class Enquiry(FormView):
    template_name = 'main/enquiry.html'
    form_class = EnquiryForm

    def form_valid(self, form):
        form.send_email()
        success_url = '{0}?{1}'.format(reverse('thanks'), urlencode({'firstname': form.cleaned_data['firstname'], 'lastname': form.cleaned_data['lastname']}))

        return redirect(success_url)


class Contact(BaseView):
    template_name = 'main/contact.html'


class Privacy(BaseView):
    template_name = 'main/privacy.html'


class Terms(BaseView):
    template_name = 'main/terms.html'


class AllNews(BaseView):
    template_name = 'main/news.html'

    def get_context_data(self, **kwargs):
        context = super(AllNews, self).get_context_data(**kwargs)

        site = get_object_or_404(Website, name='crega.com.au')
        news = site.news_set.all()
        context['news'] = news

        return context


class SingleNews(BaseView):
    template_name = 'main/singlenews.html'

    def get_context_data(self, **kwargs):
        context = super(SingleNews, self).get_context_data(**kwargs)

        news = get_object_or_404(News, pk=self.kwargs.get('pk'))
        context['news'] = news

        return context


class Thanks(BaseView):
    template_name = 'main/thanks.html'

    def get_context_data(self, **kwargs):
        context = super(Thanks, self).get_context_data(**kwargs)
        context['firstname'] = self.request.GET.get('firstname')
        context['lastname'] = self.request.GET.get('lastname')

        return context
