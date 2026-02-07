"""
CoalZero - PDF Export Module
Functions to generate professional PDF reports with proper formatting
"""

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime
import io


def generate_pdf_report(data):
    """
    Generate a comprehensive PDF report with proper CO2 subscript formatting
    
    Args:
        data (dict): Dictionary containing all emission data and results
    
    Returns:
        bytes: PDF file content
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter,
        rightMargin=72, 
        leftMargin=72,
        topMargin=72, 
        bottomMargin=18
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#27AE60'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        leading=14
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontSize=10,
        leading=12
    )
    
    # Style for table headers with WHITE text
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontSize=11,
        leading=13,
        textColor=colors.white,
        fontName='Helvetica-Bold'
    )
    
    # Title
    title = Paragraph("🌱 CoalZero Carbon Footprint Report", title_style)
    elements.append(title)
    
    # Subtitle with date
    subtitle_text = f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
    subtitle = Paragraph(subtitle_text, normal_style)
    elements.append(subtitle)
    elements.append(Spacer(1, 0.3*inch))
    
    # ==========================================
    # EXECUTIVE SUMMARY SECTION
    # ==========================================
    elements.append(Paragraph("Executive Summary", heading_style))
    
    summary_data = [
        [
            Paragraph('<b>Metric</b>', table_header_style), 
            Paragraph('<b>Value</b>', table_header_style)
        ],
        [
            Paragraph('Total Annual Emissions', table_cell_style), 
            Paragraph(f"{data['total_emissions']:.2f} tonnes CO<sub>2</sub>/year", table_cell_style)
        ],
        [
            Paragraph('Total Carbon Sinks', table_cell_style), 
            Paragraph(f"{data['total_sinks']:.2f} tonnes CO<sub>2</sub>/year", table_cell_style)
        ],
        [
            Paragraph('Net Emission Gap', table_cell_style), 
            Paragraph(f"{data['emission_gap']:.2f} tonnes CO<sub>2</sub>/year", table_cell_style)
        ],
        [
            Paragraph('Per Capita Emissions', table_cell_style), 
            Paragraph(f"{data['per_capita']:.2f} kg CO<sub>2</sub>/person/year", table_cell_style)
        ],
        [
            Paragraph('Number of Workers', table_cell_style), 
            Paragraph(f"{data['workers']}", table_cell_style)
        ],
    ]
    
    summary_table = Table(summary_data, colWidths=[3*inch, 3*inch])
    summary_table.setStyle(TableStyle([
        # Header row - Dark blue/gray background with WHITE text
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3E5771')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))
    
    elements.append(summary_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # ==========================================
    # OPERATIONAL DATA SECTION
    # ==========================================
    elements.append(Paragraph("Operational Data", heading_style))
    
    operational_data = [
        [
            Paragraph('<b>Parameter</b>', table_header_style), 
            Paragraph('<b>Value</b>', table_header_style), 
            Paragraph('<b>Unit</b>', table_header_style)
        ],
        [
            Paragraph('Diesel Consumption', table_cell_style),
            Paragraph(f"{data['diesel_litres']:,.0f}", table_cell_style),
            Paragraph('litres/year', table_cell_style)
        ],
        [
            Paragraph('Electricity Consumption', table_cell_style),
            Paragraph(f"{data['electricity_kwh']:,.0f}", table_cell_style),
            Paragraph('kWh/year', table_cell_style)
        ],
        [
            Paragraph('Coal Extracted', table_cell_style),
            Paragraph(f"{data['coal_extracted']:,.0f}", table_cell_style),
            Paragraph('tonnes/year', table_cell_style)
        ],
        [
            Paragraph('Average Transport Distance', table_cell_style),
            Paragraph(f"{data['transport_distance']:.0f}", table_cell_style),
            Paragraph('km', table_cell_style)
        ],
        [
            Paragraph('Plantation Area', table_cell_style),
            Paragraph(f"{data['plantation_area']:.1f}", table_cell_style),
            Paragraph('hectares', table_cell_style)
        ],
        [
            Paragraph('Number of Trees', table_cell_style),
            Paragraph(f"{data['num_trees']:,}", table_cell_style),
            Paragraph('count', table_cell_style)
        ],
    ]
    
    operational_table = Table(operational_data, colWidths=[2.5*inch, 2*inch, 1.5*inch])
    operational_table.setStyle(TableStyle([
        # Header row - Blue background with WHITE text
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498DB')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 1), (1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))
    
    elements.append(operational_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # ==========================================
    # EMISSION BREAKDOWN SECTION
    # ==========================================
    elements.append(Paragraph("Emission Sources Breakdown", heading_style))
    
    breakdown_data = [
        [
            Paragraph('<b>Source</b>', table_header_style), 
            Paragraph('<b>Emissions (kg)</b>', table_header_style), 
            Paragraph('<b>Emissions (tonnes)</b>', table_header_style), 
            Paragraph('<b>Percentage</b>', table_header_style)
        ],
        [
            Paragraph('Diesel Combustion', table_cell_style),
            Paragraph(f"{data['diesel_emissions']:,.2f}", table_cell_style),
            Paragraph(f"{data['diesel_emissions']/1000:.2f}", table_cell_style),
            Paragraph(f"{(data['diesel_emissions']/data['total_emissions_kg']*100):.1f}%" if data['total_emissions_kg'] > 0 else "0%", table_cell_style)
        ],
        [
            Paragraph('Electricity', table_cell_style),
            Paragraph(f"{data['electricity_emissions']:,.2f}", table_cell_style),
            Paragraph(f"{data['electricity_emissions']/1000:.2f}", table_cell_style),
            Paragraph(f"{(data['electricity_emissions']/data['total_emissions_kg']*100):.1f}%" if data['total_emissions_kg'] > 0 else "0%", table_cell_style)
        ],
        [
            Paragraph('Excavation', table_cell_style),
            Paragraph(f"{data['excavation_emissions']:,.2f}", table_cell_style),
            Paragraph(f"{data['excavation_emissions']/1000:.2f}", table_cell_style),
            Paragraph(f"{(data['excavation_emissions']/data['total_emissions_kg']*100):.1f}%" if data['total_emissions_kg'] > 0 else "0%", table_cell_style)
        ],
        [
            Paragraph('Transportation', table_cell_style),
            Paragraph(f"{data['transport_emissions']:,.2f}", table_cell_style),
            Paragraph(f"{data['transport_emissions']/1000:.2f}", table_cell_style),
            Paragraph(f"{(data['transport_emissions']/data['total_emissions_kg']*100):.1f}%" if data['total_emissions_kg'] > 0 else "0%", table_cell_style)
        ],
        [
            Paragraph('<b>TOTAL</b>', table_cell_style),
            Paragraph(f"<b>{data['total_emissions_kg']:,.2f}</b>", table_cell_style),
            Paragraph(f"<b>{data['total_emissions']:.2f}</b>", table_cell_style),
            Paragraph('<b>100%</b>', table_cell_style)
        ],
    ]
    
    breakdown_table = Table(breakdown_data, colWidths=[2*inch, 1.5*inch, 1.5*inch, 1*inch])
    breakdown_table.setStyle(TableStyle([
        # Header row - Red background with WHITE text
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E74C3C')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 1), (-1, -2), colors.white),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.lightgrey]),
    ]))
    
    elements.append(breakdown_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # ==========================================
    # GAP ANALYSIS SECTION
    # ==========================================
    elements.append(Paragraph("Gap Analysis", heading_style))
    
    if data['emission_gap'] > 0:
        status = "Carbon Positive"
        message = f"Your operation currently emits <b>{data['emission_gap']:.2f} tonnes</b> more CO<sub>2</sub> than it absorbs annually."
    else:
        status = "Carbon Neutral/Negative"
        message = "Congratulations! Your operation is carbon neutral or carbon negative."
    
    status_para = Paragraph(f"<b>Status:</b> {status}", normal_style)
    elements.append(status_para)
    elements.append(Spacer(1, 0.1*inch))
    
    message_para = Paragraph(message, normal_style)
    elements.append(message_para)
    elements.append(Spacer(1, 0.2*inch))
    
    if data['land_required'] > 0:
        land_para = Paragraph(
            f"<b>Land Requirement for Neutrality:</b> Approximately <b>{data['land_required']:.2f} hectares</b> "
            f"of additional plantation would be needed to achieve carbon neutrality.",
            normal_style
        )
        elements.append(land_para)
    
    elements.append(Spacer(1, 0.3*inch))
    
    # ==========================================
    # RECOMMENDATIONS SECTION
    # ==========================================
    elements.append(Paragraph("Recommendations", heading_style))
    
    recommendations = [
        "<b>1.</b> Consider electrifying a portion of your diesel-powered equipment to reduce emissions.",
        "<b>2.</b> Explore renewable energy sources (solar/wind) to reduce grid electricity dependence.",
        "<b>3.</b> Expand plantation and afforestation efforts to increase carbon absorption capacity.",
        "<b>4.</b> Implement regular monitoring and tracking of emissions to identify improvement areas.",
        "<b>5.</b> Consider purchasing carbon credits to offset remaining emissions while working toward neutrality."
    ]
    
    for rec in recommendations:
        rec_para = Paragraph(rec, normal_style)
        elements.append(rec_para)
        elements.append(Spacer(1, 0.08*inch))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # ==========================================
    # EMISSION FACTORS REFERENCE
    # ==========================================
    elements.append(Paragraph("Emission Factors Used", heading_style))
    
    factors_data = [
        [
            Paragraph('<b>Activity</b>', table_header_style),
            Paragraph('<b>Emission Factor</b>', table_header_style)
        ],
        [
            Paragraph('Diesel Combustion', table_cell_style),
            Paragraph('2.68 kg CO<sub>2</sub>/litre', table_cell_style)
        ],
        [
            Paragraph('Grid Electricity', table_cell_style),
            Paragraph('0.82 kg CO<sub>2</sub>/kWh', table_cell_style)
        ],
        [
            Paragraph('Coal Excavation', table_cell_style),
            Paragraph('0.15 kg CO<sub>2</sub>/tonne', table_cell_style)
        ],
        [
            Paragraph('Transportation', table_cell_style),
            Paragraph('0.062 kg CO<sub>2</sub>/tonne-km', table_cell_style)
        ],
        [
            Paragraph('Forest Absorption', table_cell_style),
            Paragraph('10,000 kg CO<sub>2</sub>/hectare/year', table_cell_style)
        ],
        [
            Paragraph('Tree Absorption', table_cell_style),
            Paragraph('22 kg CO<sub>2</sub>/tree/year', table_cell_style)
        ],
    ]
    
    factors_table = Table(factors_data, colWidths=[3*inch, 3*inch])
    factors_table.setStyle(TableStyle([
        # Header row - Gray background with WHITE text
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#95A5A6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.lightgrey]),
    ]))
    
    elements.append(factors_table)
    elements.append(Spacer(1, 0.4*inch))

    # ==========================================
    # IMPORTANT LINKS SECTION
    # ==========================================
    elements.append(Paragraph("Links to Important Government Organizations", heading_style))

    links_style = ParagraphStyle(
        'LinksStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        leftIndent=20
    )

    links_list = [
        '<b>1.</b> <link href="https://moef.gov.in/" color="blue"><u>https://moef.gov.in/</u></link> - Ministry of Environment, Forest and Climate Change',
        '<b>2.</b> <link href="https://cpcb.gov.in/" color="blue"><u>https://cpcb.gov.in/</u></link> - Central Pollution Control Board',
        '<b>3.</b> <link href="https://www.saytrees.org/" color="blue"><u>https://www.saytrees.org/</u></link> - Tree Planting NGO',
        '<b>4.</b> <link href="https://coalcontroller.gov.in/" color="blue"><u>https://coalcontroller.gov.in/</u></link> - Coal Controller\'s Organization (CCO)',
        '<b>5.</b> <link href="https://www.givemetrees.org/" color="blue"><u>https://www.givemetrees.org/</u></link> - Tree Planting Government NGO'
    ]

    for link_text in links_list:
        link_para = Paragraph(link_text, links_style)
        elements.append(link_para)
        elements.append(Spacer(1, 0.08*inch))

    elements.append(Spacer(1, 0.3*inch))
    
    # ==========================================
    # FOOTER
    # ==========================================
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER,
        leading=12
    )
    
    footer_text = (
        "<b>CoalZero - Carbon Neutrality Planning Tool</b><br/>"
        "This report was generated automatically based on provided operational data.<br/>"
        "For questions or support, contact your sustainability team."
    )
    footer = Paragraph(footer_text, footer_style)
    elements.append(footer)
    
    # Build PDF
    doc.build(elements)
    
    # Get the value of the BytesIO buffer and return it
    pdf = buffer.getvalue()
    buffer.close()
    
    return pdf