from fpdf import FPDF
import fpdf
pdf = FPDF(orientation="L", unit="mm", format="A4")

pdf.add_page()
pdf.set_font("helvetica", style="B", size=46)
pdf.cell(0, 10, "hello World!", 1,)
pdf.cell(0, 10, "Powered by FPDF.", new_x="LMARGIN", new_y="NEXT", align="C",)
pdf.output("./tuto1.pdf")
