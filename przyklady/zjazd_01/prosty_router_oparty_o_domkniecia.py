
def homepage():
    return "Strona główna"

def about():
    return "O nas"

def contact():
    return "Kontakt"


def create_router():

    routes = {}

    def route_handler(action, path, func=None):
        if action == "add":
            routes[path] = func
            print(f"Dodano nową ścieżkę: {path} -> {func.__name__}")
        elif action == "get":
            if path in routes:
                return routes[path]()
            else:
                return "404 - Not Found"
        else:
            raise ValueError(f"Invalid action: {action}")

    return route_handler


router = create_router()
router2 = create_router()


router("add", "/home", homepage)
router("add", "/about", about)
router("add", "/contact", contact)


print(router("get", "/home" ))
print(router("get", "/about" ))
print(router("get", "/contact" ))

print(router("get", "/xxx"))


print(router2("get", "/home"))
print(router("get", "/contact" ))
