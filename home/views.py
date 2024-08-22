from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView
from .models import Car


class Home(View):
    # http_method_names = ["post"]

    def get(self, request):
        return render(request, "home/home.html")

    def options(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        response = super().options(request, *args, **kwargs)
        response.headers["host"] = "localhost"
        response.headers["user"] = request.user
        return response

    def post(self, request):
        return render(request, "home/home.html")

    def options(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        response = super().options(request, *args, **kwargs)
        response.headers["host"] = "localhost"
        response.headers["user"] = request.user
        return response

    def http_method_not_allowed(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        return render(request, "method_not_allowd.html")


class HomeView(TemplateView):
    template_name = "home/home_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cars"] = Car.objects.all()
        return context


class Two(RedirectView):
    # url = 'google.com' """ http://127.0.0.1:8000/two/google.com """
    # url = 'http://google.com'
    pattern_name = "home:home"

    query_string = True  # defaulte False : http://127.0.0.1:8000/home/?name=home

    def get_redirect_url(self, *args: Any, **kwargs: Any):
        print("*" * 90)
        print("proccessing your request...")
        return super().get_redirect_url(*args, **kwargs)


class HomeListView(ListView):
    template_name = "home/home_list_view.html"
    # model = Car # object_list
    # queryset = Car.objects.filter(year__gte = 2020)
    context_object_name = "cars"
    allow_empty = False  # default True: dont error

    def get_queryset(self) -> QuerySet[Any]:
        return Car.objects.filter(year__gte=2016)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = "jack"
        return context