from django.db import models

#create a blog model

#title
#pub_date
#body
#image

class Blog(models.Model):
    title =  models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

#add the blog app in setting

#create a migration

#migrate

#add to the admin

