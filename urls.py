from django.conf.urls import url

from . import views

urlpatterns = [
    # Frontend homepage if logged out, else application home.
    url(r'^$', views.index, name='index'),
    # Group URL defined as /g/group-name/ or /group/group-name/.
    url(
        r'^(?:g|group)/(?P<group_name>[a-z-A-Z0-9]+)/$',
        views.group,
        name='group'
    ),
    # User URL defined as /u/user-name/ or /user/user-name.
    url(
        r'^(?:u|user)/(?P<user_name>[a-z-A-Z0-9]+)/$',
        views.user,
        name='user'
    ),
    # Search URL defined as /s/search-term or /search/search-term.
    url(
        r'^(?:s|search)/(?P<search_term>[a-z-A-Z0-9]+)/$',
        views.search,
        name='search'
    ),
    # Profile URL defined as /p/ or /profile/.
    url(r'^(?:p|profile)/$', views.profile, name='profile'),
    # Settings URL defined as /settings/.
    url(r'^settings/$', views.settings, name='settings'),
    # Login URL defined as /login/.
    url(r'^login/$', views.login, name='login'),
    # Signup URL defined as /signup/.
    url(r'^signup/$', views.signup, name='signup'),
    # Password reset URL defined as /reset/.
    url(r'^reset/$', views.reset, name='reset'),
    
]