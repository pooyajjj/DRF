from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls



# {
# 	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODE4MTcxMSwiaWF0IjoxNjc4MDk1MzExLCJqdGkiOiIyYjU1YWFlYWJmOGE0YzQ2YWFhNjY3MjkyOWMxYjBmYSIsInVzZXJfaWQiOjF9.ZNPdZ7x1wNYJL1ozF7ybqv1DFa72M8__xhIRJyXN-Qs",
# 	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4MDk1NjExLCJpYXQiOjE2NzgwOTUzMTEsImp0aSI6IjM2MmUzMDY2N2NiMDRkMGJhMWMyNTJiZGE3OGU5YWM5IiwidXNlcl9pZCI6MX0.oUK06DwzBpZMJkfBf9fH7CbsR2YWCV5DQd8JVIK334E"
# }
