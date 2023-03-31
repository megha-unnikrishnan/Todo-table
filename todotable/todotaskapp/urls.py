from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:updateid>/',views.update,name='update'),
    path('listview',views.Listview.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.Detailview.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.Updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.Deleteview.as_view(),name='deleteview'),
    path('createview',views.Createview.as_view(),name='createview')
]