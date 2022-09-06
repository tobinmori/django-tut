
from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name='polls'

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('question/<int:pk>/', views.QuestionDetailView.as_view(), name='question_detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('cbv', views.CBV.as_view(), name='cbv'),
    path('cbvs', views.SubclassCBV.as_view(), name='scbv'),
    ## RedirectView demos
    path('test-redirect', views.TestRedirectView.as_view(), name='goog'),
    path('test-redirect2', RedirectView.as_view(url="https://www.yahoo.com"), name='yahoo'),
    ## TemplateView demos
    path('test-template-view', views.TemplateView.as_view(template_name='polls/hello.html')),
    path('test-template-view2', views.TestTemplateView.as_view(), ),
    ## ListView demos
    path('questions/', views.ListViewDemo.as_view(), name='show-questions'),
    ## DetailView demo
    path('question-detail/<int:pk>', views.DetailViewDemo.as_view(), name='show-question'),
    ## CRUD Views
    path('question/add/', views.CreateViewDemo.as_view(), name='add-group'),
    path('question/update/<int:pk>', views.UpdateViewDemo.as_view(), name='update-group'),

]
