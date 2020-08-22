from django.urls import path
from .views import HomePage, ReadMore, Share

app_name = 'blog'


urlpatterns = [
    path('',HomePage.as_view(), name = "HomePage"),
    path('detail/<int:pk>/', ReadMore.as_view(), name = "detail-view"),
    path('Share/', Share.as_view(success_url = '../'), name = "Share"),
    
    
]

