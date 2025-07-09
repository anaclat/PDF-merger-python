# 📄 PDF Merger em Python

Este projeto em Python tem como objetivo **mesclar vários arquivos PDF em um único documento final** chamado `PDF Final.pdf`. Ele utiliza a biblioteca `PyPDF2` para manipulação de arquivos PDF e a biblioteca `os` para leitura da pasta onde estão os documentos.

## 🔧 Pré-requisitos

Antes de executar o projeto, você precisa ter o Python instalado e a biblioteca `PyPDF2`. Para instalar, rode:

```bash
pip install PyPDF2
````

## 📁 Estrutura do Projeto

Certifique-se de ter uma pasta chamada `arquivos` no mesmo diretório do script Python. Dentro dela, coloque todos os arquivos `.pdf` que deseja mesclar.

```
seu_projeto/
├── arquivos/
│   ├── documento1.pdf
│   ├── documento2.pdf
│   └── ...
├── merge_pdf.py
```

## ▶️ Como Executar

1. Coloque todos os arquivos PDF que deseja juntar dentro da pasta `arquivos`.
2. Execute o script:

```bash
python merge_pdf.py
```

3. O programa irá:

   * Listar os arquivos PDF encontrados
   * Ordená-los em ordem alfabética
   * Juntá-los em um único arquivo chamado **`PDF Final.pdf`**, que será criado no mesmo diretório do script.

## 🧠 Como funciona o código

```python
import PyPDF2
import os

merger = PyPDF2.PdfMerger()  # Cria o objeto que fará a mesclagem

lista_arquivos = os.listdir('arquivos')  # Lista os arquivos dentro da pasta
lista_arquivos.sort()  # Ordena os arquivos por nome
print(lista_arquivos)  # Exibe a lista para conferência

for arquivo in lista_arquivos:
    if '.pdf' in arquivo:  # Verifica se o arquivo é um PDF
        merger.append(f'arquivos/{arquivo}')  # Adiciona o PDF ao merger
        merger.write('PDF Final.pdf')  # Gera o arquivo final (dentro do loop — pode ser melhorado)
```python
for arquivo in lista_arquivos:
    if '.pdf' in arquivo:
        merger.append(f'arquivos/{arquivo}')

merger.write('PDF Final.pdf')
```

---

## ✅ Resultado Esperado

Ao final da execução, será criado o arquivo:

```
PDF Final.pdf
```

Contendo todos os arquivos PDF mesclados na ordem alfabética original.
