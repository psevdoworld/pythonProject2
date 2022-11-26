from rest_framework.routers import DefaultRouter
from lms.views import StudentViewSet, CuratorViewSet

lms_router = DefaultRouter()
lms_router.register(r'student', StudentViewSet, basename='user')
lms_router.register(r'curator', CuratorViewSet, basename='curator')
