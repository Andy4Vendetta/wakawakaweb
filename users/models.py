from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(
        verbose_name='электронная почта',
        max_length=256,
        unique=True,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=50, 
        blank=False
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=50, 
        blank=False,
    )
    patronymic = models.CharField(
        verbose_name='отчество',
        max_length=50,
        blank=True,
    )
    phone_number = PhoneNumberField(
        verbose_name='номер телефона',
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True
    )
    customer = models.BooleanField(
        verbose_name='заказчик',
        default=False,
        blank=False,
    )
    staff = models.BooleanField(
        verbose_name='персонал',
        default=False,
        blank=False
    )
    admin = models.BooleanField(
        verbose_name='администратор',
        default=False,
        blank=False,
    )
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email

    @property
    def is_customer(self):
        return self.customer
    
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'