from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^unorderedlist$', 'atest.views.unordered_list'),
    url(r'^mptttreelist$', 'atest.views.mptttree_list'),
)
