from django.urls import path

from blogs.views import blogs_view, blog_details_view

urlpatterns = [
    path('', blogs_view, name='blogs'),
    path('<int:blog_id>/', blog_details_view, name='blog-details'),
]
