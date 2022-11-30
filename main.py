import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors





report_text = st.selectbox('כריכים :', ('חביתה', 'Tuna'))

export_as_pdf = st.button("שמור")

if report_text == 'חביתה':
    report_text = 'omlet'

if export_as_pdf:
    fileName = 'order.pdf'
    documentTitle = 'sample'
    title = 'Order'
    subTitle = 'Sandwitches!!'
    textLines = [
        str(report_text),
        'Tuna',
    ]

    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)

    pdf.drawCentredString(300, 770, title)
    pdf.line(30, 710, 550, 710)
    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    for line in textLines:
        text.textLine(line)
    pdf.drawText(text)
    pdf.save()


    with open("order.pdf", "rb") as file:
        btn = st.download_button(
            label="הורד",
            data=file,
            file_name="order.pdf",
            mime="pdf/png"
        )