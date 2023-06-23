from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from cryptography.fernet import Fernet


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PasswordGroup(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, through='PasswordShare')

    def __str__(self):
        return self.name


class Password(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group = models.ForeignKey(PasswordGroup, on_delete=models.CASCADE, null=True, blank=True)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    encrypted_password = models.BinaryField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+",)

    def __str__(self):
        return self.username
    
    def get_decrypted_password(self):
        fernet = Fernet(self.user.profile.encryption_key)
        decrypted_password = fernet.decrypt(self.encrypted_password).decode()
        return decrypted_password


class PasswordShare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password_group = models.ForeignKey(PasswordGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.password_group.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    encryption_key = models.BinaryField()

    @staticmethod
    def generate_encryption_key():
        return Fernet.generate_key()

    @property
    def encrypted_key(self):
        return Fernet(self.encryption_key)

    def save(self, *args, **kwargs):
        if not self.encryption_key:
            self.encryption_key = self.generate_encryption_key()
        super().save(*args, **kwargs)
