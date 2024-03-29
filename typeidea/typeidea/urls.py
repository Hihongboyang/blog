"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.urls import re_path, path
# # from django.conf.urls import url
# from django.contrib import admin
# from blog.views import post_list, post_detail, login
# from config.views import links
# from typeidea.custom_site import custom_site
#
#
# urlpatterns = [
#     path("login/", login, name='login'),
#     re_path(r'^$', post_list, name='index'),
#     re_path(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
#     re_path(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
#     re_path(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
#     re_path(r'^links/$', links, name='links'),
#     re_path(r'^admin/', custom_site.urls, name='super-admin'),
#     re_path(r'^super_admin/', admin.site.urls, name='admin'),
# ]

from django.contrib import sitemaps
from django.urls import re_path, path
# from django.conf.urls import url
from django.contrib import admin
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView, login
from config.views import LinkListView
from comment.views import CommentView
from .custom_site import custom_site
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

urlpatterns = [
    re_path(r"^login/", login, name='login'),
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    re_path(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    re_path(r'^links/$', LinkListView.as_view(), name='links'),
    re_path(r'^super_admin/', admin.site.urls, name='super-admin'),
    re_path(r'^admin/', custom_site.urls, name='admin'),
    re_path(r'^search/$', SearchView.as_view(), name='search'),
    re_path(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    re_path(r'^comment/$', CommentView.as_view(), name='comment'),
    re_path(r'^rss|feed/', LatestPostFeed(), name='rss'),
    re_path(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
]
