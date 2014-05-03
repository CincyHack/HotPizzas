from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HotPizzas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'PizzaTracker.views.home', name='home'),
    url(r'^pizzas/available/$', 'PizzaTracker.views.available_pizzas', name='available_pizzas'),
    url(r'^admin/', include(admin.site.urls)),
    #/login/ to sign in to the application
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #/logout/ to sign out of the application
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
)
