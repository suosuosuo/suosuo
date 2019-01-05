from django.shortcuts import render
from blog.models import Post


# Create your views here.
def index(request):
    list_data = Post.objects.all()# 获取所有数据
    list_data_star = Post.objects.filter(blog_type = 'star')
    return render(request, 
    	'index.html',
    	{'lists':list_data,'lists_star':list_data_star})



def about(request):
    return render(request, 'about.html')

def detail(request,id):
	data = Post.objects.get(id=id)
	return render(request,'detail.html',{'data':data})
def jingxuan(request,id):
	data = Post.objects.get(id=id)
	return render(request,'jingxuan.html',{'data':data})
