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
