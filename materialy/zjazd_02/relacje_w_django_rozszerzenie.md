### 1. Relacje w Django (rozszerzenie)

#### 1.1 Teoretyczne wprowadzenie

Relacje w Django są podstawą modelowania powiązań między różnymi modelami w bazie danych. Django ORM oferuje trzy główne typy relacji: 
- `ForeignKey` (relacja jeden do wielu),
- `OneToOneField` (relacja jeden do jednego),
- `ManyToManyField` (relacja wiele do wielu).

Każdy z tych typów pozwala na precyzyjne odwzorowanie zależności między tabelami, umożliwiając budowanie elastycznych i efektywnych struktur danych. Zrozumienie relacji jest kluczowe dla projektowania dobrze zoptymalizowanych aplikacji.

---

#### 1.2 Praktyczne przykłady

1. **`ForeignKey` – relacja jeden do wielu**:
   ```python
   class Author(models.Model):
       name = models.CharField(max_length=100)

   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
   ```
   - Każda książka może mieć jednego autora, ale jeden autor może mieć wiele książek.
   - `related_name` umożliwia dostęp do książek autora przez `author.books.all()`.

2. **`OneToOneField` – relacja jeden do jednego**:
   ```python
   class UserProfile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       bio = models.TextField()
   ```
   - Użytkownik ma jedno powiązane konto użytkownika.

3. **`ManyToManyField` – relacja wiele do wielu**:
   ```python
   class Student(models.Model):
       name = models.CharField(max_length=100)

   class Course(models.Model):
       title = models.CharField(max_length=100)
       students = models.ManyToManyField(Student, related_name='courses')
   ```
   - Wielu studentów może zapisać się na wiele kursów i vice versa.

4. **Relacje self-referencing**:
   ```python
   class Employee(models.Model):
       name = models.CharField(max_length=100)
       manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
   ```
   - Każdy pracownik może mieć menedżera będącego innym pracownikiem.

5. **Through models (w `ManyToManyField`)**:
   ```python
   class Membership(models.Model):
       student = models.ForeignKey(Student, on_delete=models.CASCADE)
       course = models.ForeignKey(Course, on_delete=models.CASCADE)
       date_joined = models.DateField()

   class Course(models.Model):
       title = models.CharField(max_length=100)
       students = models.ManyToManyField(Student, through=Membership)
   ```
   - Pozwala na dodanie dodatkowych informacji do relacji wiele-do-wielu.

---

#### 1.3 Ćwiczenia dla uczestników

1. Stwórz modele reprezentujące autorów, książki i wydawnictwa, z odpowiednimi relacjami (`ForeignKey`).
2. Zaprojektuj model UserProfile powiązany z modelem User relacją `OneToOneField`.
3. Utwórz system rejestracji studentów na kursy z wykorzystaniem `ManyToManyField` i modelu pośredniego z informacją o dacie zapisania.
4. Dodaj relację self-referencing do modelu reprezentującego organizację hierarchiczną pracowników.

---

#### 1.4 Najlepsze praktyki i common pitfalls

- **Używaj `related_name` dla lepszej czytelności kodu:** Domyślne nazwy powiązań mogą być trudne do zrozumienia.
- **Starannie wybieraj `on_delete`:** 
  - `CASCADE` – używaj tylko, gdy chcesz automatycznie usuwać powiązane obiekty.
  - `SET_NULL` – wymaga `null=True` w polu i pozwala zachować rekordy.
  - `PROTECT` – zapobiega usunięciu obiektu powiązanego, co może być przydatne w ważnych relacjach.
- **Optymalizuj zapytania:** Używaj `select_related` i `prefetch_related`, aby zminimalizować liczbę zapytań do bazy danych.
- **Unikaj cyklicznych relacji:** Może to prowadzić do problemów z rekurencją podczas przetwarzania danych.
- **Przetestuj relacje:** Użyj testów jednostkowych, aby upewnić się, że powiązania działają zgodnie z oczekiwaniami.

