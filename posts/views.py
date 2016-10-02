from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.


def posts_create(request):
    form = PostForm(request.POST or None)
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

def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context= {
        "title": instance.title,
        "obj": instance
    }
    return render(request, "post_detail.html",context)

def posts_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "title",
        "object_list": queryset
    }
    return render(request, "index.html", context)


def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
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

def posts_delete(request):
    return HttpResponse("<h1> delete </h1>")
