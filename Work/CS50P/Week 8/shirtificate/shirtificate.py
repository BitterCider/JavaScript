from fpdf import FPDF

class PDF(FPDF):
    def header(self):

        self.image("shirtificate.png", 30, 40, 150)

        self.set_font("helvetica", "B", 40)

        self.cell(80)

        self.cell(30, 20, "CS50 Shirtificate", border=0, align="C")

        self.ln(20)



pdf = PDF()
pdf.add_page()
pdf.set_line_width(1.2)
pdf.set_draw_color(r=100, g=160, b=150)
pdf.line(x1=65, y1=103, x2=145, y2=103)
pdf.set_font("helvetica", "B", 30)
pdf.set_y(90)
pdf.set_x(68)
pdf.set_text_color(r=100, g=160, b=150)
pdf.cell(13, 10, f"T.B took CS50", ln=True)
pdf.output("shirtificate.pdf")

