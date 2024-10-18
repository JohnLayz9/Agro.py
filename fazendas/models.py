from django.db import models # type: ignore

def populate():
    fazendas = [
        {"nome": "Fazenda São José", "localizacao": "São Paulo", "tamanho": 150.0},
        {"nome": "Fazenda Boa Vista", "localizacao": "Minas Gerais", "tamanho": 300.0},
        {"nome": "Fazenda Água Limpa", "localizacao": "Goiás", "tamanho": 220.5},
    ]

    for fazenda_data in fazendas:
        fazenda = Fazenda(**fazenda_data)
        fazenda.save()

    if __name__ == "__main__":
        populate()

class Fazenda(models.Model):
    nome = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tamanho = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.nome

class Talhao(models.Model):
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    estado_solo = models.TextField()

    def __str__(self):
        return f'{self.nome} - {self.fazenda.nome}'
    
    
