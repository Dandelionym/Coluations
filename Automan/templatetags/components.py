from django import template
from django.db.models import Count
from django.db.models.functions import TruncMonth
from Automan.sqlHelper import SqlHelper
from .components_dashboard import  *

register = template.Library()


@register.inclusion_tag('components/navbar.html')
def get_header_info(username):
    
    username = username
    
    return locals()


@register.inclusion_tag('components/leftbar.html')
def left_bar():
    
    return locals()


@register.inclusion_tag('components/content.html')
def header_line():
    
    
    return locals()


@register.inclusion_tag('components/account_table.html')
def account_table():
    
    sql = SqlHelper()
    user_list = sql.get_list('select username, userwork, gender, birthday, university, religion from user_info', [])
    sql.close()
    
    return locals()
