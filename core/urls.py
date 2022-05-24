from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'journals', views.JournalViewSet, basename='journal')
urlpatterns = router.urls
