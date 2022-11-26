from rest_framework.routers import DefaultRouter
from lms.views import StudentViewSet
student_router = DefaultRouter()
student_router.register(r'student',
                StudentViewSet,
                basename='user')
