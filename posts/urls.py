from django.urls import path
from .views import PostView , PostDetailView ,PostCreateView ,UpdatePostView , DeletePostView ,LikePostView ,CommentCreateView

urlpatterns = [
    path('allposts' ,PostView.as_view() , name= 'allposts' ),
    path('post/<int:pk>' ,PostDetailView.as_view() , name= 'post' ),
    path('createpost' ,PostCreateView.as_view() , name= 'createpost' ),
    path('updatepost/<int:pk>' , UpdatePostView.as_view() , name= 'updatepost' ),
    path('deletepost/<int:pk>/remove' , DeletePostView.as_view() , name= 'deletepost' ),
    path('likepost/<int:pk>' ,LikePostView, name= 'likepost' ),
    path('comment/<int:pk>' ,CommentCreateView.as_view(), name= 'comment' ),
    
      
    
      
]


