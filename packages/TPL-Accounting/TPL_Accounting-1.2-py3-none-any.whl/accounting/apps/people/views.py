from django.views import generic
from django.urls import reverse
from accounting.apps.books.mixins import (
    RestrictToSelectedOrganizationQuerySetMixin,
    AutoSetSelectedOrganizationMixin
)
from .models import Client, Employee
from .forms import ClientForm, EmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientListView(
    LoginRequiredMixin,
    RestrictToSelectedOrganizationQuerySetMixin,
    generic.ListView
):
    template_name = "people/client_list.html"
    model = Client
    context_object_name = "clients"


class ClientCreateView(
    LoginRequiredMixin,
    AutoSetSelectedOrganizationMixin,
    generic.CreateView
):
    template_name = "people/client_create_or_update.html"
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("people:client-list")


class ClientUpdateView(
    LoginRequiredMixin,
    RestrictToSelectedOrganizationQuerySetMixin,
    AutoSetSelectedOrganizationMixin,
    generic.UpdateView
):
    template_name = "people/client_create_or_update.html"
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("people:client-list")


class ClientDetailView(
    LoginRequiredMixin,
    RestrictToSelectedOrganizationQuerySetMixin,
    generic.DetailView
):
    template_name = "people/client_detail.html"
    model = Client
    context_object_name = "client"


class EmployeeListView(
    LoginRequiredMixin,
    RestrictToSelectedOrganizationQuerySetMixin,
    generic.ListView
):
    template_name = "people/employee_list.html"
    model = Employee
    context_object_name = "employees"


class EmployeeCreateView(
    LoginRequiredMixin,
    AutoSetSelectedOrganizationMixin,
    generic.CreateView
):
    template_name = "people/employee_create_or_update.html"
    model = Employee
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse("people:employee-list")


class EmployeeUpdateView(
    LoginRequiredMixin,
    RestrictToSelectedOrganizationQuerySetMixin,
    AutoSetSelectedOrganizationMixin,
    generic.UpdateView
):
    template_name = "people/employee_create_or_update.html"
    model = Employee
    form_class = EmployeeForm

    def get_success_url(self):
        return reverse("people:employee-list")


class EmployeeDetailView(
    LoginRequiredMixin,
    RestrictToSelectedOrganizationQuerySetMixin,
    generic.DetailView
):
    template_name = "people/employee_detail.html"
    model = Employee
    context_object_name = "employee"
