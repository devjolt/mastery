from django.urls import path, include
from . import views
from .mastery_modules import _1, _2, _3, _4
from .views import HomeView, RandomModuleView, log_problem

urlpatterns = [
    path('', HomeView.as_view(), name='mastery_home'),
    path('/all_nt/', RandomModuleView.as_view(modules = (_1,)), name = 'all_nt'),
] 