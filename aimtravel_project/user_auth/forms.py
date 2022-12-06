from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2')



    """
    No need of override save method if use signal
    """
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     profile = UserModel(user=user)
    #
    #     if commit:
    #         profile.save()
    #
    #     return user


class EditForm(auth_forms.UserChangeForm):
    fieldsets = (
        (None, {'fields': ("email", "password")}),
        ("Permissions", {'fields': ('is_staff', 'is_active', 'date_joined')})
    )

    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'email': auth_forms.UsernameField}
