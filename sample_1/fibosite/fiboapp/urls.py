from django.conf.urls import url,include
import fiboapp.views

urlpatterns = [url(r'fibarchive/',fiboapp.views.fib_archive, name = 'fib_archive'),
               url(r'^$',fiboapp.views.index,name = 'index'),
               url(r'fibpost/',fiboapp.views.fib_post,name = 'fib_post'),
              ]
#url(r'fibarchive/',fiboapp.views.fib_archive, name = 'fib_archive'),




#url(r'create/',myblog.views.create_blogpost),
#url('',myblog.views.index,name = 'index'),
#url(r'^$', myblog.views.archive),
