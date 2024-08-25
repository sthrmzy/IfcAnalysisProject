# Pasta `data` - Arquivos IFC e OBJ

Esta pasta contém arquivos relacionados a projetos de construção e modelagem 3D, incluindo arquivos no formato IFC e OBJ. Estes arquivos são usados para análise, visualização e manipulação de dados BIM (Building Information Modeling) e geometria 3D.

## Estrutura da Pasta

- **Arquivos IFC**
  - **Descrição**: Arquivos no formato IFC (Industry Foundation Classes) que contêm informações detalhadas sobre modelos de construção, incluindo dados sobre elementos arquitetônicos, estruturais e de engenharia.
  - **Extensão**: `.ifc`
  - **Exemplo**: `casa.ifc`
    - **Descrição**: Um modelo de construção que inclui elementos como paredes, portas, janelas, etc., representados em um formato padrão para interoperabilidade.

- **Arquivos OBJ**
  - **Descrição**: Arquivos no formato OBJ que contêm informações sobre a geometria 3D dos modelos. Este formato é amplamente utilizado para a troca de dados de geometria entre diferentes softwares de modelagem 3D.
  - **Extensão**: `.obj`
  - **Exemplo**: `modelo.obj`
    - **Descrição**: Um modelo 3D exportado em formato OBJ, representando a geometria dos elementos do projeto, sem informações adicionais de BIM.

## Como Usar

1. **Análise de Arquivos IFC**:
   - Utilize scripts Python com a biblioteca `IfcOpenShell` para carregar e analisar os arquivos IFC. Esses arquivos fornecem dados detalhados sobre o modelo de construção, incluindo propriedades e relações entre elementos.

2. **Visualização de Arquivos OBJ**:
   - Utilize ferramentas de visualização 3D, como `PyVista` ou software de modelagem 3D, para carregar e visualizar os arquivos OBJ. Esses arquivos são úteis para ver a geometria do modelo em 3D.

3. **Conversão entre Formatos**:
   - Se necessário, você pode converter arquivos IFC para OBJ ou outros formatos usando ferramentas de conversão para melhor compatibilidade com diferentes softwares e pipelines de trabalho.

## Exemplos de Uso

### Análise com Python

```python
import ifcopenshell

# Carregar um arquivo IFC
file_path = 'data/casa.ifc'
arquivo_ifc = ifcopenshell.open(file_path)

# Exemplo de análise
elementos = arquivo_ifc.by_type("IfcE
