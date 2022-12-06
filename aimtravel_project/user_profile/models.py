from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


class Students(models.Model):
    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=15,
        verbose_name='First name',
        blank=True,
        null=True,
        default='',
    )
    middle_name = models.CharField(
        max_length=15,
        verbose_name='Middle name',
        blank=True,
        null=True,
        default='',
    )
    last_name = models.CharField(
        max_length=15,
        verbose_name='Last name',
        blank=True,
        null=True,
        default='',
    )
    date_of_birth = models.DateField(
        verbose_name='Date of birth',
        help_text='dd-mm-yyyy',
        blank=True,
        null=True,
    )
    place_of_birth = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    city = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    province = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    street = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default='',
    )
    bg_personal_number = models.CharField(
        max_length=15,
        verbose_name='EGN',
        blank=True,
        null=True,
        default='',
    )
    nationality = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    country_of_birth = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )

    id_passport_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    passport_date_of_issue = models.DateField(
        blank=True,
        null=True,
    )
    is_received_visa = models.BooleanField(
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    email = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        default='',
    )
    university = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        default='',
    )
    year_of_education = models.PositiveIntegerField(
        help_text='Semester',
        blank=True,
        null=True,
    )
    foreign_university = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    is_fulltime_student = models.BooleanField(
        blank=True,
        null=True,
    )
    search_job_pref = models.CharField(
        default='',
        max_length=15,
        blank=True,
        null=True,
    )
    how_to_reach = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    visa_photo = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )

    def __str__(self):
        name_str = f"{self.user}\n"
        if self.first_name:
            name_str += '\n' + '-' + '\n' + self.first_name
        if self.last_name:
            name_str += '\n' + self.last_name
        return name_str

    @receiver(post_save, sender=UserModel)
    def create_profile(sender, instance, created, *args, **kwargs):
        if created:
            Students.objects.create(user=instance)


"""
Above 'Signal' is placed to create 'Student' (regular user) instance. 
Can be filled later by the student/employee/superuser. 
"""


class Employee(models.Model):
    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    employee_first_name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    employee_last_name = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    employee_role = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    employee_pic = models.URLField(
        max_length=200,
        blank=True,
        null=True,
    )
    employee_phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    employee_email = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )

    @receiver(post_save, sender=UserModel)
    def create_profile(sender, instance, created, *args, **kwargs):
        if created:
            Employee.objects.create(user=instance)


"""
Above 'Signal' is placed to create 'Employee' (staff user) instance. 
Can be filled later by the employee/superuser. 
"""
