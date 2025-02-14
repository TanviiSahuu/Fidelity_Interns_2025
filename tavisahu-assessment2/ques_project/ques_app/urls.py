from ques_app.views import QuestionViews
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
schema_view = get_schema_view(openapi.Info(title='Question_paper_api', default_version="1.0.0", description="Questions",
                                           terms_of_service="", contact=openapi.Contact(email="tanvi.sahu30@gmail.com"),
                                            license=openapi.License("Open")), public=True)
from rest_framework import routers

myrouter = routers.DefaultRouter()
myrouter.register("Questionpaper", QuestionViews, "base")

urlpatterns = [
    path('view/', include(myrouter.urls)),   
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]
