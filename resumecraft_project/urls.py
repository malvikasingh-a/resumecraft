from django.contrib import admin
from django.urls import path
from core import views  # We import our views from the core app

urlpatterns = [
    # 1. Admin Panel (Standard Django)
    path('admin/', admin.site.urls),
    
    # 2. Public Pages
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    
    # 3. Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # 4. RESUME ACTIONS (This is the new part!)
    # This URL runs the function that creates a blank resume in the database
    path('create-resume/', views.create_resume, name='create_resume'),

    # This URL expects a number (int:id) after 'editor/'
    # Example: /editor/5/ -> Opens resume #5
    path('editor/<int:id>/', views.editor, name='editor'),
    path('delete/<int:id>/', views.delete_resume, name='delete_resume'),
]