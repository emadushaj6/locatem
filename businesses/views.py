from django.shortcuts import render, get_object_or_404
from .models import Category, Business
from .forms import ContactForm


def home(request):
    categories = Category.objects.all()
    for category in categories:
        category.business_count = category.business_set.count()

    featured_businesses = Business.objects.filter(
        is_featured=True, is_active=True)[:4]

    business_count = Business.objects.count()

    context = {
        'categories': categories,
        'featured_businesses': featured_businesses,
        'business_count': business_count,
    }
    return render(request, 'home.html', context)


def categories(request):
    categories = Category.objects.all()
    for category in categories:
        category.business_count = category.business_set.count()
    return render(request, 'categories.html', {'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    businesses = Business.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'businesses': businesses})


def business_detail(request, slug):
    business = get_object_or_404(Business, slug=slug)
    return render(request, 'business_detail.html', {'business': business})


def plans(request):
    return render(request, 'plans.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally add email sending here
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    return render(request, 'contact.html', {'form': form})
