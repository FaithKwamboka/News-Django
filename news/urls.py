from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path,include
from . import views

urlpatterns=[
    # re_path('^$',views.welcome,name = 'welcome'),
    re_path(r'^article/(\d+)',views.article,name ='article'),
    re_path(r'^$',views.news_today,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)