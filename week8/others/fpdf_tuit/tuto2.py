from fpdf import FPDF
import fpdf

class PDF(FPDF):
    def header(self):

        self.image("./random_logo.png", x=fpdf.enums.Align.C ,)

        self.set_font("helvetica", style="B", size=15)

        self.cell(40,)

        self.cell(40, 15, "Random LOGO", 1, align="C")

        self.ln(40)

    def footer(self):

        self.set_y(-15)
        self.set_font("helvetica", style="I", size=8)

        self.cell(0,10,f"page {self.page_no()}/{{nb}}", align="C")


# instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_font("Times", size=12)

for i in range(1,51):
    pdf.cell(0, 10, f"LINE NO: {i}",new_x="LMARGIN", new_y="NEXT")
pdf.output("./tuto2.pdf")