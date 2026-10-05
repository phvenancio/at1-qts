# PRD — Sistema de Cálculo de Estacionamento

## 1. Objetivo

Desenvolver uma função determinística capaz de calcular o valor a ser
pago por um veículo de acordo com seu tempo de permanência, tipo de
veículo e utilização de vaga especial.

O sistema será utilizado como domínio para a aplicação de técnicas de
Engenharia de Testes, incluindo Particionamento de Equivalência,
Análise de Valor Limite e Error Guessing.

---

## 2. Escopo

O sistema será responsável exclusivamente pelo cálculo do valor da
permanência.

Não fazem parte do escopo:

- cadastro de clientes;
- cadastro de veículos;
- controle de entrada e saída;
- banco de dados;
- autenticação;
- pagamento;
- emissão de nota fiscal.

---

## 3. Entradas

A função receberá três informações:

### 3.1 Horas

Quantidade de horas que o veículo permaneceu estacionado.

Tipo esperado:

```text
int ou float
```