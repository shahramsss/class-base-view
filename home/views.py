from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import (
    TemplateView,
    RedirectView,
    ListView,
    DetailView,
    FormView,
    CreateView , 
    DeleteView,
)
from .models import Car
from .forms import CarCreateForm
from django.urls import reverse_lazy
from django.contrib import messages


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
        return Car.objects.filter(year__gte=2000)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["name"] = "jack"
        return context


class Detail(DetailView):
    template_name = "home/detail.html"
    # model = Car # object
    # # context_object_name = "car"
    # slug_field = 'name'
    # slug_url_kwarg = "my_slug"
    # # pk_url_kwarg = 'id' # default: pk
    # # queryset = Car.objects.filter(year__gte = 2016)

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Car.objects.filter(name = self.kwargs['my_slug'])
    #     else:
    #         return Car.objects.none()

    def get_object(self, queryset=None):
        return Car.objects.get(
            name=self.kwargs["name"],
            owner=self.kwargs["owner"],
            year=self.kwargs["year"],
        )


class Create(FormView):
    template_name = "home/create.html"
    form_class = CarCreateForm
    success_url = reverse_lazy("home:homelistview")

    def form_valid(self, form):
        self._create_car(form.cleaned_data)
        messages.success(self.request, " created car successfully", "success")
        return super().form_valid(form)

    def _create_car(self, data):
        return Car.objects.create(
            name=data["name"], owner=data["owner"], year=data["year"]
        )


class CarCreateView(CreateView):
    model = Car 
    fields = ['name' , 'year']
    success_url = reverse_lazy("home:homelistview")
    template_name = "home/create.html"

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = self.request.user.username if self.request.user.username else 'nothing'
        car.save()
        messages.success(self.request, " created car successfully", "success")
        return super().form_valid(form)



class CarDeleteView(DeleteView):
    model = Car # object
    success_url = reverse_lazy("home:homelistview")
    template_name = "home/delete.html"