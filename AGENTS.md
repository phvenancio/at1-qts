# Regras de Contexto do Projeto

## Objetivo

Este projeto implementa a AT1 da disciplina Qualidade e Teste de
Software.

O domínio escolhido é um sistema de cálculo de estacionamento.

---

## Regras de desenvolvimento

1. O `PRD.md` é a fonte de verdade das regras de negócio.

2. Não adicionar uma nova regra de negócio sem atualizar o `PRD.md`.

3. Toda alteração no código do domínio deve possuir testes
   correspondentes.

4. Os testes devem seguir o padrão AAA:
   - Arrange
   - Act
   - Assert

5. Utilizar `pytest.mark.parametrize` sempre que vários cenários
   utilizarem a mesma estrutura de teste.

6. Os testes devem utilizar Particionamento de Equivalência,
   Análise de Valor Limite e Error Guessing.

7. Casos inválidos e inesperados devem ser testados.

8. A cobertura de código não deve ser utilizada como único indicador
   de qualidade dos testes.

9. O código deve permanecer simples, determinístico e sem dependências
   externas desnecessárias.

10. O projeto deve continuar executável utilizando `uv`.

---

## Testes

Executar os testes com:

```bash
uv run pytest -v
```