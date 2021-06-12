from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('home', views.home),
    path('post', views.create_post),
    path('post-comment/<int:post_id>', views.post_comment),
    path('delete/<int:id>', views.delete_comment),
    path('remove-post/<int:id>', views.delete_post),
    path('like/<int:id>', views.add_like),
    path('like-comment/<int:id>', views.like),
    path('food',views.food),

    path('create_food',views.create_food),
    
    path('post_food',views.post_food),

    path('food/<int:food_id>/edit', views.edit),
    path('food/<int:food_id>/update', views.update),
    path('food/<int:food_id>/delete', views.delete),
]
