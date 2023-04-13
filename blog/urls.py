from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', views.single_post_page, name="single_post_page"),
    path('', views.index, name="index"),
    # path('', views.PostList.as_view()),
]

