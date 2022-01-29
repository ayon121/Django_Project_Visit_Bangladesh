from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy  
from posts.models import Post ,Comment
from .forms import PostForm ,CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.
def LikePostView(request , pk):
    post = get_object_or_404(Post , id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse ('post' , args = [str(pk)]))


class PostView(ListView):
    model = Post
    template_name = 'posts.html'
    ordering = ['-post_date']
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    
    def get_context_data(self, *args , **kwargs):
        context = super(PostDetailView , self).get_context_data(*args , **kwargs)
        
        post= get_object_or_404(Post , id=self.kwargs['pk'])
        total_likes = post.total_likes()
        
        liked = False
        if post.likes.filter(id= self.request.user.id).exists():
            liked = True
        
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
    
        

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    
    #fields = '__all__'
    #fields = ('title','body' , 'author')
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    #fields = ('title' ,'body')
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('allposts') 
    
    

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html'
    ordering = ['-post_date']
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('allposts')
    
    