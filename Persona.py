
class Persona:

    def __init__(self, name, old) -> None:
        self._name = name
        self._old = old

    def get_information(self):
        print(f"#"*60 + "\n\t\t\t Get Information Person \n" + "#"*60)
        print(f"\n Nombre :: {self._name}\n Edad :: {self._old}")