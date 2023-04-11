from django.contrib import admin
from django.urls import path
from django.views import generic
from django.contrib.auth.models import User
from MyApp.views import ContactCreateView, ContactListView, ContactDeleteView, ContactUpdateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('contact/add/', ContactCreateView.as_view(), name='contact-create'),
    path('list', ContactListView.as_view(), name='contact-list'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


