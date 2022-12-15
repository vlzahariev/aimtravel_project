from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Students(models.Model):
    user = models.OneToOneField(
        UserModel,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=15,
        verbose_name='Име',
        blank=True,
        null=True,
        default='',
    )
    middle_name = models.CharField(
        default="",
        max_length=15,
        verbose_name='Презиме',
        blank=True,
        null=True,

    )
    last_name = models.CharField(
        max_length=15,
        verbose_name='Фамилия',
        blank=True,
        null=True,
        default='',
    )
    date_of_birth = models.DateField(
        verbose_name='Дата на раждане',
        help_text='dd-mm-yyyy',
        blank=True,
        null=True,
    )
    place_of_birth = models.CharField(
        verbose_name='Място на раждане',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    city = models.CharField(
        verbose_name='Град',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    province = models.CharField(
        verbose_name='Област',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    street = models.CharField(
        verbose_name='Улица/ж.к.',
        max_length=30,
        blank=True,
        null=True,
        default='',
    )
    bg_personal_number = models.CharField(
        max_length=15,
        verbose_name='ЕГН',
        blank=True,
        null=True,
        default='',
    )
    nationality = models.CharField(
        verbose_name='Националност',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    country_of_birth = models.CharField(
        verbose_name='Държава на раждане',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )

    id_passport_number = models.CharField(
        verbose_name='Номер на паспорт',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    passport_date_of_issue = models.DateField(
        verbose_name='Дата на издаване',
        blank=True,
        null=True,
    )
    is_received_visa = models.BooleanField(
        verbose_name='Получена виза',
        blank=True,
        null=True,
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    email = models.CharField(
        verbose_name='E-mail',
        max_length=40,
        blank=True,
        null=True,
        default='',
    )
    university = models.CharField(
        verbose_name='Университет',
        max_length=30,
        blank=True,
        null=True,
        default='',
    )
    year_of_education = models.PositiveIntegerField(
        default='',
        verbose_name='Курс',
        blank=True,
        null=True,
    )
    foreign_university = models.CharField(
        verbose_name='Чуждестранен университет',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    is_fulltime_student = models.BooleanField(
        verbose_name='Студент "Редовно обучение"',
        blank=True,
        null=True,
    )
    search_job_pref = models.CharField(
        verbose_name='Предпочитана работа',
        default='',
        max_length=15,
        blank=True,
        null=True,
    )
    how_to_reach = models.CharField(
        verbose_name='Как да комуникираме?',
        max_length=15,
        blank=True,
        null=True,
        default='',
    )
    visa_photo = models.URLField(
        verbose_name='Снимка за ВИЗА',
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
        default='https://media.istockphoto.com/id/1300845620/vector/user-icon-flat-isolated-on-white-background-user-symbol-vector-illustration.jpg?s=612x612&w=0&k=20&c=yBeyba0hUkh14_jgv1OKqIH0CCSWU_4ckRkAoy2p73o=',
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
    is_staff = models.BooleanField(
        default=True,
        blank=False,
        null=False,
    )

    """
    *edited*
    Below signal not to be used. To avoid creating two separate instances of Employee model and Student Model 
    to same AppUser instance, If employee user needs to be created, super user will create instance of AppUser,
    and then manually delete automatically created Student Model, and manually create Employee Model, assigning 
    manually the user to the model.

    Above 'Signal' is placed to create 'Employee' (staff user) instance. 
    Can be filled later by the employee/superuser. 
    """
    # @receiver(post_save, sender=UserModel)
    # def create_profile(sender, instance, created, *args, **kwargs):
    #     if created:
    #         Employee.objects.created(user=instance)



