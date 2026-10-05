import math
import pytest
from app.estacionamento import (
    EstacionamentoError,
    calcular_valor_estacionamento,
)

pytestmark = pytest.mark.unit

@pytest.mark.parametrize(
    ("horas", "tipo", "especial", "esperado"),
    [
        # Carro
        (0.5, "carro", False, 10.0),
        (2, "carro", False, 10.0),
        (2.01, "carro", False, 10.04),
        (3, "carro", False, 14.0),
        (5, "carro", False, 22.0),
        (5.01, "carro", False, 35.0),
        (6, "carro", False, 35.0),

        # Moto
        (0.5, "moto", False, 6.0),
        (2, "moto", False, 6.0),
        (2.01, "moto", False, 6.02),
        (3, "moto", False, 8.0),
        (5, "moto", False, 12.0),
        (5.01, "moto", False, 20.0),
        (6, "moto", False, 20.0),

        # Utilitário
        (0.5, "utilitario", False, 14.0),
        (2, "utilitario", False, 14.0),
        (2.01, "utilitario", False, 14.05),
        (3, "utilitario", False, 19.0),
        (5, "utilitario", False, 29.0),
        (5.01, "utilitario", False, 45.0),
        (6, "utilitario", False, 45.0),
    ],
)

def test_calculo_por_tipo_e_faixa_de_tempo(
    horas,
    tipo,
    especial,
    esperado,
):
    # Arrange
    # Os dados da regra são fornecidos pela parametrização.

    # Act
    resultado = calcular_valor_estacionamento(
        horas,
        tipo,
        especial,
    )

    # Assert
    assert resultado == esperado

@pytest.mark.parametrize(
    ("horas", "esperado"),
    [
        (0.5, 9.0),
        (2, 9.0),
        (2.01, 9.04),
        (5, 19.8),
        (5.01, 31.5),
        (6, 31.5),
    ],
)
def test_carro_com_vaga_especial_recebe_desconto(
    horas,
    esperado,
):
    # Arrange
    tipo = "carro"
    possui_vaga_especial = True

    # Act
    resultado = calcular_valor_estacionamento(
        horas,
        tipo,
        possui_vaga_especial,
    )

    # Assert
    assert resultado == esperado


@pytest.mark.parametrize(
    "horas",
    [
        0,
        -1,
        -0.01,
    ],
)
def test_rejeita_horas_zero_ou_negativas(horas):
    # Arrange
    tipo = "carro"

    # Act
    with pytest.raises(EstacionamentoError):
        calcular_valor_estacionamento(horas, tipo)

    # Assert
    # A exceção é a própria asserção do teste.


@pytest.mark.parametrize(
    "horas",
    [
        None,
        "2",
        math.nan,
        math.inf,
        True,
    ],
)
def test_rejeita_horas_invalidas_ou_inesperadas(horas):
    # Arrange
    tipo = "carro"

    # Act
    with pytest.raises(EstacionamentoError):
        calcular_valor_estacionamento(horas, tipo)

    # Assert
    # A exceção é a própria asserção do teste.


@pytest.mark.parametrize(
    "tipo",
    [
        "bicicleta",
        "",
        "CARRO",
        "caminhao",
        None,
    ],
)
def test_rejeita_tipo_de_veiculo_invalido(tipo):
    # Arrange
    horas = 2

    # Act
    with pytest.raises(EstacionamentoError):
        calcular_valor_estacionamento(horas, tipo)

    # Assert
    # A exceção é a própria asserção do teste.


@pytest.mark.parametrize(
    "especial",
    [
        None,
        1,
        0,
        "sim",
        "",
    ],
)
def test_rejeita_vaga_especial_com_tipo_invalido(especial):
    # Arrange
    horas = 2
    tipo = "carro"

    # Act
    with pytest.raises(EstacionamentoError):
        calcular_valor_estacionamento(
            horas,
            tipo,
            especial,
        )

    # Assert
    # A exceção é a própria asserção do teste.


@pytest.mark.parametrize(
    "tipo",
    [
        "moto",
        "utilitario",
    ],
)
def test_vaga_especial_e_restrita_a_carros(tipo):
    # Arrange
    horas = 2

    # Act
    with pytest.raises(EstacionamentoError):
        calcular_valor_estacionamento(
            horas,
            tipo,
            True,
        )

    # Assert
    # A exceção é a própria asserção do teste.