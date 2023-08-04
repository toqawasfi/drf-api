from django.urls import path
from .views import PostsList, PostDetail, CommentList, CommentDetail

urlpatterns = [
    path('', PostsList.as_view(), name='Posts_List'),
    path('<int:pk>/', PostDetail.as_view(), name='Posts_Detail'),
    path('comment/', CommentList.as_view(), name='Comments_List'),
    path('comment/<int:pk>/', CommentDetail.as_view(), name='Comments_Detail')
]
