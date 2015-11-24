from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(r'^cal/$', 'cal.views.calculate', name='calculate'),
    url(r'^signup/$', 'accounts.views.signup', name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view( #정적인 페이지 보여줄때 씀. Generic View
        template_name='accounts.views.signup_ok.html'
    ), name='signup_ok'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login_url'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/login/'}, name='logout_url'),
]