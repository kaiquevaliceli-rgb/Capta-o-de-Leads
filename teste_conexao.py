import gspread
from google.oauth2.service_account import Credentials

ESCOPO = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]

ID_PLANILHA = "19RY8uHw-mdBXsLGuuk3eRu6veRiJ1o5nS6ltEkYXhR4"

# Traduz o texto exato do formulario para o formato usado internamente no projeto
MAPA_INTERESSE_FORMULARIO = {
    "Implante": "implante",
    "Avaliação": "avaliacao",
    "Dúvida geral": "duvida geral",
    "Emergência": "emergencia",
}


def qualificar_lead(interesse):
    """Define a prioridade do lead com base no interesse informado."""
    if interesse == "emergencia":
        return "urgente"
    elif interesse in ("implante", "avaliacao"):
        return "quente"
    else:
        return "morno"


def conectar_planilha():
    """Autentica com o Google e retorna a primeira aba da planilha."""
    credenciais = Credentials.from_service_account_file("credenciais.json", scopes=ESCOPO)
    cliente = gspread.authorize(credenciais)
    planilha = cliente.open_by_key(ID_PLANILHA)
    return planilha.sheet1


def importar_leads_do_formulario():
    """Le todas as respostas do formulario e converte cada linha em um lead qualificado."""
    aba = conectar_planilha()
    linhas = aba.get_all_records()

    leads_importados = []
    for linha in linhas:
        interesse_bruto = linha.get("Interesse:", "")
        interesse = MAPA_INTERESSE_FORMULARIO.get(interesse_bruto, "duvida geral")

        lead = {
            "nome": linha.get("Nome:", ""),
            "telefone": linha.get("Telefone (whatsapp):", ""),
            "interesse": interesse,
            "origem": linha.get("Como chegou ate a clinica?", ""),
            "prioridade": qualificar_lead(interesse),
        }
        leads_importados.append(lead)

    return leads_importados


if __name__ == "__main__":
    leads = importar_leads_do_formulario()
    print(f"{len(leads)} lead(s) importado(s) do formulario:\n")
    for lead in leads:
        print(
            f"[{lead['prioridade'].upper()}] {lead['nome']} | "
            f"Tel: {lead['telefone']} | Interesse: {lead['interesse']}"
        )
