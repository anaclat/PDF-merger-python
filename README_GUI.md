# PDF Merger (Programa com Interface)

Este projeto agora inclui uma interface para mesclar PDFs.

## Requisitos
- Windows 10/11
- Python 3.9+ (recomendado)

## Instalação (dev)
```bash
pip install -r requirements.txt
pip install PyQt5 pyinstaller
```

> Observação: o `requirements.txt` original não tinha `PyQt5`, mas este README inclui a instalação.

## Rodar (Python)
```bash
python app_gui.py
```

## Usar o .exe (Windows)
Se você já tem um executável gerado em `dist/` (por exemplo `dist/PDF Merger.exe`), basta:
1. Abrir a pasta `dist/`
2. Dar dois cliques no `.exe`
3. Na interface:
   - Adicione os PDFs
   - (Opcional) defina o arquivo de saída
   - Clique em **Mesclar**

## Observação sobre a parte web
A parte web (Flask + `public/index.html`) ainda está em desenvolvimento para deploy/hospedagem. Se você quiser publicar para a internet, pode ser necessário ajustar rotas/integração. Sugestões e correções são bem-vindas.


