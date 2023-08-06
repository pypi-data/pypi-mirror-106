from django.urls import path
from . import views


urlpatterns = (
    # Step by step
    path('', views.GettingStartedView.as_view(), name="getting-started"),
)
