from django.urls import path, include
#from .views import ArticleList,ArticleDetails
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet


router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')


urlpatterns = [
    #path('articles/', article_list),
    #path('articles/<slug:slug>/', article_details),
    #path('articles/', ArticleList.as_view()),
    #path('articles/<slug:slug>/', ArticleDetails.as_view())
    path('', include(router.urls))
]