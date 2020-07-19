#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
report = SimpleDocTemplate("<>/py_pdf.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("complete inventory of my fruit",styles["h1"])
fruits = {'banana':4,'mango':9}
fruits_list = []
for key,val in fruits.items():
    fruits_list.append([key,val])
report_table = Table(data = fruits_list)
report_para = Paragraph("this is my complete fruits list", styles["BodyText"])
report.build([report_title,report_para,report_table])
