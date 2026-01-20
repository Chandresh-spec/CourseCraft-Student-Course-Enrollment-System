from django.db import models

# Create your models here.


class Courses(models.Model):
    LEVEL_CHOICES=(
        ('beginner','Beginner'),
        ('intermediate','Intermedaite'),
        ('advanced','Advanced'),
    )
    course_name=models.CharField(max_length=100,null=False,blank=False)
    price=models.DecimalField(max_digits=8,decimal_places=2)

    duration=models.IntegerField()
    certificate=models.BooleanField(default=True)

    course_img=models.ImageField(upload_to='course_img',null=True,blank=True)
    short_description=models.CharField(max_length=150)

    description=models.TextField()
    levels=models.CharField(max_length=20,choices=LEVEL_CHOICES)

    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    instrctor_name=models.CharField(max_length=100)
    total_students=models.PositiveIntegerField(default=0)
    rating=models.DecimalField(max_digits=2,decimal_places=1,default=0.0)


    def __str__(self):
        return  self.course_name