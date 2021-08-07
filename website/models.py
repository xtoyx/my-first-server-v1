from django.db import models

# Create your models here.
class ProjectsIdea(models.Model):
    Project_Name               =models.CharField(max_length=50)
    Desprecent          =models.TextField()
    url                 =models.CharField(max_length=50)
    Date_started        =models.CharField(max_length=10)
    website_uploaded_project=models.CharField(max_length=10)


    def __str__(self):
        return self.Project_Name + ' ' + self.website_uploaded_project
        #toseeitgood


class PrecentCHECKD(models.Model):
    Python_p            =models.IntegerField()
    CyberSecruity_p     =models.IntegerField()
    Web_p               =models.IntegerField()
    Andriod_p           =models.IntegerField()

    

    def __str__(self):
        return 'Precents'