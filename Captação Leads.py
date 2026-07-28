import json
import os

ARQUIVO_LEADS = "leads.json"


def carregar_leads():
    """Le o arquivo JSON e retorna a lista de leads. Se nao existir, retorna lista vazia."""
    if os.path.exists(ARQUIVO_LEADS):
        with open(ARQUIVO_LEADS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_leads(leads):
    """Salva a lista de leads no arquivo JSON."""
    with open(ARQUIVO_LEADS, "w", encoding="utf-8") as arquivo:
        json.dump(leads, arquivo, indent=4, ensure_ascii=False)


def gerar_novo_id(leads):
    """Gera o proximo ID disponivel, baseado no maior ID existente."""
    if not leads:
        return 1
    return max(lead["id"] for lead in leads) + 1


def qualificar_lead(interesse):
    """Define a prioridade do lead com base no interesse informado."""
    if interesse == "emergencia":
        return "urgente"
    elif interesse in ("implante", "avaliacao"):
        return "quente"
    else:
        return "morno"


def adicionar_lead(leads):
    """Pergunta os dados do lead ao usuario e adiciona na lista."""
    print("\n--- Novo Lead ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    print("Interesse do lead:")
    print("1 - Implante")
    print("2 - Avaliacao")
    print("3 - Duvida geral")
    print("4 - Emergencia")
    opcao_interesse = input("Escolha uma opcao (1-4): ")

    mapa_interesse = {
        "1": "implante",
        "2": "avaliacao",
        "3": "duvida geral",
        "4": "emergencia",
    }
    interesse = mapa_interesse.get(opcao_interesse, "duvida geral")

    print("Como o lead chegou ate a clinica?")
    print("1 - Instagram")
    print("2 - Google")
    print("3 - Indicacao")
    print("4 - Outro")
    opcao_origem = input("Escolha uma opcao (1-4): ")

    mapa_origem = {
        "1": "instagram",
        "2": "google",
        "3": "indicacao",
        "4": "outro",
    }
    origem = mapa_origem.get(opcao_origem, "outro")

    prioridade = qualificar_lead(interesse)

    novo_lead = {
        "id": gerar_novo_id(leads),
        "nome": nome,
        "telefone": telefone,
        "interesse": interesse,
        "origem": origem,
        "prioridade": prioridade,
    }

    leads.append(novo_lead)
    salvar_leads(leads)
    print(f"\nLead '{nome}' adicionado com sucesso! (ID {novo_lead['id']}, prioridade: {prioridade})")


def listar_leads(leads):
    """Mostra todos os leads cadastrados."""
    if not leads:
        print("\nNenhum lead cadastrado ainda.")
        return

    print("\n--- Lista de Leads ---")
    for lead in leads:
        prioridade = lead.get("prioridade", "nao definida")
        print(
            f"ID {lead['id']} | {lead['nome']} | Tel: {lead['telefone']} | "
            f"Interesse: {lead['interesse']} | Origem: {lead['origem']} | "
            f"Prioridade: {prioridade}"
        )


def relatorio_por_prioridade(leads):
    """Mostra os leads ordenados por prioridade: urgente -> quente -> morno."""
    if not leads:
        print("\nNenhum lead cadastrado ainda.")
        return

    peso_prioridade = {
        "urgente": 0,
        "quente": 1,
        "morno": 2,
    }

    leads_ordenados = sorted(
        leads,
        key=lambda lead: peso_prioridade.get(lead.get("prioridade", "morno"), 3)
    )

    print("\n--- Relatorio por Prioridade ---")
    for lead in leads_ordenados:
        prioridade = lead.get("prioridade", "nao definida")
        print(
            f"[{prioridade.upper()}] ID {lead['id']} | {lead['nome']} | "
            f"Tel: {lead['telefone']} | Interesse: {lead['interesse']}"
        )


def menu():
    leads = carregar_leads()

    while True:
        print("\n=== Sistema de Captacao de Leads ===")
        print("1 - Adicionar lead")
        print("2 - Listar leads")
        print("3 - Relatorio por prioridade")
        print("4 - Sair")
        escolha = input("Escolha uma opcao: ")

        if escolha == "1":
            adicionar_lead(leads)
        elif escolha == "2":
            listar_leads(leads)
        elif escolha == "3":
            relatorio_por_prioridade(leads)
        elif escolha == "4":
            print("Encerrando o sistema. Ate mais!")
            break
        else:
            print("Opcao invalida, tente novamente.")


if __name__ == "__main__":
    menu()


