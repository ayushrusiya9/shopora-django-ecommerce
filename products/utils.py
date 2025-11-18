from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.http import HttpResponse

def render_to_pdf(template_src, context_dict={}):
    html = render_to_string(template_src, context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{context_dict["order"].uid}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation failed')
    return response
