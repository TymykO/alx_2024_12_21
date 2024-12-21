
# stwórz funkcje greateing_factory, która tworzy funkcje zwracające napis zawierający powitanie w danym jezyku

def greeting_factory(language):

    greetings = {
        "en": "Hello",
        "pl": "Cześć",
        "de": "Hallo",
        "fr": "Bonjour"
    }

    def greeting(name):
        return f"{greetings[language]}, {name}!"

    return greeting

if __name__ == "__main__":

    assert greeting_factory("en")("Alice") == "Hello, Alice!"
    assert greeting_factory("pl")("Alice") == "Cześć, Alice!"
    assert greeting_factory("de")("Alice") == "Hallo, Alice!"
    assert greeting_factory("fr")("Alice") == "Bonjour, Alice!"


