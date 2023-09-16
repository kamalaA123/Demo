from django.urls import path
from .import views

urlpatterns = [
    path('',views.test,name='test'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listtask/',views.listtask.as_view(),name='listtask'),
    path('detailtask/<int:pk>/',views.detailtask.as_view(),name='detailtask'),
    path('updatetask/<int:pk>/',views.updatetask.as_view(),name='updatetask'),
    path('deletetask/<int:pk>/',views.deletetask.as_view(),name='deletetask')
]