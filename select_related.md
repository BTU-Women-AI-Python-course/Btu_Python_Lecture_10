# select_related

**Purpose**:  
`select_related` is used for optimizing database access in Django by fetching related objects upfront. It's particularly useful for single-valued relationships such as `ForeignKey` and `OneToOneField`.

**How It Works**:  
When you use `select_related`, Django performs a SQL `JOIN` and retrieves the related objects in the same database query, reducing the number of database queries needed.

**Benefit**:  
By fetching related objects in a single query, `select_related` significantly reduces the database load and improves performance.

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

## Without `select_related`:

```python
# views.py

from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    for student in students:
        print(student.department.name)  # This triggers a separate query per student
    return render(request, 'students/list.html', {'students': students})
```
**Issue**: This approach results in N+1 queries:
  - 1 query to fetch all students.
  - N queries to fetch each student's department.

## With `select_related`:
```python
# views.py

from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.select_related('department').all()
    for student in students:
        print(student.department.name)  # No additional queries
    return render(request, 'students/list.html', {'students': students})
```
**Benefit**: 
  - Only 1 query is executed using a SQL JOIN to fetch students and their departments together.
    
