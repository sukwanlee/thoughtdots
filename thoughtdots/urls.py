from django.conf.urls import patterns, include, url

from thoughtdots.views import DataDetailView, DataSetCreateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^(?P<pk>\d+)/$', DataDetailView.as_view(), name='data_detail_view'),
    url(r'^create/data/$', DataSetCreateView.as_view(), name='data_set_create_view'),
    # url(r'^$', 'thoughtdots.views.home', name='home'),
    # url(r'^thoughtdots/', include('thoughtdots.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
