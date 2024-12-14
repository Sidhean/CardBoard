class Automaton:
    def __init__(self, job: str | None = None, name: str | None = None):
        pass  # learn constructors again
        self.inv = {}
        self.job = job if job else "Jobless"
        self.name = name if name else "Automaton"
        self.title = f"{self.job} {self.name}"

    def __str__(self):
        return self.title

if __name__ == "__main__":
    demo_automaton = Automaton("Monkey-at-Typewriter","Lyra")
    print("Written by",demo_automaton)