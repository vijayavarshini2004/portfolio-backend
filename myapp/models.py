from django.db import models

# Profile Model
class Profile(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name

# About Section Model
class About(models.Model):
    point_1 = models.TextField()
    point_2 = models.TextField()
    point_3 = models.TextField()
    point_4 = models.TextField()

    def __str__(self):
        return self.point_1

# Skills Model
class Skill(models.Model):
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return str(self.icon)

# Projects Model
class Project(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=255)
    demo_video = models.FileField(upload_to='videos/')
    project_overview = models.TextField()
    tech_stack_used = models.TextField()
    key_features = models.TextField()
    challenges_faced = models.TextField()
    use_cases = models.TextField()
    future_enhancements = models.TextField()
    repository_link = models.URLField()
    documentation = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title

# HomePage Model
class HomePage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# HomePageProject Model
class HomePageProject(models.Model):
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='home_projects')
    project_title = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='homepage_projects/')

    def __str__(self):
        return self.project_title
