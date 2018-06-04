from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from snippets import views, views_cb
from snippets.views_cb import SnippetViewSet, UserViewSet


#################### function-based views ###############
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list_old),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail_old),
# ]




##################### function-based views using wrapper ###############
# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# Using format suffixes gives us URLs that explicitly refer to a given format
# e.g.http://example.com/api/items/4.json
# urlpatterns = format_suffix_patterns(urlpatterns)



###################### class-based views #########################
# urlpatterns = [
# 	url(r'^$', views.api_root),
#     url(r'^snippets/$', views_cb.SnippetView.as_view(), name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views_cb.SnippetDetailView.as_view(), name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views_cb.SnippetHighlight.as_view(), name='snippet-highlight'),

#     url(r'^users/$', views_cb.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views_cb.UserDetail.as_view(), name='user-detail'),
# ]


###################### Binding ViewSets to URLs explicitly #########################
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ])




###################### Using routers #########################
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views_cb.SnippetViewSet)
router.register(r'users', views_cb.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
