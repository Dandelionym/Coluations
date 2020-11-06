from django import template
from django.db.models import Count
from django.db.models.functions import TruncMonth


register = template.Library()


@register.inclusion_tag('components/dashboard/four_center_box.html')
def four_center_box():
	
	return


@register.inclusion_tag('components/dashboard/view_line_box.html')
def view_line_box():
	
	return