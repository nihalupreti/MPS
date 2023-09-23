from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View


class Base(View):
    views = {}


class HomeView(Base):

    def get(self, request):
        self.views['sellings'] = TopSelling.objects.all
        return render(request, 'index-2.html', self.views)


class About(Base):

    def get(self, request):
        return render(request, 'about-us.html', self.views)


class Blog(Base):

    def get(self, request):
        return render(request, 'blog.html', self.views)


class BlogDetails(Base):

    def get(self, request):
        return render(request, 'blog-details.html', self.views)


class Cart(Base):

    def get(self, request):
        return render(request, 'cart.html', self.views)


class Checkout(Base):

    def get(self, request):
        return render(request, 'checkout.html', self.views)


class Contact(Base):

    def get(self, request):
        return render(request, 'contact-us.html', self.views)


class Error(Base):

    def get(self, request):
        return render(request, 'error404.html', self.views)


class Shop(Base):

    def get(self, request):
        return render(request, 'shop.html', self.views)


class LoginRegister(Base):

    def get(self, request):
        return render(request, 'login-register.html', self.views)