from pathlib import Path
import json


caminho_json = Path(__file__).parent.parent / "saved_data.json"

def carregar_dados():
    if not caminho_json.exists():
        return {}
    
    with open(caminho_json, "r") as arquivo:
        return json.load(arquivo)


def salvar_dados(data: dict):
    if not isinstance(data, dict):
        raise TypeError("Formato invalido, informe um dict.") 

    with open(caminho_json, "w") as arquivo:
        json.dump(data, arquivo, indent=4)
        
    return True
