from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import PyPDF2
import io
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/merge', methods=['POST'])
def merge_pdfs():
    if 'files' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    files = request.files.getlist('files')
    if not files:
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    merger = PyPDF2.PdfMerger()

    try:
        for file in files:
            if file.filename == '':
                continue
            if file and file.filename.endswith('.pdf'):
                # Ler o arquivo diretamente da memória para ser compatível com Serverless
                pdf_stream = io.BytesIO(file.read())
                merger.append(pdf_stream)
            else:
                return jsonify({'error': f'Arquivo inválido: {file.filename}. Apenas PDFs são permitidos.'}), 400

        # Criar o PDF mesclado na memória
        output_stream = io.BytesIO()
        merger.write(output_stream)
        merger.close()
        output_stream.seek(0)

        return send_file(
            output_stream,
            as_attachment=True,
            download_name="merged_pdf.pdf",
            mimetype='application/pdf'
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Exportar o app para a Vercel
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run()
