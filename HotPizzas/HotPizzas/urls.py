from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'PizzaTracker.views.home', name='home'),
    url(r'^pizzas/available/$', 'PizzaTracker.views.available_pizzas', name='available_pizzas'),
    url(r'^pizzas/delivered/$', 'PizzaTracker.views.delivered_pizzas', name='delivered_pizzas'),
    url(r'^pizzas/to-deliver/$', 'PizzaTracker.views.to_deliver_pizzas', name='to_deliver_pizzas'),
    url(r'^deliver-pizza/$', 'PizzaTracker.views.deliver_pizza', name='deliver_pizza'),
    url(r'^driver/$', 'PizzaTracker.views.driver_dashboard', name='driver_dashboard'),
    url(r'^customer/$', 'PizzaTracker.views.customer_dashboard', name='customer_dashboard'),
    url(r'^pizzas/closest/$', 'PizzaTracker.views.anonymous_pizza_browser', name='anonymous_pizza_browser'),
    url(r'^pizza/update/$', 'PizzaTracker.views.update_pizza', name='update_pizza'),
    url(r'^admin/', include(admin.site.urls)),
    #/login/ to sign in to the application
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #/logout/ to sign out of the application
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'login.html'}),
)
