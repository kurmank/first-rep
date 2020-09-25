from django.views.generic import (
    ListView, 
    DeleteView, 
    DetailView, 
    UpdateView,
    CreateView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Review
from django.urls import reverse_lazy

class ReviewListView(LoginRequiredMixin, ListView):
    model = Review
    template_name='review_list.html'
    context_object_name='review_list'
    login_url = 'login'

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name='review_delete.html'
    success_url=reverse_lazy('review_list')
    context_object_name='review'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    template_name='review_edit.html'
    fields = ('film_name', 'actors', 'body')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    template_name='review_detail.html'
    context_object_name = 'review'
    login_url = 'login'

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ('film_name', 'body', 'actors')
    login_url = 'login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)