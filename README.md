# Sistema de Captação e Qualificação de Leads

Sistema em Python, via terminal, para capturar leads de uma clínica odontológica e qualificá-los automaticamente por prioridade de atendimento, com base no interesse informado.

Projeto de portfólio desenvolvido aplicando conhecimento real de rotina clínica (implantodontia) à lógica de programação.

## Funcionalidades

- **Cadastro de leads**: nome, telefone, interesse e origem (Instagram, Google, indicação, etc.)
- **Qualificação automática**: cada lead recebe uma prioridade com base no interesse
- **Listagem geral**: todos os leads cadastrados
- **Relatório por prioridade**: leads ordenados do mais urgente ao menos urgente
- **Persistência em JSON**: os dados não se perdem ao fechar o programa

## Regras de qualificação

| Interesse informado         | Prioridade |
|------------------------------|------------|
| Emergência                   | Urgente    |
| Implante ou Avaliação        | Quente     |
| Dúvida geral                 | Morno      |

Essas regras foram definidas com base em experiência real de triagem em clínica odontológica: emergências precisam de contato imediato, quem já demonstra intenção de tratamento (implante/avaliação) tem alta conversão, e dúvidas gerais podem ser respondidas com menor urgência.

## Como executar

```bash
python captacao_leads.py
```

O menu do sistema apresenta as opções:

1. Adicionar lead
2. Listar leads
3. Relatório por prioridade
4. Sair

Os dados ficam salvos automaticamente em `leads.json`, na mesma pasta do projeto.

## Tecnologias

- Python 3
- Módulo `json` (persistência de dados)
- Módulo `os` (verificação de arquivos)

## Possíveis evoluções futuras

- Integração com formulário web (Google Forms/Sheets)
- Envio automático de notificação para novos leads urgentes
- Interface gráfica ou web

## Autor

Projeto desenvolvido como parte de transição de carreira para a área de tecnologia, unindo experiência prévia em odontologia/implantodontia com programação em Python.
