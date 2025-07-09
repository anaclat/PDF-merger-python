# 📄 PDF Merger em Python

Este projeto em Python tem como objetivo **mesclar vários arquivos PDF em um único documento final** chamado `PDF Final.pdf`. Ele utiliza a biblioteca `PyPDF2` para manipulação de arquivos PDF e a biblioteca `os` para leitura da pasta onde estão os documentos.

## 🔧 Pré-requisitos

Antes de executar o projeto, você precisa ter o Python instalado e a biblioteca `PyPDF2`. Para instalar, rode:

```bash
pip install PyPDF2
```

## 📁 Estrutura do Projeto
Certifique-se de ter uma pasta chamada arquivos no mesmo diretório do script Python. Dentro dela, coloque todos os arquivos .pdf que deseja mesclar.

```seu_projeto/
├── arquivos/
│   ├── documento1.pdf
│   ├── documento2.pdf
│   └── ...
├── main.py
```

## ▶️ Como Executar
- Coloque todos os arquivos PDF que deseja juntar dentro da pasta arquivos.
- Execute o script:
```
python main.py
```

## O programa irá:
- Listar os arquivos PDF encontrados
- Ordená-los em ordem alfabética
- Juntá-los em um único arquivo chamado PDF Final.pdf, que será criado no mesmo diretório do script.
