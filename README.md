# Análise de Arquivos IFC com Python

Este projeto realiza a análise e visualização de arquivos IFC (Industry Foundation Classes) usando Python e bibliotecas como `ifcopenshell`, `pandas`, `matplotlib`, `seaborn` e `pyvista`. O objetivo é extrair dados dos arquivos IFC, realizar análises e gerar visualizações 3D dos elementos do modelo.

![Visualização do Modelo IFC](reports/figures/ifc_model_visualization.png)

## Funcionalidades

* **Extração de Dados:** Extrai informações detalhadas sobre os elementos (`IfcElement`) presentes no arquivo IFC, como ID, Nome, Tipo, GlobalId, Descrição e Modelo, utilizando `ifcopenshell`.
* **Análise de Dados:** Utiliza `pandas` para organizar os dados extraídos em DataFrames, permitindo análises como contagem de elementos por tipo e identificação de nomes únicos.
* **Visualização de Dados:** Gera gráficos (contagem por tipo, distribuição de nomes, histograma de tipos) usando `matplotlib` e `seaborn` para entender a composição do modelo IFC.
* **Visualização 3D:** Renderiza o modelo 3D a partir de um arquivo OBJ (convertido do IFC) usando `pyvista`.
* **Exportação:** Salva os dados extraídos dos elementos em formato CSV.

## Estrutura do Repositório

* `data/`: Contém os arquivos IFC (`casa.ifc`) e OBJ (`casa.obj`) para análise e visualização.
* `notebooks/`: Contém o notebook Jupyter (`analysis.ipynb`) para análise interativa e exploração dos dados.
* `src/`: Contém os scripts Python:
    * `analyze_ifc.py`: Script principal para extrair dados do IFC e salvar em CSV.
    * `visualization.py`: Script para visualização 3D do arquivo OBJ.
* `results/`: Armazena os arquivos CSV gerados pela análise (ex: `elementos_ifc.csv`).
* `reports/figures/`: Contém imagens e gráficos gerados, incluindo a visualização do modelo.
* `requirements.txt`: Lista as dependências do projeto.

## Instalação

1.  Clone o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd IfcAnalysisProject
    ```
2.  Crie um ambiente virtual (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # ou
    .\venv\Scripts\activate  # Windows
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    *Nota:* Pode ser necessário instalar dependências adicionais como `vtk` dependendo do seu sistema operacional para `pyvista` funcionar corretamente. O notebook `analysis.ipynb` também lista comandos `pip install` específicos que podem ser necessários em ambientes como o Google Colab.

## Como Usar

1.  **Análise de Dados (Script):**
    * Coloque seu arquivo IFC na pasta `data/` (ex: `data/casa.ifc`).
    * Execute o script de análise:
        ```bash
        python src/analyze_ifc.py
        ```
    * Os dados extraídos serão impressos no console e salvos em `results/elementos_ifc.csv`.

2.  **Análise Interativa (Notebook):**
    * Abra e execute o notebook `notebooks/analysis.ipynb` usando Jupyter Lab ou Jupyter Notebook.
    * Siga as células do notebook para carregar o arquivo IFC, extrair dados, realizar análises e gerar gráficos.

3.  **Visualização 3D:**
    * Certifique-se de ter um arquivo OBJ na pasta `data/` (ex: `data/casa.obj`). Você pode precisar converter seu IFC para OBJ usando outras ferramentas.
    * Execute o script de visualização:
        ```bash
        python src/visualization.py
        ```
    * Uma janela interativa do `pyvista` será aberta exibindo o modelo 3D.

## Requisitos

As principais bibliotecas utilizadas são:

* ifcopenshell
* pandas
* matplotlib
* seaborn
* pyvista
* vtk (geralmente uma dependência do pyvista)

Consulte o arquivo `requirements.txt` para a lista completa.
