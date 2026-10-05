# AI_USAGE — Governança e Transparência de IA

## 1. Ferramenta utilizada

Foi utilizado o ChatGPT como ferramenta de apoio ao desenvolvimento
desta atividade.

---

## 2. Objetivo do uso da IA

A IA foi utilizada como apoio para:

- escolha do domínio da aplicação;
- organização da estrutura do projeto;
- elaboração inicial do PRD;
- implementação inicial das regras de negócio;
- elaboração de cenários de teste;
- identificação de casos de Particionamento de Equivalência;
- identificação de Valores Limite;
- identificação de cenários de Error Guessing;
- organização da suíte de testes com Pytest;
- revisão da estratégia de cobertura de código.

---

## 3. Auditoria humana

O código sugerido pela IA não deve ser considerado automaticamente
correto.

O autor é responsável por:

1. verificar se a implementação corresponde ao PRD;
2. revisar as regras de negócio;
3. revisar os testes;
4. executar a suíte localmente;
5. analisar os resultados do Pytest;
6. verificar a cobertura de linhas;
7. verificar a cobertura de branches;
8. corrigir eventuais problemas identificados durante a execução.

---

## 4. Critério de aceitação

O resultado final somente será considerado válido após execução local
dos comandos:

```bash
uv run pytest -v
```