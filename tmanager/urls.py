from django.urls import path,include
from .views import *

urlpatterns = [
    # users
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    # tickets
    path('ticket/<int:pk>/',TicketDetails.as_view(),name='ticket-details'),
    path('tickets/',TicketsList.as_view(),name='tickets-list'),
    path('ticket/<int:pk>/add_comment/',CreateComment.as_view(),name='create-comment'),
    path('ticket/<int:pk>/add_tracking/',CreateTracking.as_view(),name='add-tracking'),
    # comments
    path('comment/<int:pk>/update/',CommentUpdate.as_view(),name='update-comment'),
    path('comment/<int:pk>/delete/',CommentDelete.as_view(),name='delete-comment'),
    # status
    path('status/',StatusList.as_view(),name='status-list'),
    path('status/<int:pk>/',StatusDetails.as_view(),name='status-details'),
    # api-auth
    path('api-auth/', include('rest_framework.urls')),
]