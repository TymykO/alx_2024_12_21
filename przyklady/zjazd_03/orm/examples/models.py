from django.db import models


# example 1 to 1

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.phone_number:
            return f"{self.user.username} - {self.phone_number}"
        return f"{self.user.username}"

# example 1 to many

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    

# example many to many


class Enrollment(models.Model):
    student = models.ForeignKey("examples.Student", on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey("examples.Course", on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.name} - {self.course.title}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='courses', through=Enrollment)
    
    def __str__(self):
        return self.title
    

# example for database views

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.author.name})"
    

class BookSummary(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        managed = False  # Django nie będzie zarządzać tym modelem
        db_table = 'book_summary'  # Nazwa widoku w bazie danych

    def __str__(self):
        return f"{self.title} ({self.author_name})"