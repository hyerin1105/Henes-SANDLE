from django.urls import path, include
import main.views

urlpatterns = [
    ########### ceo ###########
    path('', main.views.wait, name="wait"),
    path('loading/', main.views.loading, name="loading"),
    path('checking/', main.views.checking, name="checking"),
    
    ########### customer ###########
    path('main/', main.views.main, name="main"),
    path('goods/<int:customer_id>', main.views.goods, name="goods"),
    path('complete/', main.views.complete, name="complete"),
    path('end/', main.views.end, name="end"),
]