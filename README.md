# AT1 — Engenharia de Testes Unitários

Projeto desenvolvido para a atividade avaliativa da disciplina Qualidade e Teste de Software.

## Domínio

Sistema de cálculo de estacionamento.

O sistema calcula o valor da permanência de veículos considerando:

- quantidade de horas;
- tipo de veículo;
- utilização de vaga especial.

---

## Tecnologias

- Python 3.12+
- uv
- Pytest
- pytest-cov

---

## Estrutura

```text
├── app/
│   ├── __init__.py
│   └── estacionamento.py
├── tests/
│   ├── __init__.py
│   └── test_estacionamento.py
├── PRD.md
├── AGENTS.md
├── AI_USAGE.md
├── README.md
├── pyproject.toml
└── uv.lock
```

---

## Instalação de Dependências

```bash
uv venv
uv sync
```
