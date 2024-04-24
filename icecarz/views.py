from django.http import HttpResponse
from django.shortcuts import render
from adddata.models import *


def homePage(request):
    popular_brands = PopularBrands.objects.all()[:5]
    popular_cars = PopularCars.objects.all()[:4]
    data = {
        "title": "Home",
        "brands" : brands,
        'popular_brands' : popular_brands,
        'popular_cars' : popular_cars,
    }
    return render(request, "index.html", data)

def aboutus(request):
    return render(request, "aboutus.html")


def brands(request, brand_slug):
    brand = Brand.objects.get(slug=brand_slug)
    cars = Car.objects.filter(brand=brand)
    data={
        'brand': brand, 'cars': cars, 'title': brand.name
    }
    return render(request, "brands.html", data)


def allbrands(request):
    brands=Brand.objects.all()
    
    data = {
        "title": "Brands",
        "brands" : brands,
    }
    return render(request, "allbrands.html", data)


def carinfo(request, car_slug):
    car = Car.objects.get(slug=car_slug)
    carinfo = CarInfo.objects.get(car=car)
    data = {
        'car': car, 'carinfo': carinfo, 'title': car.name
    }
    return render(request, "carinfo.html", data)


def aboutUs(request):
    return render(request, "aboutUs.html")
