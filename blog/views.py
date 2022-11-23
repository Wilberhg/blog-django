from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.views.generic import ListView


# Versão utilizando classe
class PostListView(ListView):
    # model = Post
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# Versão utilizando método
# def post_list(request):
#     # Versão sem paginação
#     # posts = Post.published.all()
#     # posts = Post.objects.filter(status='published')
#     # return render(request, 'blog/post/list.html',{'posts': posts})

#     # Versão com paginação
#     # object_list = Post.published.all()
#     # paginator = Paginator(object_list, 3) # três postagens em cada página
#     # page = request.GET.get('page')
#     # try:
#     #     posts = paginator.page(page)
#     # except PageNotAnInteger:
#     #     # Se a página não for um inteiro, exibe a primeira página
#     #     posts = paginator.page(1)
#     # except EmptyPage:
#     #     # Se a página estiver fora do intervalo,
#     #     # exibe a última página de resultados
#     #     posts = paginator.page(paginator.num_pages)
#     # return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )