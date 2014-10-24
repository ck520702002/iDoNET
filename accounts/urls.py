from django.conf.urls import patterns, include, url
from views import logout,login,signup,setting

urlpatterns = patterns('',
    # Examples:
     
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', login.as_view()),
    url(r'^signup/', signup.as_view()),
    url(r'^logout/', logout.as_view()),
    url(r'^setting/', setting.as_view()),
)
