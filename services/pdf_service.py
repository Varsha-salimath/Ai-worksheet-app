from fpdf import FPDF
from io import BytesIO
from utils.helpers import remove_emojis


class WorksheetPDF(FPDF):
    """Custom PDF class with footer disabled (we add our own footer manually)"""

    def __init__(self):
        super().__init__()
        # We disable built-in footer because we ONLY want a footer on last page
        self.added_disclaimer = False

    def footer(self):
        """
        Overridden footer so FPDF does NOT auto-add footer.
        We keep this empty.
        """
        pass


def add_last_page_disclaimer(pdf):
    """
    Draw a true fixed footer at the bottom of the LAST page.
    Uses absolute positioning so auto-page-break cannot move it.
    """

    pdf.set_font("Arial", "I", 8)
    pdf.set_text_color(120, 120, 120)

    disclaimer = (
        "Disclaimer: Worksheets are AI-generated and may contain inaccuracies. "
        "Please review before use."
    )

    # Move to absolute bottom position (5mm above bottom)
    page_width = pdf.w  # width of page
    pdf.set_xy(0, pdf.h - 15)   # <- REAL fixed footer bottom position
    pdf.cell(page_width, 10, disclaimer, align="C")


def create_worksheet_pdf(pdf_header, subject, chapter, grade, difficulty,
                         questions_list, answers_list, include_answers):

    pdf = WorksheetPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()
    pdf.set_margins(15, 15, 15)

    clean_header = remove_emojis(pdf_header)

    # ==================== HEADER ====================
    pdf.set_font("Arial", "B", 18)
    pdf.cell(0, 10, clean_header, ln=True, align="C")
    pdf.ln(2)

    # ==================== TITLE ====================
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"{subject} - {chapter} Worksheet", ln=True, align="C")
    pdf.ln(5)

    # ==================== DETAILS ====================
    pdf.set_font("Arial", "", 10)
    pdf.cell(90, 6, f"Grade: {grade}", border=0)
    pdf.cell(90, 6, f"Subject: {subject}", ln=True, border=0)
    pdf.cell(90, 6, f"Chapter: {chapter}", border=0)
    pdf.cell(90, 6, f"Difficulty: {difficulty}", ln=True, border=0)
    pdf.cell(90, 6, f"Total Questions: {len(questions_list)}", ln=True, border=0)
    pdf.ln(5)

    pdf.set_draw_color(0, 217, 255)
    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
    pdf.ln(8)

    # ==================== QUESTIONS ====================
    pdf.set_font("Arial", "B", 13)
    pdf.cell(0, 8, "Questions", ln=True)
    pdf.ln(3)

    for idx, question in enumerate(questions_list, 1):
        if pdf.get_y() > 250:
            pdf.add_page()

        pdf.set_font("Arial", "B", 11)
        clean_question = remove_emojis(question)
        pdf.multi_cell(0, 7, f"Q{idx}. {clean_question}")
        pdf.ln(4)

    # ==================== ANSWERS ====================
    if include_answers and answers_list:
        pdf.add_page()

        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Answer Key", ln=True, align="C")
        pdf.ln(5)

        pdf.set_draw_color(0, 217, 255)
        pdf.line(15, pdf.get_y(), 195, pdf.get_y())
        pdf.ln(8)

        for idx, answer in enumerate(answers_list, 1):
            if pdf.get_y() > 250:
                pdf.add_page()

            pdf.set_font("Arial", "B", 11)
            clean_answer = remove_emojis(answer)
            pdf.multi_cell(0, 7, f"A{idx}. {clean_answer}")
            pdf.ln(4)

    # ==================== TRUE BOTTOM DISCLAIMER ====================
    add_last_page_disclaimer(pdf)

    # ==================== SAVE PDF ====================
    pdf_output = BytesIO()
    pdf_bytes = pdf.output(dest='S')

    if isinstance(pdf_bytes, str):
        pdf_bytes = pdf_bytes.encode("latin1", errors="replace")

    pdf_output.write(pdf_bytes)
    pdf_output.seek(0)

    return pdf_output