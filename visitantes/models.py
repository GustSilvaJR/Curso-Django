from django.db import models

# Create your models here.
class Visitante(models.Model):
    nome = models.CharField(
        max_length = 194,
        verbose_name = "Nome do Visitante",
    )

    cpf = models.CharField(
        max_length = 11,
        verbose_name = "CPF",
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name = "Número da Casa sendo visitada",
    )

    placa_veiculo = models.CharField(
        verbose_name = "Placa do Veículo",
        max_length=7,
        blank = True,#Informando que o campo pode ficar em branco
        null = True,#Informando que o campo pode ser nulo
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de chegada",
        auto_now_add=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de saída",
        auto_now=False,
        blank=True,
        null=True, 
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de autorização de entrada",
        auto_now=False,
        blank=True,
        null=True,
    )

    morador_responsavel = models.CharField(
        verbose_name="Nome do morador responsável por autorizar a entrada do visitante",
        max_length=194,
        blank=True,
    )

    registrado_por = models.ForeignKey(
        "projetos.Porteiro",
        verbose_name="Porteiro responsavel pelo registro",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self):
        return self.nome    