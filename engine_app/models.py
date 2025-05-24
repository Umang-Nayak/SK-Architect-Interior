import os
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver


class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Feedback(Base):
    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ]
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=False, blank=False)
    rating = models.IntegerField(choices=RATING_CHOICES)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    user_phone_number = PhoneNumberField(null=False, blank=False, region='IN')

    class Meta:
        db_table = 'feedback'
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        return f'{self.id}'


class Project(Base):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ongoing')
    location = models.CharField(max_length=255, null=True, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    project_image = models.ImageField(upload_to='engine_app/project_gallery/', null=True, blank=True)

    class Meta:
        db_table = 'project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f"{self.id} - {self.name}"


@receiver(models.signals.post_delete, sender=Project)
def delete_project_image(sender, instance, **kwargs):
    if instance.project_image:
        if os.path.isfile(instance.project_image.path):
            os.remove(instance.project_image.path)


class ProjectGallery(Base):
    project = models.ForeignKey(Project, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='engine_app/project_images/')
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'project_gallery'
        verbose_name = 'Project Gallery'
        verbose_name_plural = 'Project Galleries'

    def __str__(self):
        return f"{self.id} - {self.name or 'Untitled Image'}"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


class Contact(Base):
    name = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"{self.id} - {self.subject}"

