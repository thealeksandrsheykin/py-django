from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

# urlpatterns = [
#     path('',views.HelloWorldView.as_view()),
#     path('<str:word>/',views.check_kwargs),

# ]

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("coursers/", views.CoursesPageView.as_view(), name="courses_list"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
]
