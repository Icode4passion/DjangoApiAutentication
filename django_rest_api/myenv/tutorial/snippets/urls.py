# from django.urls import path
# from snippets import views
# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     path('snippets/',views.SnippetList.as_view()),
#     path('snippets/<int:pk>',views.SnippetDetail.as_view()),
#     path('users/',views.UserList.as_view()),
#     path('users/<int:pk>',views.UserDetail.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]