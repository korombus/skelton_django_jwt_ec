from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, last_name=None, address=None, tel_number=None):
        if not email:
            raise ValueError('Users must have an email.')

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            address=address,
            tel_number=tel_number
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('メールアドレス', unique=True)
    first_name = models.CharField('姓', max_length=255)
    last_name = models.CharField('名', max_length=255)
    address = models.CharField('住所', max_length=255, blank=True)
    tel_number = models.CharField('電話番号', max_length=30, blank=True)
    created = models.DateTimeField('入会日', default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    


