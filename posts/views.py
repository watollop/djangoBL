from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# Create your views here.


def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Creado")
        return HttpResponseRedirect(instance.get_absolut_url())
    else:
        messages.error(request, "Error creando")
    context = {
        "form": form,
    }
    return render(request, "post_form.html",context)

def posts_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context= {
        "title": instance.title,
        "obj": instance
    }
    return render(request, "post_detail.html",context)

def posts_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "title",
        "object_list": queryset
    }
    return render(request, "post_list.html", context)




def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Guardado")
        return HttpResponseRedirect(instance.get_absolut_url())
    context= {
        "title": instance.title,
        "obj": instance,
        "form": form,
    }
    return render(request, "post_form.html",context)

def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Borrado")
    return redirect("posts:list")
