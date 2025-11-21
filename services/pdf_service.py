"""
Add this code to your existing pdf_service.py file
Update the create_worksheet_pdf function to include disclaimer at bottom
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from io import BytesIO

def create_worksheet_pdf(header, subject, chapter, grade, difficulty, questions, answers, include_answers):
    """
    Generate PDF worksheet with disclaimer at bottom
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=1*inch  # Extra space for disclaimer
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Heading1'],
        fontSize=16,
        textColor='#2563eb',
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='#1e40af',
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    info_style = ParagraphStyle(
        'InfoStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#4b5563',
        spaceAfter=6,
        alignment=TA_CENTER
    )
    
    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    answer_style = ParagraphStyle(
        'AnswerStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor='#059669',
        spaceAfter=10,
        alignment=TA_LEFT,
        fontName='Helvetica-Oblique'
    )
    
    disclaimer_style = ParagraphStyle(
        'DisclaimerStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor='#666666',
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique',
        spaceAfter=0
    )
    
    # Header
    story.append(Paragraph(header, header_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Title
    story.append(Paragraph(f"{subject} - {chapter}", title_style))
    story.append(Paragraph(f"{grade} | Difficulty: {difficulty}", info_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Questions Section
    story.append(Paragraph("<b>Questions:</b>", question_style))
    story.append(Spacer(1, 0.1*inch))
    
    for i, question in enumerate(questions, 1):
        q_text = f"<b>Q{i}.</b> {question}"
        story.append(Paragraph(q_text, question_style))
        story.append(Spacer(1, 0.15*inch))
    
    # Answer Key Section (if enabled)
    if include_answers and answers:
        story.append(PageBreak())
        story.append(Paragraph("<b>Answer Key:</b>", question_style))
        story.append(Spacer(1, 0.1*inch))
        
        for i, answer in enumerate(answers, 1):
            a_text = f"<b>A{i}.</b> {answer}"
            story.append(Paragraph(a_text, answer_style))
            story.append(Spacer(1, 0.1*inch))
    
    # Add flexible spacer to push disclaimer to bottom
    story.append(Spacer(1, 0.5*inch))
    
    # DISCLAIMER AT BOTTOM
    disclaimer_text = (
        "⚠️ Disclaimer: Worksheets are AI-generated and may contain inaccuracies. "
        "Please review content before use."
    )
    story.append(Paragraph(disclaimer_text, disclaimer_style))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


# ALTERNATIVE: Add disclaimer as footer on every page
def add_disclaimer_footer(canvas, doc):
    """
    Add disclaimer as footer on every page
    Use this with doc.build(story, onFirstPage=add_disclaimer_footer, onLaterPages=add_disclaimer_footer)
    """
    canvas.saveState()
    canvas.setFont('Helvetica-Oblique', 8)
    canvas.setFillColor('#666666')
    
    disclaimer = "⚠️ Disclaimer: Worksheets are AI-generated and may contain inaccuracies. Please review before use."
    
    # Center the text
    text_width = canvas.stringWidth(disclaimer, 'Helvetica-Oblique', 8)
    page_width = A4[0]
    x_position = (page_width - text_width) / 2
    
    canvas.drawString(x_position, 0.5*inch, disclaimer)
    canvas.restoreState()


# USAGE IN YOUR create_worksheet_pdf FUNCTION:
# Replace: doc.build(story)
# With: doc.build(story, onFirstPage=add_disclaimer_footer, onLaterPages=add_disclaimer_footer)