from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from lockedinapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from lockedinapi.views import DifficultyView
from lockedinapi.views import EquipmentView
from lockedinapi.views import ExerciseView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'difficulty', DifficultyView, 'difficulty')
router.register(r'equipment', EquipmentView, 'equipment')
router.register(r'exercises', ExerciseView, 'exercise')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]