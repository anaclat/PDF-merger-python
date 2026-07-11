import os
import sys
import tempfile
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QAbstractItemView,
    QMessageBox,
    QLineEdit,
)

import PyPDF2


class PdfMergerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Merger")
        self.setMinimumWidth(760)

        self.files: List[str] = []

        # Widgets
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.btn_add = QPushButton("Adicionar PDFs")
        self.btn_remove = QPushButton("Remover selecionado")
        self.btn_clear = QPushButton("Limpar")
        self.btn_merge = QPushButton("Mesclar")
        self.btn_merge.setEnabled(False)

        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Arquivo de saída (opcional) — clique em ‘Salvar como…’) ")
        self.output_path.setReadOnly(True)

        self.btn_choose_output = QPushButton("Salvar como…")

        # Layout
        top = QVBoxLayout()
        top.addWidget(QLabel("Selecione e mescle seus PDFs"))
        top.addWidget(self.status_label)

        top.addWidget(self.list_widget)

        row_buttons = QHBoxLayout()
        row_buttons.addWidget(self.btn_add)
        row_buttons.addWidget(self.btn_remove)
        row_buttons.addWidget(self.btn_clear)
        top.addLayout(row_buttons)

        row_output = QHBoxLayout()
        row_output.addWidget(self.output_path)
        row_output.addWidget(self.btn_choose_output)
        top.addLayout(row_output)

        top.addWidget(self.btn_merge)

        self.setLayout(top)

        # Signals
        self.btn_add.clicked.connect(self.add_pdfs)
        self.btn_remove.clicked.connect(self.remove_selected)
        self.btn_clear.clicked.connect(self.clear_files)
        self.btn_choose_output.clicked.connect(self.choose_output_path)
        self.btn_merge.clicked.connect(self.merge_pdfs)
        self.list_widget.itemSelectionChanged.connect(self._sync_buttons)

    def set_status(self, text: str):
        self.status_label.setText(text)

    def _sync_buttons(self):
        has_selection = self.list_widget.currentRow() >= 0
        self.btn_remove.setEnabled(has_selection)
        self.btn_merge.setEnabled(len(self.files) > 0)

    def add_pdfs(self):
        paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Selecionar PDFs",
            "",
            "PDF Files (*.pdf);;All Files (*)",
        )
        if not paths:
            return

        added = 0
        for p in paths:
            if not p.lower().endswith(".pdf"):
                continue
            if p not in self.files:
                self.files.append(p)
                added += 1
                item = QListWidgetItem(os.path.basename(p))
                item.setToolTip(p)
                self.list_widget.addItem(item)

        if added == 0:
            self.set_status("Nenhum PDF novo foi adicionado.")
        else:
            self.set_status(f"{added} PDF(s) adicionados.")

        self._sync_buttons()

    def remove_selected(self):
        row = self.list_widget.currentRow()
        if row < 0:
            return
        self.files.pop(row)
        self.list_widget.takeItem(row)
        self.set_status("Arquivo removido.")
        self._sync_buttons()

    def clear_files(self):
        self.files = []
        self.list_widget.clear()
        self.output_path.setText("")
        self.set_status("")
        self._sync_buttons()

    def choose_output_path(self):
        default_name = "merged_pdf.pdf"
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Salvar PDF mesclado como…",
            default_name,
            "PDF Files (*.pdf)",
        )
        if not path:
            return

        # Garante extensão .pdf
        if not path.lower().endswith(".pdf"):
            path += ".pdf"

        self.output_path.setText(path)
        self.set_status("Caminho de saída definido.")

    def merge_pdfs(self):
        if len(self.files) == 0:
            QMessageBox.warning(self, "Aviso", "Selecione pelo menos um PDF.")
            return

        out_path = self.output_path.text().strip()
        if not out_path:
            # Se o usuário não escolheu, pedimos aqui (UX melhor)
            self.choose_output_path()
            out_path = self.output_path.text().strip()
            if not out_path:
                return

        self.btn_merge.setEnabled(False)
        QApplication.setOverrideCursor(Qt.WaitCursor)

        try:
            merger = PyPDF2.PdfMerger()

            for p in self.files:
                # Abre em disco para PyPDF2 dar conta do parser/IO
                with open(p, "rb") as f:
                    merger.append(f)

            merger.write(out_path)
            merger.close()

            self.set_status("✓ PDFs mesclados com sucesso!")
            QMessageBox.information(self, "Sucesso", f"Arquivo gerado em:\n{out_path}")

        except Exception as e:
            self.set_status("")
            QMessageBox.critical(self, "Erro", f"Falha ao mesclar PDFs:\n{e}")
        finally:
            QApplication.restoreOverrideCursor()
            self._sync_buttons()


def main():
    # Garantir PyQt5 em modo correto
    app = QApplication(sys.argv)
    w = PdfMergerGUI()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

