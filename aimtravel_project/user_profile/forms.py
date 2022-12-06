from django import forms

from aimtravel_project.user_profile.models import Students, Employee

YES_NO_CHOICES = {
    ('yes', 'Yes'),
    ('no', 'No'),
}

"""
Below two forms are related with Student Model. 
They keep data needed for WAT program.
"""


class StudentEditForm(forms.ModelForm):
    is_received_visa = forms.BooleanField(required=False)
    is_fulltime_student = forms.BooleanField(required=False)
    date_of_birth = forms.DateField(
        required=False,
        input_formats=[
            '%d-%m-%y',
            '%d.%m.%y',
            '%Y-%m-%d',
            '%m/%d/%Y',
            '%m/%d/%y',
            '%b %d %Y',
            '%b %d, %Y',
            '%d %b %Y',
            '%d %b, %Y',
            '%B %d %Y',
            '%B %d, %Y',
            '%d %B %Y',
            '%d %B, %Y'],
        help_text='DD-MM-YYYY',
    )

    class Meta:
        model = Students
        exclude = ['user']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'Date of Birth'}),
            'place_of_birth': forms.TextInput(attrs={'placeholder': 'Place of Birth'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'province': forms.TextInput(attrs={'placeholder': 'Province'}),
            'street': forms.TextInput(attrs={'placeholder': 'Street'}),
            'bg_personal_number': forms.TextInput(attrs={'placeholder': 'EGN'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),
            'country_of_birth': forms.TextInput(attrs={'placeholder': 'Country of Birth'}),
            'id_passport_number': forms.TextInput(attrs={'placeholder': 'Passport Number'}),
            'passport_date_of_issue': forms.TextInput(attrs={'placeholder': 'Passport Date of Issue'}),
            'is_received_visa': forms.BooleanField(),
            'Phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'university': forms.TextInput(attrs={'placeholder': 'University Name'}),
            'year_of_education': forms.TextInput(attrs={'placeholder': 'Year of Education'}),
            'foreign_university': forms.TextInput(attrs={'placeholder': 'Foreign University'}),
            'is_fulltime_student': forms.BooleanField(),
            'search_job_pref': forms.TextInput(attrs={'placeholder': 'Preferable job'}),
            'how_to_reach': forms.TextInput(attrs={'placeholder': 'How to reach you?'}),
        }


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = Students
        exclude = ['user']


"""
Below two forms are related with Employee Model. 
They keep data related to the employees - can be seen on the 'about us' page.
"""


class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']


class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['user']
        widgets = {
            'employee_first_name': forms.TextInput(attrs={'placeholder': 'Име'}, ),
            'employee_last_name': forms.TextInput(attrs={'placeholder': 'Фамилия'}, ),
            'employee_role': forms.TextInput(attrs={'placeholder': 'Позиция'}, ),
            'employee_pic': forms.TextInput(attrs={'placeholder': 'Снимка URL'}, ),
            'employee_phone': forms.TextInput(attrs={'placeholder': 'Телефон'}, ),
            'employee_email': forms.TextInput(attrs={'placeholder': 'E-mail'}, ),
        }
