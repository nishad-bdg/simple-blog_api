from django.conf.urls import url
from blog_app import views

urlpatterns = [
    url(r'^blog/category/$', views.CategoryList.as_view()),
    url(r'^blog/category/(?P<slug>[\w-]+)/$', views.CategoryDetail.as_view()),

    url(r'^blog/$',views.BlogList.as_view()),
    url(r'^blog/(?P<pk>\d+)/$',views.BlogDetail.as_view()),
    url(r'^user-blogs/$',views.UserBlogList.as_view()),
    
]