from .models import (
    FacebookInfo, InstagramInfo, TwitterInfo, GmailInfo, YoutubeInfo, Result, Reason
)
from django.http import JsonResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from crawler_AML.crawler.Crawler_facebook import start as facebook
from crawler_AML.crawler.Crawler_instagram import start as instagram
from crawler_AML.crawler.Crawler_youtube import start as youtube
from crawler_AML.crawler.Crawler_twitter import start as twitter
from crawler_AML.crawler.Crawler_gmail import start as gmail
from crawler_AML.crawler.Crawler_google import start as google
from crawler_AML.analysis.analysis_result import sns_data
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, TemplateView, View


class Home(TemplateView):
    template_name = 'aml/home.html'
# def home(request, pk):
#     ctx = {
#
#     }
#     return render(request, 'aml/home.html', ctx)


def analysing(request):
    if request.POST:
        f_username = request.POST.get('f_username')
        f_password = request.POST.get('f_password')
        i_username = request.POST.get('i_username')
        i_password = request.POST.get('i_password')
        g_username = request.POST.get('g_username')
        g_password = request.POST.get('g_password')
        t_username = request.POST.get('t_username')
        t_password = request.POST.get('t_password')
        t_ph = request.POST.get('t_ph')
        t_email = request.POST.get('t_email')
        ctx = {
            'f_username': f_username,
            'f_password': f_password,
            'i_username': i_username,
            'i_password': i_password,
            't_username': t_username,
            't_password': t_password,
            'g_username': g_username,
            'g_password': g_password,
            't_ph': t_ph,
            't_email': t_email,
        }
        return render(request, 'aml/analysing.html', ctx)
    ctx = {

    }
    return render(request, 'aml/analysing.html', ctx)


def result(request):
    if request.POST:
        f_id = request.POST.get('f_username')
        i_id = request.POST.get('i_username')
        t_id = request.POST.get('t_username')
        g_id = request.POST.get('g_username')

        try:
            f_info = FacebookInfo.objects.filter(user_id=f_id).last()
        except Exception as e:
            f_info = None
        try:
            i_info = InstagramInfo.objects.filter(user_id=i_id).last()
        except Exception as e:
            i_info = None
        try:
            t_info = TwitterInfo.objects.filter(user_id=t_id).last()
        except Exception as e:
            t_info = None
        try:
            y_info = YoutubeInfo.objects.filter(user_id=g_id).last()
        except Exception as e:
            y_info = None
        try:
            g_info = GmailInfo.objects.filter(user_id=g_id).last()
        except Exception as e:
            g_info = None

        ctx = {
            'f_id': f_id,
            'i_id': i_id,
            't_id': t_id,
            'g_id': g_id,
            'facebook': f_info,
            'instagram': i_info,
            'twitter': t_info,
            'youtube': y_info,
            'gmail': g_info,
        }
        return render(request, 'aml/result.html', ctx)

    ctx = {

    }
    return render(request, 'aml/result.html', ctx)


def risk(request, facebook_id):
    f_info = FacebookInfo.objects.filter(user_id=facebook_id).last()
    result_ = Result.objects.filter(f_id=facebook_id).last()
    reason = Reason.objects.get(rating=result_.user_rate)
    ctx = {
        'facebook': f_info,
        'result': result_,
        'reason': reason
    }
    return render(request, 'aml/risk.html', ctx)


def analysing_risk(request):
    if request.POST:
        f_username = request.POST.get('f_username')
        t_username = request.POST.get('t_username')
        i_username = request.POST.get('i_username')
        g_username = request.POST.get('g_username')

        sns_data(f_username, t_username, i_username, g_username)

        ctx = {

        }
        return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    ctx = {

    }
    return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})


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


def g_auth_crawling(request):
    if request.is_ajax() and request.POST:
        g_username = request.POST.get('g_username')
        g_password = request.POST.get('g_password')
        if g_username is not None and g_password is not None:
            data = google(g_username, g_password)
            print('google :', data[0])
            ctx = {
                'auth': '성공',
                'data': data[0],
            }
            return JsonResponse(ctx, content_type="application/json", json_dumps_params={'ensure_ascii': False})
    return None


def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
