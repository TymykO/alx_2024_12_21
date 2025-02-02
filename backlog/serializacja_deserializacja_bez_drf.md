### **Serializacja i deserializacja w Django (bez Django REST Framework)**

Serializacja i deserializacja to kluczowe pojęcia w programowaniu, które odgrywają ważną rolę w przetwarzaniu danych. W kontekście Django, serializacja oznacza przekształcenie obiektów Django (np. modeli) do formatu, który może być łatwo przesyłany lub przechowywany (np. JSON, XML). Deserializacja to proces odwrotny — przekształcenie danych z formatu zewnętrznego z powrotem do obiektów Django.

W tym artykule omówimy, jak serializować i deserializować dane w Django **bez użycia Django REST Framework (DRF)**, korzystając z wbudowanych narzędzi Django.

---

### **1. Serializacja w Django**

Serializacja w Django polega na przekształceniu obiektów (np. instancji modeli) do formatu, który może być łatwo przesyłany lub przechowywany. Django oferuje wbudowane narzędzia do serializacji danych do formatów takich jak JSON, XML czy YAML.

#### **a) Serializacja do JSON**
Django udostępnia moduł `django.core.serializers`, który umożliwia łatwą serializację obiektów do JSON.

```python
from django.core import serializers
from myapp.models import Product

# Pobierz wszystkie produkty
products = Product.objects.all()

# Serializuj do JSON
data = serializers.serialize('json', products)
print(data)
```

**Wynik:**
```json
[
    {
        "model": "myapp.product",
        "pk": 1,
        "fields": {
            "name": "Laptop",
            "price": "2500.00",
            "category": 1
        }
    },
    {
        "model": "myapp.product",
        "pk": 2,
        "fields": {
            "name": "Smartphone",
            "price": "1500.00",
            "category": 1
        }
    }
]
```

#### **b) Serializacja do XML**
Można również serializować dane do formatu XML.

```python
data = serializers.serialize('xml', products)
print(data)
```

**Wynik:**
```xml
<django-objects version="1.0">
    <object model="myapp.product" pk="1">
        <field name="name" type="CharField">Laptop</field>
        <field name="price" type="DecimalField">2500.00</field>
        <field name="category" type="ForeignKey">1</field>
    </object>
    <object model="myapp.product" pk="2">
        <field name="name" type="CharField">Smartphone</field>
        <field name="price" type="DecimalField">1500.00</field>
        <field name="category" type="ForeignKey">1</field>
    </object>
</django-objects>
```

#### **c) Serializacja do innych formatów**
Django obsługuje również serializację do formatów takich jak YAML czy Python (słowniki).

```python
# Serializacja do YAML
data = serializers.serialize('yaml', products)
print(data)

# Serializacja do słowników Pythona
data = serializers.serialize('python', products)
print(data)
```

---

### **2. Deserializacja w Django**

Deserializacja to proces przekształcenia danych z formatu zewnętrznego (np. JSON, XML) z powrotem do obiektów Django.

#### **a) Deserializacja z JSON**
Aby deserializować dane z JSON, można użyć tego samego modułu `django.core.serializers`.

```python
from django.core import serializers

# Dane JSON do deserializacji
json_data = '''
[
    {
        "model": "myapp.product",
        "pk": 3,
        "fields": {
            "name": "Tablet",
            "price": "800.00",
            "category": 1
        }
    }
]
'''

# Deserializuj dane
objects = serializers.deserialize('json', json_data)

# Zapisz obiekty w bazie danych
for obj in objects:
    obj.save()
```

#### **b) Deserializacja z XML**
Podobnie można deserializować dane z XML.

```python
xml_data = '''
<django-objects version="1.0">
    <object model="myapp.product" pk="4">
        <field name="name" type="CharField">Smartwatch</field>
        <field name="price" type="DecimalField">500.00</field>
        <field name="category" type="ForeignKey">1</field>
    </object>
</django-objects>
'''

# Deserializuj dane
objects = serializers.deserialize('xml', xml_data)

# Zapisz obiekty w bazie danych
for obj in objects:
    obj.save()
```

---

### **3. Ręczna serializacja i deserializacja**

Czasami wbudowane narzędzia Django nie wystarczą, np. gdy chcesz kontrolować, które pola są serializowane lub deserializowane. W takim przypadku możesz ręcznie serializować i deserializować dane.

#### **a) Ręczna serializacja do JSON**
Możesz użyć modułu `json` Pythona, aby ręcznie serializować obiekty.

```python
import json
from myapp.models import Product

# Pobierz wszystkie produkty
products = Product.objects.all()

# Ręczna serializacja
data = [
    {
        "id": product.id,
        "name": product.name,
        "price": str(product.price),  # DecimalField musi być przekształcony do stringa
        "category_id": product.category_id
    }
    for product in products
]

# Konwertuj do JSON
json_data = json.dumps(data)
print(json_data)
```

#### **b) Ręczna deserializacja z JSON**
Możesz również ręcznie deserializować dane.

```python
import json
from myapp.models import Product

# Dane JSON do deserializacji
json_data = '''
[
    {
        "id": 5,
        "name": "E-book Reader",
        "price": "300.00",
        "category_id": 1
    }
]
'''

# Deserializuj dane
data = json.loads(json_data)

# Utwórz obiekty i zapisz je w bazie danych
for item in data:
    product = Product(
        id=item['id'],
        name=item['name'],
        price=item['price'],
        category_id=item['category_id']
    )
    product.save()
```

---

### **4. Kiedy używać serializacji i deserializacji?**

- **Eksport danych**: Gdy chcesz wyeksportować dane z bazy danych do pliku (np. JSON, XML).
- **Import danych**: Gdy chcesz zaimportować dane z pliku do bazy danych.
- **Przesyłanie danych**: Gdy chcesz przesłać dane między aplikacjami (np. przez API).
- **Tworzenie kopii zapasowych**: Gdy chcesz stworzyć kopię zapasową danych.

---

### **5. Podsumowanie**

- **Serializacja** to proces przekształcania obiektów Django do formatu zewnętrznego (np. JSON, XML).
- **Deserializacja** to proces przekształcania danych z formatu zewnętrznego z powrotem do obiektów Django.
- Django oferuje wbudowane narzędzia do serializacji i deserializacji (`django.core.serializers`), ale można również robić to ręcznie.
- Serializacja i deserializacja są przydatne w wielu scenariuszach, takich jak eksport/import danych, przesyłanie danych między aplikacjami czy tworzenie kopii zapasowych.

Dzięki tym technikom możesz łatwo zarządzać danymi w swojej aplikacji Django, nawet bez użycia Django REST Framework.