from libpythonpro.spam.enviador_email import Enviador, EmailInvalido
import pytest

def test_criar_enviador_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['remetente@email.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'destinatario@email.com',
        'assunto',
        'corpo do email'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'sem_arroba']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'destinatario@email.com',
            'assunto',
            'corpo do email'
        )
