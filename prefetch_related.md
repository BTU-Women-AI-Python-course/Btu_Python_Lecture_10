# prefetch_related

**Purpose**: 
  - Used for multi-valued relationships, such as ManyToManyField and Reverse ForeignKey (One-to-Many).

**How It Works**:
  - Executes separate queries for each relationship and joins them in Python.

**Benefit**:
  - Optimizes queries by reducing the number of database hits, especially with large related datasets.

## Example Scenario

Consider the following models:

### `models.py`

```python
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='students')
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

**Relationships**:
  - Each Student belongs to one Department.
  - Each Student can enroll in multiple Courses.
  - Each Course belongs to one Department.

## Without `prefetch_related`:

```python
# views.py

from django.shortcuts import render
from .models import Student

def student_courses(request):
    students = Student.objects.all()
    for student in students:
        courses = student.courses.all()  # Triggers a separate query per student
        for course in courses:
            print(course.title)
    return render(request, 'students/courses.html', {'students': students})
```
**Issue**: This results in 1 + N queries:
  - 1 query to fetch all students.
  - N queries to fetch courses for each student.

## With `prefetch_related`:

```python
# views.py

from django.shortcuts import render
from .models import Student

def student_courses(request):
    students = Student.objects.prefetch_related('courses').all()
    for student in students:
        courses = student.courses.all()  # No additional queries
        for course in courses:
            print(course.title)
    return render(request, 'students/courses.html', {'students': students})
```
**Benefit**: Only 2 queries are executed:
  - Fetch all students.
  - Fetch all related courses for those students.
