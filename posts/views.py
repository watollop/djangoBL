from urllib import quote_plus

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.utils import timezone
# Create your views here.


def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
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
    if instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context= {
        "title": instance.title,
        "obj": instance,
        "share_string": share_string
    }
    return render(request, "post_detail.html",context)

def posts_list(request):
    queryset_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
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



def posts_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
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
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Borrado")
    return redirect("posts:list")
