import ifcopenshell
import pandas as pd
import os

def extrair_dados_ifc(file_path):
    """
    Extrai dados dos elementos de um arquivo IFC e os retorna como um DataFrame do Pandas.
    """
    # Abrir o arquivo IFC
    try:
        arquivo_ifc = ifcopenshell.open(file_path)
        print("Arquivo IFC aberto com sucesso.")
    except Exception as e:
        raise RuntimeError(f"Erro ao abrir o arquivo IFC: {e}")

    # Obter todos os elementos do arquivo
    elementos = arquivo_ifc.by_type("IfcElement")

    # Criar uma lista com os dados dos elementos
    dados_elementos = []
    for elemento in elementos:
        dados = {
            "ID": elemento.id(),
            "Nome": elemento.Name,
            "Tipo": elemento.is_a(),
            "GlobalId": elemento.GlobalId,
            "Descrição": getattr(elemento, "Description", "N/A"),
            "Modelo": getattr(elemento, "ObjectType", "N/A"),
            "Unidade de Medida": getattr(elemento, "PredefinedType", "N/A")
        }
        dados_elementos.append(dados)

    # Converter para um DataFrame do Pandas
    df_elementos = pd.DataFrame(dados_elementos)

    return df_elementos

def salvar_csv(df, output_path):
    """
    Salva o DataFrame como um arquivo CSV.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Dados salvos no arquivo CSV: {output_path}")
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar o arquivo CSV: {e}")

def main():
    # Caminho para o arquivo IFC
    file_path = 'data/casa.ifc'  # Atualize para o caminho do seu arquivo IFC
    output_path = 'results/elementos_ifc.csv'  # Caminho para salvar o arquivo CSV

    # Certifique-se de que o diretório de saída existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Extrair dados do arquivo IFC
    df_elementos = extrair_dados_ifc(file_path)

    # Mostrar todos os dados do DataFrame
    print("Todos os dados do DataFrame:")
    pd.set_option('display.max_rows', None)  # Mostrar todas as linhas
    pd.set_option('display.max_columns', None)  # Mostrar todas as colunas
    pd.set_option('display.width', None)  # Ajustar a largura do display
    print(df_elementos.to_string())

    # Salvar os dados em um arquivo CSV
    salvar_csv(df_elementos, output_path)

if __name__ == "__main__":
    main()
