from django.urls import path
from . import views
urlpatterns = [
    path('shop/', views.shop),
    path('jeju/', views.jeju),
    # path(
    #     'text/<str:char>/',
    #     c_views.text
    #     ),
    # path(
    #     '<int:year>/<int:month>/',
    #     c_views.date
    #     ),
]