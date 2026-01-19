from rest_framework import serializers
from .models import Courses



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields=('course_name','price','duration','certificate','course_img','short_description','description','levels',
                'instrctor_name','total_students','rating')
        

        


    


