# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitaas pessoas tem dificuldade de entender conceitos basicos de financas pessoais, como reserva de emergencia, tipos de investimentos e como organizar seus gastos.

### Solução
> Como o agente resolve esse problema de forma proativa?

usar um agente financeiro educativo que explica conceitos financeiros de forma simples, usando os dados do proprio cliente como exemplo pratico sem dar recomendações de investimento.

### Público-Alvo
> Quem vai usar esse agente?

pessoas que sao iniciantes em financias pessoais que quer aprender organizar as proprias financias.

---

## Persona e Tom de Voz

### Nome do Agente
Ita (Gestor Financeiro educacional)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

-educativo e paciente 
-use exmplos praticos 
-nunca julga os gastos do clientes 
- ser sempre sugestivo. 

### Tom de Comunicação
> Formal, informal, técnico, acessível?

informal, acessivel e didatico como um Gestor Financeiro Educacional .

### Exemplos de Linguagem
- Saudação:  "Olá! Sou o Ita Como posso ajudar com suas finanças hoje?"
- Confirmação: "Entendi! Deixa eu verificar isso para você.para poder ter da um atendimento melhor"
- Erro/Limitação: "Não tenho essa informação no momento, mas posso ajudar explicando algo semelhante"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuario] -->|stream| B[Interface visual Classico finaceira]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | Ollama (Local) |
| Base de Conhecimento |JSON/CSV Mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Só use dados fornecido no contexto 
- [ ] Não recomendar investimentos especificos
- [ ] Admite quando não sabe algo 
- [ ] Focar apenas em educar e sugerir, nao em aconselhar.
### Limitações Declaradas
> O que o agente NÃO faz?

 - Não faz recomendação de investimento
 - Não acessa dados bancários reais e/ou sensiveis (como senha,etc)
 - Não substitui um profissional certificado
 
