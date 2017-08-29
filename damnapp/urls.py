from django.conf.urls import url

from . import views as handyTool

urlpatterns = [
    url(r'^googlejabo/', handyTool.fBasedView),
    url(r'^buet/', handyTool.buetWeb),
]
