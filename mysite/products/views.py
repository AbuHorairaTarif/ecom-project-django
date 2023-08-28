from django.utils import timezone

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product, ProductReview
from .forms import ProductReviewForm

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        queryset = Product.objects.all()
        if search_query:
            queryset = queryset.filter(Q(name__icontains=search_query))
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['product']
        context['reviews'] = product.productreview_set.all()
        context['form'] = ProductReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.comment_date = timezone.now()
            review.save()
            return redirect('products:product_detail', pk=product.pk)
        else:
            # Handle invalid form data here
            pass
