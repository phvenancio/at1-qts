import math
"""Regras de negócio de um sistema simples de estacionamento."""


class EstacionamentoError(ValueError):
    """Erro de validação das entradas do domínio."""


def calcular_valor_estacionamento(
    horas: float,
    tipo_veiculo: str,
    possui_vaga_especial: bool = False,
) -> float:
    """Calcula o valor da permanência de um veículo no estacionamento.

    Regras:
    - horas deve ser maior que zero;
    - tipo_veiculo deve ser carro, moto ou utilitario;
    - vaga especial só pode ser usada por carro;
    - até 2 horas: tarifa base;
    - acima de 2 até 5 horas: tarifa base + hora excedente;
    - acima de 5 horas: aplica tarifa de diária.
    """

    if not isinstance(horas, (int, float)) or isinstance(horas, bool):
        raise EstacionamentoError("Quantidade de horas inválida.")
    
    if not math.isfinite(horas) or horas <= 0:
        raise EstacionamentoError("Quantidade de horas inválida.")

    if not isinstance(horas, (int, float)) or isinstance(horas, bool):
        raise EstacionamentoError("horas deve ser numérico.")

    if horas <= 0:
        raise EstacionamentoError("horas deve ser maior que zero.")

    if tipo_veiculo not in {"carro", "moto", "utilitario"}:
        raise EstacionamentoError("tipo de veículo inválido.")

    if not isinstance(possui_vaga_especial, bool):
        raise EstacionamentoError(
            "possui_vaga_especial deve ser booleano."
        )

    if possui_vaga_especial and tipo_veiculo != "carro":
        raise EstacionamentoError(
            "Somente carros podem utilizar vaga especial."
        )

    tarifas = {
        "carro": {
            "base": 10.0,
            "excedente": 4.0,
            "diaria": 35.0,
        },
        "moto": {
            "base": 6.0,
            "excedente": 2.0,
            "diaria": 20.0,
        },
        "utilitario": {
            "base": 14.0,
            "excedente": 5.0,
            "diaria": 45.0,
        },
    }

    tarifa = tarifas[tipo_veiculo]

    if horas <= 2:
        valor = tarifa["base"]

    elif horas <= 5:
        horas_excedentes = horas - 2
        valor = (
            tarifa["base"]
            + horas_excedentes * tarifa["excedente"]
        )

    else:
        valor = tarifa["diaria"]

    if possui_vaga_especial:
        valor *= 0.9

    return round(valor, 2)