# Relacja wiele do wielu w Django

## 1. Co to jest relacja wiele do wielu?
Relacja wiele do wielu (ManyToManyField) oznacza, że wiele rekordów w jednej tabeli może być powiązanych z wieloma rekordami w drugiej tabeli.

## 2. Kiedy warto stosować relację wiele do wielu?
- **Modelowanie zależności N:N** – np. jeden student może uczęszczać na wiele kursów, a każdy kurs może mieć wielu studentów.
- **Optymalizacja struktury danych** – unikanie duplikacji rekordów poprzez tworzenie tabeli pośredniczącej.
- **Łatwe pobieranie powiązanych rekordów** – Django automatycznie zarządza relacją przez tabelę pośredniczącą.

## 3. Przykład użycia relacji wiele do wielu w Django

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, related_name='courses')
    
    def __str__(self):
        return self.title
```

W powyższym przykładzie jeden student może być zapisany na wiele kursów, a każdy kurs może mieć wielu studentów.

## 4. Dodawanie i pobieranie danych

Dodawanie studenta do kursu:

```python
student = Student.objects.create(name='John Doe')
course = Course.objects.create(title='Python Basics')

course.students.add(student)  # Dodanie studenta do kursu
```

Pobieranie kursów, na które zapisał się student:

```python
student = Student.objects.get(name='John Doe')
courses = student.courses.all()
```

Pobieranie studentów zapisanych na dany kurs:

```python
course = Course.objects.get(title='Python Basics')
students = course.students.all()
```

## 5. Optymalizacja zapytań

### a) Użycie `prefetch_related` do optymalizacji pobierania powiązanych rekordów
Bez `prefetch_related`, Django wykonuje osobne zapytanie dla każdego powiązanego obiektu:

```python
students = Student.objects.all()
for student in students:
    courses = student.courses.all()  # Każde wywołanie generuje osobne zapytanie!
    print(courses)
```

Rozwiązanie:

```python
students = Student.objects.prefetch_related('courses').all()
for student in students:
    courses = student.courses.all()  # Wszystkie kursy są pobierane w jednym zapytaniu
    print(courses)
```

### b) Użycie `through` do pełnej kontroli nad relacją
Możemy stworzyć własny model pośredniczący, np. z dodatkowymi informacjami o zapisach:

```python
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
```

Następnie zmieniamy pole `ManyToManyField`:

```python
class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, through='Enrollment', related_name='courses')
```

Teraz możemy dodać studenta do kursu z dodatkowymi informacjami:

```python
Enrollment.objects.create(student=student, course=course, enrollment_date='2024-01-01')
```

## 6. Podsumowanie
- `ManyToManyField` pozwala na modelowanie relacji wiele do wielu.
- `prefetch_related` optymalizuje zapytania do bazy danych.
- Można użyć modelu pośredniczącego (`through`), jeśli potrzebne są dodatkowe informacje o relacji.
- Django automatycznie zarządza tabelą pośredniczącą, ale można ją dostosować do własnych potrzeb.

