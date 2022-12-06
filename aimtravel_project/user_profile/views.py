from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from aimtravel_project.user_profile.forms import StudentEditForm, StudentDetailsForm, EmployeeDetailsForm, EmployeeEditForm
from aimtravel_project.user_profile.models import Students, Employee

"""
Following two views are related to User Details page and functionality for editing regular(students) user Details.
All logged in users will be able to reach this page. 
"Staff" members will be able to reach this page as well typing the URL of the page.
"""


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentEditForm
    template_name = 'user_profile/edit_personal_profile.html'

    def get_success_url(self):
        student_pk = self.kwargs['pk']
        return reverse_lazy('details profile', kwargs={'pk': student_pk})


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Students
    template_name = 'user_profile/personal_profile.html'
    form_class = StudentDetailsForm


"""
Below two views are related to Employee profile page and functionality to edit employee profile details.
Only logged in as "Staff" members will be able to visit and edit this profile.
"""


class EmployeeProfileView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Employee
    permission_required = 'is_staff'
    template_name = 'user_profile/employee_profile.html'
    form_class = EmployeeDetailsForm


class EditEmployeeProfileView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    permission_required = 'is_staff'
    form_class = EmployeeEditForm
    template_name = 'user_profile/edit_employee_profile.html'

    def get_success_url(self):
        employee_pk = self.kwargs['pk']
        return reverse_lazy('employee profile details', kwargs={'pk': employee_pk})
