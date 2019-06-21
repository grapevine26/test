from .models import (
    Client, FacebookInfo, InstagramInfo, TwitterInfo, GmailInfo, YoutubeInfo, Result, Reason
)
from .forms import ClientForm
from django.http import JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from crawler_AML.crawler.Crawler_facebook import start as facebook
from crawler_AML.crawler.Crawler_instagram import start as instagram
from crawler_AML.crawler.Crawler_youtube import start as youtube
from crawler_AML.crawler.Crawler_twitter import start as twitter
from crawler_AML.crawler.Crawler_gmail import start as gmail
from crawler_AML.crawler.Crawler_google import start as google
from crawler_AML.analysis.analysis_result import sns_data
from django.views.generic import ListView, CreateView, UpdateView, FormView, TemplateView, View
from django.views.generic.detail import DetailView, SingleObjectMixin, ContextMixin, SingleObjectTemplateResponseMixin
from django.urls import reverse_lazy, reverse


@method_decorator(login_required, name='dispatch')
class Home(FormView):
    form_class = ClientForm
    template_name = 'aml/home.html'

    def get_success_url(self, **kwargs):
        obj = Client.objects.order_by('-pk')[0].pk
        return reverse('aml:analysing', args=(obj,))

    def form_valid(self, form):
        form.instance.analyst = self.request.user
        form.save()
        return super(Home, self).form_valid(form)
    # def get_success_url(self):
    #     return reverse_lazy('aml:analysing', kwargs={'pk': self.kwargs['pk']})
    # def get_object(self):
    #     self.request.user


class Analysing(DetailView):
    model = Client
    template_name = 'aml/analysing.html'

    # def get_success_url(self, **kwargs):
    #     obj = Client.objects.order_by('-pk')[0].pk
    #     return reverse('aml:analysing', args=(obj,))

    def get_context_data(self, **kwargs):
        context = super(Analysing, self).get_context_data(**kwargs)
        sns_data(self.kwargs['pk'])
        return context


    # def get(self, request, *args, **kwargs):
    #     client = self.get_context_data(object=self.get_object())
    #     print(client)
    #     return render(request, 'aml/analysing.html', client)

    # def post(self, request, *args, **kwargs):
    #     # self.object = self.get_object()
    #     # self.object.view_count += 1
    #     # self.object.save()
    #     # post = self.get_context_data(object=self.object)
    #     return render(request, 'aml/analysing.html', self.get_object())

    # def get_context_data(self, **kwargs):
    #     context = super(Analysing, self).get_context_data(**kwargs)
    #     context['client'] = ClientInformation.objects.filter(pk=self.get_object())
    #     return context


class ResultView(DetailView):
    model = Client
    template_name = 'aml/result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        return context


def f_crawling(request):
    if request.is_ajax() and request.POST:
        f_username = request.POST.get('f_username')
        f_password = request.POST.get('f_password')
        if f_username is not None and f_password is not None:
            error = facebook(f_username, f_password)
            print('f_error :', error)

            try:
                data = FacebookInfo.objects.filter(user_id=f_username).last()
            except Exception as e:
                data = None
            print('f_data :', data)

            if error is None and data is not None:
                ctx = {
                    'facebook': '성공',
                    'username': data.username,
                    'birthday': data.birthday,
                    'phone_number': data.phone_number,
                    'address1': data.address1,
                    'friends_cnt': data.friends_cnt,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'facebook': data,
                    'error': error[0],
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def i_crawling(request):
    if request.is_ajax() and request.POST:
        i_username = request.POST.get('i_username')
        i_password = request.POST.get('i_password')
        if i_username is not None and i_password is not None:
            error = instagram(i_username, i_password)
            print('i_error :', error)
            try:
                data = InstagramInfo.objects.filter(user_id=i_username).last()
            except Exception as e:
                data = None
            print('i_data :', data)

            if error is None and data is not None:
                ctx = {
                    'instagram': '성공',
                    'username': data.username,
                    'post_cnt': data.post_cnt,
                    'follower_cnt': data.follower_cnt,
                    'following_cnt': data.following_cnt,
                    'like_cnt': data.like_cnt,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'instagram': data,
                    'error': error[0],
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def t_crawling(request):
    if request.is_ajax() and request.POST:
        t_username = request.POST.get('t_username')
        t_password = request.POST.get('t_password')
        t_ph = request.POST.get('t_ph')
        t_email = request.POST.get('t_email')
        if t_username is not None and t_password is not None:
            error = twitter(t_username, t_password, t_ph, t_email)
            print('error :', error)
            try:
                data = TwitterInfo.objects.filter(user_id=t_username).last()
            except Exception as e:
                data = None
            print('t_data :', data)

            if error is None and data is not None:
                ctx = {
                    'twitter': '성공',
                    'username': data.username,
                    'tweet_cnt': data.tweet_cnt,
                    'follower_cnt': data.follower_cnt,
                    'following_cnt': data.following_cnt,
                    'joined_date': data.joined_date,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'twitter': data,
                    'error': error[0],
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def y_crawling(request):
    if request.is_ajax() and request.POST:
        y_username = request.POST.get('g_username')
        y_password = request.POST.get('g_password')
        if y_username is not None and y_password is not None:
            error = youtube(y_username, y_password)
            print('y_error :', error)
            try:
                data = YoutubeInfo.objects.filter(user_id=y_username).last()
            except Exception as e:
                data = None
            print('y_data :', data)

            if error is None and data is not None:
                ctx = {
                    'youtube': '성공',
                    'username': data.username,
                    'subscribe_cnt': data.subscribe_cnt,
                    'recent_video_cnt': data.recent_video_cnt,
                    'comment_history_cnt': data.comment_history_cnt,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'youtube': data,
                    'error': error[0],
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def g_crawling(request):
    if request.is_ajax() and request.POST:
        g_username = request.POST.get('g_username')
        g_password = request.POST.get('g_password')
        if g_username is not None and g_password is not None:
            error = gmail(g_username, g_password)
            print('g_error :', error)
            try:
                data = GmailInfo.objects.filter(user_id=g_username).last()
            except Exception as e:
                data = None
            print('g_data :', data)

            if error is None and data is not None:
                ctx = {
                    'gmail': '성공',
                    'username': data.username,
                    'email': data.email,
                    'mail_cnt': data.mail_cnt,
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
            else:
                ctx = {
                    'gmail': data,
                    'error': error[0],
                }
                return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
        else:
            return None
    return None


def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
