from django.urls import path, include

from application.account.views import RegisterApiView, ActivationView, LoginApiView


urlpatterns = [

   path('register/', RegisterApiView.as_view()),
   path('activate/<uuid:activation_code>/', ActivationView.as_view()),
   path('login/', LoginApiView.as_view()),


]