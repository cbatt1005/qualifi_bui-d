from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name= 'logout'),
    path('add_campaign', views.add_campaign, name='add-campaign'),
    path('view_campaign', views.list_campaign, name='list-campaign'),
    path('show_campaign/<campaign_id>', views.show_campaign, name='show-campaigns'),
    path('search_camps', views.search_camps, name='search-camps'),
    path('update_campaign/<campaign_id>', views.update_campaign, name='update-campaign'),
    path('delete_campaign/<campaign_id>', views.delete_campaign, name='delete-campaign'),
    path('missing_campaign', views.update_missinginfo_camapign, name='update-missinginfo-campaign'),
]