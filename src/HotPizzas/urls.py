from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^pizzas/available/$', 'core.views.available_pizzas', name='available_pizzas'),
    url(r'^pizzas/delivered/$', 'core.views.delivered_pizzas', name='delivered_pizzas'),
    url(r'^pizzas/to-deliver/$', 'core.views.to_deliver_pizzas', name='to_deliver_pizzas'),
    url(r'^add-pizza/$', 'core.views.add_pizza', name='add_pizza'),
    url(r'^deliver-pizza/$', 'core.views.deliver_pizza', name='deliver_pizza'),
    url(r'^driver/$', 'core.views.driver_dashboard', name='driver_dashboard'),
    url(r'^customer/$', 'core.views.customer_dashboard', name='customer_dashboard'),
    url(r'^pizzas/closest/$', 'core.views.anonymous_pizza_browser', name='anonymous_pizza_browser'),
    url(r'^pizza/update/$', 'core.views.update_pizza', name='update_pizza'),
    url(r'^admin/', include(admin.site.urls)),
    #/login/ to sign in to the application
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #/logout/ to sign out of the application
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
)
