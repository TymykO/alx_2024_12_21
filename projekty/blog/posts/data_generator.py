"""
Stwórz funkcję, która wygeneruje n losowych postów. 

- losowy tytuł
- losowa treść o różnej długości (100 - 2000 znaków)
- losowy autor (z istniejących)
- losowy status (published, draft)

p = Post(title=title, content=content, author=author, status=status)
p.save()

funkcję odpalimy w shellu:
python manage.py shell

from posts.data_generator import generate_posts
generate_posts(100)



"""
from faker import Faker

from posts.models import Post
from django.contrib.auth.models import User



def generate_posts(n, language="pl_PL"):
    faker = Faker(language)
    authors = User.objects.all()
    statuses = ["published", "draft"]
    for _ in range(n):
        title = faker.sentence()

        content_length = faker.random_int(100, 2000)
        content = faker.text(content_length)

        author = faker.random_element(authors)
        status = faker.random_element(statuses)

        post = Post(title=title, content=content, author=author, status=status)
        post.save()

    print(f"Generated {n} posts")

