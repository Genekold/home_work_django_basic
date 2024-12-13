from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blogs.forms import BlogsForm, AutorForm, BlogsModeratorForm
from blogs.models import Blog, Autor


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        BlogForsetUpdate = inlineformset_factory(Blog, Autor, AutorForm, extra=1)
        context_data['formset'] = BlogForsetUpdate(instance=self.object)
        return context_data


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogsForm
    success_url = reverse_lazy("blogs:blog_list")

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.creator = user
        blog.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogsForm
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        BlogFormset = inlineformset_factory(Blog, Autor, AutorForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = BlogFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = BlogFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.creator:
            return BlogsForm
        if user.has_perm("blogs.can_unpublish_blog"):
            return BlogsModeratorForm
        raise PermissionDenied


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        user = self.request.user
        if user == self.object.creator or user.groups.filter(name='moderator').exists():
            self.object.delete()
            return HttpResponseRedirect(success_url)
        raise PermissionDenied


