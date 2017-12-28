from django.db import models

# Create your models here.

# class BlogType(models.Model):


class GeneralBlog(models.Model):
    GENERAL_PYTHON = 'GP'
    DJANGO = 'DJ'
    BLOCKCHAIN = 'BC'
    DATA_SCIENCE = 'DS'
    ARTIFICIAL_INTELLIGENCE = 'AI'
    RANDOM_THOUGHTS = 'RT'

    POST_CAT=(
        ('GENERAL_PYTHON', 'General Python'),
        ('DJANGO', 'Django'),
        ('BLOCKCHAIN', 'Blockchain'),
        ('DATA_SCIENCE', 'Data Science'),
        ('ARTIFICIAL_INTELLIGENCE', 'AI'),
        ('RANDOM_THOUGHTS', 'Random Thoughts')
    )

    post_category=models.CharField(max_length=15, choices=POST_CAT, default='RANDOM_THOUGHTS')
    post_name=models.CharField(max_length=255)
    post_description=models.CharField(max_length=255)
    upload_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    post_content=models.FileField(upload_to='static/blogfiles', default=None)


    def __str__(self):
        return self.post_name



#class PythonBlog(models.model):
