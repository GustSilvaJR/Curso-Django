from visitantes.models import Visitante
from django import forms

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = (
            "nome", "cpf", "data_nascimento", "numero_casa", "placa_veiculo"
        )

        error_messages = {
            "nome":{
                "required":"O nome completo do visitante é obrigatório para o registro"
            },
            "cpf":{
                "required":"O CPF do visitante é obrigatório para o registro"
            },
            "data_nascimento":{
                "required":"A data de nascimento do visitante é obrigatório para o registro",

                "invalid":"Informe uma data de nascimento válida (DD/MM/AAAA)"
            },
            "numero_casa":{
                "required":"O número da casa a ser visitada é obrigatório para o registro"
            },
        }