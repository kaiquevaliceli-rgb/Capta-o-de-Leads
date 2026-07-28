# Sistema de Captação e Qualificação de Leads

Sistema em Python para capturar leads de uma clínica odontológica, qualificá-los automaticamente por prioridade de atendimento e notificar sobre os leads mais importantes — com integração ao Google Forms/Sheets.

Projeto de portfólio desenvolvido aplicando conhecimento real de rotina clínica (implantodontia) à lógica de programação.

## Funcionalidades

**Sistema principal (terminal):**
- **Cadastro de leads**: nome, telefone, interesse e origem (Instagram, Google, indicação, etc.)
- **Qualificação automática**: cada lead recebe uma prioridade com base no interesse
- **Listagem geral**: todos os leads cadastrados
- **Relatório por prioridade**: leads ordenados do mais urgente ao menos urgente
- **Persistência em JSON**: os dados não se perdem ao fechar o programa

**Integração externa (Google Forms/Sheets + e-mail):**
- Captação de leads via formulário público (Google Forms)
- As respostas caem automaticamente em uma planilha (Google Sheets)
- Um script Python lê a planilha, aplica a mesma lógica de qualificação e envia um **e-mail de alerta automático** sempre que um lead de prioridade alta (urgente ou quente) é identificado

## Regras de qualificação

| Interesse informado         | Prioridade |
|------------------------------|------------|
| Emergência                   | Urgente    |
| Implante ou Avaliação        | Quente     |
| Dúvida geral                 | Morno      |

Essas regras foram definidas com base em experiência real de triagem em clínica odontológica: emergências precisam de contato imediato, quem já demonstra intenção de tratamento (implante/avaliação) tem alta conversão, e dúvidas gerais podem ser respondidas com menor urgência. Leads urgentes e quentes disparam notificação automática por e-mail.

## Como executar o sistema principal

```bash
python "Captação Leads.py"
```

O menu do sistema apresenta as opções:

1. Adicionar lead
2. Listar leads
3. Relatório por prioridade
4. Sair

Os dados ficam salvos automaticamente em `leads.json`, na mesma pasta do projeto.

## Como funciona a integração externa

O fluxo completo é: **Google Forms → Google Sheets → Python lê e qualifica → e-mail de alerta**.

Por segurança, os arquivos com credenciais **não estão neste repositório** (estão no `.gitignore`). Para reproduzir essa parte do projeto, é necessário:

1. Criar um formulário no Google Forms com os campos: nome, telefone, interesse (implante/avaliação/dúvida geral/emergência) e origem, com as respostas vinculadas a uma planilha Google Sheets.
2. Criar um projeto no Google Cloud, ativar a Google Sheets API e a Google Drive API, e gerar uma conta de serviço com um arquivo de credenciais `credenciais.json` (não incluído no repositório).
3. Compartilhar a planilha com o e-mail da conta de serviço.
4. Configurar um arquivo `notificar_leads.py` (não incluído) com e-mail remetente, senha de app do Gmail e e-mail destinatário, para o envio dos alertas.

O script `teste_conexao.py`, incluído neste repositório, mostra a lógica de leitura e qualificação dos leads vindos da planilha (sem as credenciais reais).

## Tecnologias

- Python 3
- Módulo `json` (persistência de dados)
- Módulo `os` (verificação de arquivos)
- `gspread` e `google-auth` (integração com Google Sheets)
- `smtplib` (envio de e-mail)

## Possíveis evoluções futuras

- Interface gráfica ou web
- Integração com WhatsApp Business API
- Execução automática e periódica (agendamento do script)

## Autor

Projeto desenvolvido como parte de transição de carreira para a área de tecnologia, unindo experiência prévia em odontologia/implantodontia com programação em Python.
