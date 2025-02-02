### **Zwracanie różnych rodzajów odpowiedzi w Django: HTML, JSON, XML, pliki**

W Django widoki (views) mogą zwracać różne rodzaje odpowiedzi, w zależności od potrzeb aplikacji. Można zwracać strony HTML, dane w formacie JSON lub XML, a nawet pliki do pobrania. W tym materiale omówimy, jak zwracać różne rodzaje odpowiedzi w Django.

---

### **1. Zwracanie odpowiedzi HTML**

Django jest frameworkiem do tworzenia aplikacji webowych, więc domyślnie zwraca odpowiedzi w formacie HTML. Można to zrobić na kilka sposobów.

#### **a) Użycie szablonów (templates)**
Najczęstszym sposobem jest renderowanie szablonów HTML za pomocą funkcji `render`.

```python
from django.shortcuts import render
from myapp.models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/list.html', {'products': products})
```

W szablonie `products/list.html` możesz wyświetlić listę produktów:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista produktów</title>
</head>
<body>
    <h1>Produkty</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - {{ product.price }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### **b) Zwracanie prostego HTML**
Możesz również zwrócić prosty HTML bez użycia szablonów, korzystając z `HttpResponse`.

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Witaj, świecie!</h1>")
```

---

### **2. Zwracanie odpowiedzi JSON**

JSON to popularny format danych używany w API. Django umożliwia łatwe zwracanie odpowiedzi w formacie JSON.

#### **a) Użycie `JsonResponse`**
Klasa `JsonResponse` automatycznie konwertuje słownik Pythona na JSON.

```python
from django.http import JsonResponse
from myapp.models import Product

def product_list_json(request):
    products = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': str(product.price)  # DecimalField musi być przekształcony do stringa
        }
        for product in products
    ]
    return JsonResponse(data, safe=False)  # safe=False pozwala na zwracanie list
```

#### **b) Ręczne tworzenie JSON**
Możesz również ręcznie stworzyć JSON za pomocą modułu `json` i zwrócić go przez `HttpResponse`.

```python
import json
from django.http import HttpResponse
from myapp.models import Product

def product_list_json_manual(request):
    products = Product.objects.all()
    data = [
        {
            'id': product.id,
            'name': product.name,
            'price': str(product.price)
        }
        for product in products
    ]
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
```

---

### **3. Zwracanie odpowiedzi XML**

XML to kolejny format danych, który może być używany w API. Django nie ma wbudowanej obsługi XML, ale można go łatwo wygenerować.

#### **a) Ręczne tworzenie XML**
Możesz ręcznie stworzyć XML i zwrócić go przez `HttpResponse`.

```python
from django.http import HttpResponse
from myapp.models import Product

def product_list_xml(request):
    products = Product.objects.all()
    xml_data = '<products>'
    for product in products:
        xml_data += f'''
            <product>
                <id>{product.id}</id>
                <name>{product.name}</name>
                <price>{product.price}</price>
            </product>
        '''
    xml_data += '</products>'
    return HttpResponse(xml_data, content_type='application/xml')
```

#### **b) Użycie biblioteki zewnętrznej**
Możesz użyć biblioteki `xml.etree.ElementTree` do generowania XML.

```python
import xml.etree.ElementTree as ET
from django.http import HttpResponse
from myapp.models import Product

def product_list_xml_etree(request):
    products = Product.objects.all()
    root = ET.Element('products')
    for product in products:
        product_elem = ET.SubElement(root, 'product')
        ET.SubElement(product_elem, 'id').text = str(product.id)
        ET.SubElement(product_elem, 'name').text = product.name
        ET.SubElement(product_elem, 'price').text = str(product.price)
    xml_data = ET.tostring(root, encoding='utf-8', method='xml')
    return HttpResponse(xml_data, content_type='application/xml')
```

---

### **4. Zwracanie plików**

Django umożliwia zwracanie plików do pobrania, np. PDF, obrazków czy dokumentów tekstowych.

#### **a) Zwracanie pliku z dysku**
Możesz zwrócić plik z dysku za pomocą `FileResponse`.

```python
from django.http import FileResponse

def download_file(request):
    file_path = '/path/to/your/file.pdf'
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='file.pdf')
```

#### **b) Generowanie pliku w locie**
Możesz również generować plik w locie i zwrócić go jako odpowiedź.

```python
from django.http import HttpResponse
import csv

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Price'])
    products = Product.objects.all()
    for product in products:
        writer.writerow([product.id, product.name, product.price])

    return response
```

---

### **5. Podsumowanie**

- **HTML**: Użyj `render` do zwracania szablonów HTML lub `HttpResponse` do zwracania prostego HTML.
- **JSON**: Użyj `JsonResponse` do zwracania danych w formacie JSON.
- **XML**: Ręcznie generuj XML lub użyj biblioteki `xml.etree.ElementTree`.
- **Pliki**: Użyj `FileResponse` do zwracania plików z dysku lub `HttpResponse` do generowania plików w locie.

Dzięki tym technikom możesz zwracać różne rodzaje odpowiedzi w Django, dostosowane do potrzeb Twojej aplikacji.