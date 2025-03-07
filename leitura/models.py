from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_publicacao = models.IntegerField()
    genero = models.CharField(max_length=255)  # Campo obrigatório
    numero_capitulos = models.IntegerField()
    
    # Nota não é obrigatória
    nota = models.IntegerField(choices=[(i, f'{i} estrelas') for i in range(1, 6)], null=True, blank=True) 
    
    # Review não é obrigatório
    review = models.TextField(null=True, blank=True)
    
    # Capa não é obrigatória
    capa = models.ImageField(upload_to='capas_livros/', null=True, blank=True) 
    
    # Data de término não é obrigatória
    data_termino = models.DateField(null=True, blank=True) 
    
    # Campo favorito não é obrigatório
    favorito = models.BooleanField(default=False, null=True, blank=True)  

    ESTANTE_CHOICES = [
        ('na_estante', 'Na Estante'),
        ('lista', 'Lista'),
        ('lidos', 'Lidos'),
        ('lendo', 'Lendo'),
    ]
    
    estante = models.CharField(max_length=20, choices=ESTANTE_CHOICES, default='na_estante')

    def __str__(self):
        return self.titulo

class MetaLeitura(models.Model):
    mes = models.IntegerField(choices=[(i, f'{i}º Mês') for i in range(1, 13)])
    ano = models.IntegerField()
    quantidade_meta = models.IntegerField()
    livros_concluidos = models.IntegerField(default=0)

    def __str__(self):
        return f'Meta de {self.quantidade_meta} livros em {self.mes}/{self.ano}'

    def marcar_concluido(self):
        self.livros_concluidos += 1
        if self.livros_concluidos >= self.quantidade_meta:
            
            pass
        self.save()