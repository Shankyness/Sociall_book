from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('authors-sellers/', views.authors_and_sellers, name='authors_and_sellers'),
    path('upload-books/', views.upload_books, name='upload_books'),
    path('uploaded-files/', views.uploaded_files, name='uploaded_files'),

]
