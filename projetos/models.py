from django.db import models

# Create your models here.
class Porteiro(models.Model):

    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name = "Usuário",
        on_delete=models.PROTECT,
    )

    nome_completo = models.CharField(
        max_length=194,
        verbose_name="Nome Completo",
    )

    cpf = models.CharField(
        max_length=11,
        verbose_name="CPF",
    )

    telefone = models.CharField(
        max_length=11,
        verbose_name="Telefone de Contato",
    )

    data_nascimento = models.DateField(
        verbose_name = "Data de Nascimento",
        auto_now_add = False, #COnfiguração que se habilitada diz para o banco que toda vez que o dado for ser salvo ele deve ir com a data e hora atual do relogio.
        auto_now = False, #Config que se habilitada faz com que toda vez que o registro sofrer uma atualização  a data precise ser alterada
    )

    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = 'porteiro'

    def __str__(self):
        return self.nome_completo