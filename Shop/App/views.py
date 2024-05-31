from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product, Category, Review
from .serializers import ReviewSerializers, CategorySerializers, ProductSerializers
# Create your views here.



class ProductDetailView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def post(self,requset,*args,**kwargs):
        return self.create(requset,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)


class ReviewDetailView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, requset, *args, **kwargs):
        return self.create(requset, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class CategoryDetailView(generics.GenericAPIView,mixins.CreateModelMixin,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, requset, *args, **kwargs):
        return self.create(requset, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)