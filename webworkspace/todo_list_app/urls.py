from django.urls import path
from todo_list_app import views

urlpatterns = [
        path('todo/',
            views.index, name='index'),
        path('todo/about/',
            views.about, name='about'),
        path('todo/planner/',
            views.planner, name='planner'),
        path('todo/planner/edit/<int:todo_id>/',
            views.edit_todo, name='edit_todo'),
        path('todo/planner/delete/<int:todo_id>/',
            views.delete_todo, name='delete_todo'),
        ]
