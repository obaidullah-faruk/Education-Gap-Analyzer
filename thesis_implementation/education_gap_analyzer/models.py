from django.db import models


class UniversityCurriculum(models.Model):
    universityName=models.CharField(max_length=50)
    deptName=models.CharField(max_length=50)
    courseName=models.CharField(max_length=50)
    courseContent=models.TextField()
    courseKeyword=models.TextField(null=True)

    def __str__(self):
        return self.universityName


class jobData(models.Model):
    jobTitle=models.CharField(max_length=70)
    category=models.CharField(max_length=40)
    jobRequirments=models.TextField()
    relatedDept=models.CharField(max_length=50)
    keywords=models.TextField()

    def __str__(self):
        return self.jobTitle