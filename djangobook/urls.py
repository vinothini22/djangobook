from django.conf.urls import patterns, include, url
from books import views
from djangobook import views as views1
from contactform.views import contact
from contactform.views import thanks
from djangobook.views import base
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',   #patterns is a function which takes an empty string and other url patterns through url function where first argument to it is regex and next is name of the view function
	url(r'^$',base),
	url(r'^hello/$',views1.hello),
	url(r'^hello/plus$',views1.current_datetime), #dynamic content
	url(r'^hello/plus/(\d{1,2})/$',views1.hours_ahead), #dynamic url
	url(r'^metainfo$',views1.display_metadata),
	url(r'^meta$',views1.display_meta),
	url(r'^search-form/$',views.search_form),
	url(r'^search/$',views.search),
	url(r'^search-test/$',views.search_test),
	url(r'^contact/$',contact),
	url(r'^contact/thanks/$',thanks),
	url(r'^image$',views.my_image),
)
