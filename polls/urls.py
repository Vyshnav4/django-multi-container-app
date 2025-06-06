from django.urls import path

from . import views

# This sets the application namespace. It allows Django to differentiate
# the URL names between different apps.
app_name = 'polls'

# This list defines the URL patterns for the polls app.
# Each URL is mapped to a specific view.
urlpatterns = [
    # Example: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # Example: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # Example: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # Example: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
