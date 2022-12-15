from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic as views

from aimtravel_project.user_profile.forms import StudentEditForm, StudentDetailsForm, EmployeeDetailsForm, \
    EmployeeEditForm
from aimtravel_project.user_profile.models import Students, Employee

UserModel = get_user_model()

"""
Following two views are related to User Details page and functionality for editing regular(students) user Details.
All logged in users will be able to reach this page. 
"Staff" members will be able to reach this page as well typing the URL of the page.
"""


class EditUserProfileView(LoginRequiredMixin, views.UpdateView):
    model = Students
    form_class = StudentEditForm
    template_name = 'user_profile/edit_personal_profile.html'
    context_object_name = 'students'

    def get_success_url(self):
        student_pk = self.kwargs['pk']
        return reverse_lazy('details profile', kwargs={'pk': student_pk})


class UserProfileView(LoginRequiredMixin, views.DetailView):
    model = Students
    template_name = 'user_profile/personal_profile.html'
    form_class = StudentDetailsForm


"""
Below two views are related to Employee profile page and functionality to edit employee profile details.
Only logged in as "Staff" members will be able to visit and edit this profile.
"""


class EmployeeProfileView(LoginRequiredMixin, UserPassesTestMixin, views.DetailView):
    model = Employee
    template_name = 'user_profile/employee_profile.html'
    form_class = EmployeeDetailsForm

    def test_func(self):
        return self.request.user.is_staff


class EditEmployeeProfileView(LoginRequiredMixin, UserPassesTestMixin, views.UpdateView):
    model = Employee
    permission_required = 'is_staff'
    form_class = EmployeeEditForm
    template_name = 'user_profile/edit_employee_profile.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        employee_pk = self.kwargs['pk']
        return reverse_lazy('employee profile details', kwargs={'pk': employee_pk})


class AllUsersView(LoginRequiredMixin, UserPassesTestMixin, views.ListView):
    model = Students
    template_name = 'user_profile/all_students.html'
    context_object_name = 'student_list'
    ordering = 'first_name'
    paginate_by = 2

    def test_func(self):
        return self.request.user.is_staff
