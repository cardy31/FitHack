from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from fitness import views

# app_name = 'refs'
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^food/$',
        views.FoodList.as_view(),
        name='food-list'),
    url(r'^food/(?P<pk>[0-9]+)/$',
        views.FoodDetail.as_view(),
        name='food-detail'),
    url(r'^memberinfo/$',
        views.MemberInfoList.as_view(),
        name='memberinfo-list'),
    url(r'^memberinfo/(?P<pk>[0-9]+)/',
        views.MemberInfoDetail.as_view(),
        name='memberinfo-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
