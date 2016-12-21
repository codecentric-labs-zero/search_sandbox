from django.conf.urls import url, include
from search_sandbox_web import views

# patterns here are prefixed with 'web/'
urlpatterns = [
    url(r'^$', views.notes),
    url(r'^add_random_note/', views.add_random_note),
    url(r'^search/', include('haystack.urls')),
]
