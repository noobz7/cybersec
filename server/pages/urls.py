from django.urls import path

from .views import homePageView, balanceView, transferView, confirmView, sendMessageView, messageSentView

urlpatterns = [
    path('', homePageView, name='home'),
    path('balance/', balanceView, name='balance'),
    path('transfer/', transferView, name='transfer'),
    path('confirm/', confirmView, name='confirm'),
    path('message/', sendMessageView, name='message'),
    path('message_sent/', messageSentView, name='messageSent')
]
