from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blogs.forms import BlogsForm, AutorForm
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
        BlogForset = inlineformset_factory(Blog, Autor, AutorForm, extra=1)
        if self.request.metod == 'POST':
            context_data['formset'] = BlogForset(self.request.POST, instance=self.object)



class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogsForm
    success_url = reverse_lazy("blogs:blog_list")

    def form_valid(self, form):
        blog = form.save()
        user = self.request.user
        blog.autor = user
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
        BlogForset = inlineformset_factory(Blog, Autor, AutorForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = BlogForset(self.request.POST, instance=self.object)
            pass


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")




