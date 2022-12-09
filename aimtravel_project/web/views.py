from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from aimtravel_project.user_profile.models import Employee
from aimtravel_project.web.forms import JobOfferDetailForm, CompanyDetailForm, CompanyEditForm, PriceDetailForm
from aimtravel_project.web.models import JobOffer, Prices, AdditionalServices, Company


# Create your views here.

def index(request):
    return render(request, template_name='index.html')


def admin_panel(request):
    return render(request, template_name='admin_panel.html')


class CreateOfferView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    fields = '__all__'
    model = JobOffer
    template_name = 'job_offer/add_offer.html'
    success_url = reverse_lazy('offers')


class DisplayOfferView(views.ListView):
    model = JobOffer
    template_name = 'job_offer/offers.html'
    context_object_name = 'offer_list'
    paginate_by = 4
    ordering = ('-ranking', '-wage',)


class DetailsOfferView(views.DetailView):
    model = JobOffer
    template_name = 'job_offer/details_offer.html'
    form_class = JobOfferDetailForm
    context_object_name = 'offer_details'


class EditOfferView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    model = JobOffer
    fields = '__all__'
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'job_offer/edit_offer.html'
    context_object_name = 'edit_offer'

    def get_success_url(self):
        offer_pk = self.kwargs['pk']
        return reverse_lazy('details offer', kwargs={'pk': offer_pk})


class DeleteOfferView(LoginRequiredMixin, PermissionRequiredMixin, views.DeleteView):
    model = JobOffer
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'job_offer/delete_offer.html'
    context_object_name = 'delete_offer'
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('offers')


class CreatePriceView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = ('is_superuser',)
    permission_denied_message = 'Нямаш необходимите права.'
    fields = '__all__'
    model = Prices
    template_name = 'price/add_price.html'
    success_url = reverse_lazy('prices')


class DisplayPricesView(views.ListView):
    model = Prices
    ordering = ['price']
    template_name = 'price/prices.html'
    context_object_name = 'prices_list'


class EditPriceView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    model = Prices
    fields = '__all__'
    permission_required = ('is_superuser',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'price/edit_price.html'
    context_object_name = 'edit_price'

    def get_success_url(self):
        price_pk = self.kwargs['pk']
        return reverse_lazy('details price', kwargs={'pk': price_pk})


class DetailsPriceView(views.DetailView):
    model = Prices
    template_name = 'price/details_price.html'
    form_class = PriceDetailForm
    context_object_name = 'price_details'


class DeletePriceView(LoginRequiredMixin, PermissionRequiredMixin, views.DeleteView):
    model = Prices
    permission_required = ('is_superuser',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'price/delete_price.html'
    context_object_name = 'delete_price'
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('prices')


class DisplayAdditionalServicesView(views.ListView):
    model = AdditionalServices
    template_name = 'additional_services/additional_services.html'
    context_object_name = 'services_list'


class AllEmployeeView(views.ListView):
    model = Employee
    template_name = 'about_us/team.html'
    context_object_name = 'employee_list'


class CreateCompanyView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    fields = '__all__'
    model = Company
    template_name = 'employer/add_employer.html'
    success_url = reverse_lazy('view all employer')


class CompanyDetailView(views.DetailView):
    model = Company
    template_name = 'employer/details_employer.html'
    form_class = CompanyDetailForm
    context_object_name = 'employer_details'


class AllCompanyView(views.ListView):
    model = Company
    template_name = 'employer/view_all.html'
    context_object_name = 'employers'
    paginate_by = 4
    ordering = 'employer_name'


class EditCompanyView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    model = Company
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'employer/edit_employer.html'
    context_object_name = 'edit_employer'
    form_class = CompanyEditForm

    def get_success_url(self):
        emp_pk = self.kwargs['pk']
        return reverse_lazy('employer details', kwargs={'pk': emp_pk})


class DeleteCompanyView(LoginRequiredMixin, PermissionRequiredMixin, views.DeleteView):
    model = Company
    permission_required = ('is_staff',)
    permission_denied_message = 'Нямаш необходимите права.'
    template_name = 'employer/delete_employer.html'
    context_object_name = 'delete_company'
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('view all employer')
