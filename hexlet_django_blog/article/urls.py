from django.urls import path
from hexlet_django_blog.article import views
# from .views import IndexView


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:tags>/<int:article_id>/', views.get_tags, name='article'),
]
# urlpatterns = [
#     path('', views.index, name='index'),
# ]
