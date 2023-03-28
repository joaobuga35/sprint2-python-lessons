class Movie:
    def __init__(self, name, duration) -> None:
        self.name = name
        self.duration = duration
        pass

    def __str__(self):
        return f"Filme: {self.name}"
    
    def __len__(self):
        return self.duration
    
    def numero_de_exibicoes(self, exibicoes):
        self.exibicoes = exibicoes

        return self.exibicoes


John = Movie("John Wick", 115)

print(John.name)
print(John.duration)


