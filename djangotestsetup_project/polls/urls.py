from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('home/', views.IndexView.as_view(), name='index'),
    path('', views.PollsIndexView.as_view(), name='poll_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]