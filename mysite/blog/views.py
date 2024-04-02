from .models import Post
from django.http import HttpResponse, Http404


# Create your views here.

def list(request):
    post_list = Post.objects.all()
    
    titles = ''
    
    for post in post_list:
        titles += post.title
    
    return HttpResponse(titles)

def detail(request,id):
    try:
        post = Post.objects.get(id=id)
        
    except Post.DoesNotExist:
        raise Http404("존재하지 않는 데이터 입니다.")
    
    return HttpResponse(post.title)