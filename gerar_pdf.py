from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, self.title, ln=True, align="C")
        self.ln(10)

    def add_slide(self, title, content):
        self.add_page()
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", "", 12)
        for line in content.split("\n"):
            self.multi_cell(0, 10, line)
        self.ln()

slides = [
    ("Por que supercomputadores usam Linux?", ""),
    ("Fatos rápidos",
     "- Mais de 95% dos supercomputadores usam Linux\n"
     "- Fonte: Top500.org\n"
     "- Sistema estável, rápido e flexível"),
    ("Vantagens do Linux",
     "✅ Gratuito\n"
     "✅ Código aberto e personalizável\n"
     "✅ Suporte a HPC (MPI, SLURM)\n"
     "✅ Roda dias ou semanas sem travar"),
    ("Exemplos Reais",
     "- Frontier (EUA) – Mais rápido do mundo\n"
     "- Fugaku (Japão) – Pesquisa sobre COVID-19\n"
     "- LUMI (Europa) – Ciência e inteligência artificial"),
    ("Conclusão",
     "Linux é o sistema ideal para supercomputadores:\n"
     "Leve, poderoso, flexível e feito para alta performance.")
]

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.title = "Supercomputadores e Linux (Resumo)"

for title, content in slides:
    pdf.add_slide(title, content)

pdf.output("Supercomputadores_Linux_Resumo.pdf")


