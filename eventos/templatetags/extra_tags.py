# -*- coding: utf-8 -*-
from django.template import Library, Node, TemplateSyntaxError,VariableDoesNotExist,Variable
from django.db.models import Q
from datetime import *
from dateutil.relativedelta import *

register = Library()

class GetListIndex(Node):
    def __init__(self,varname,index):
        self.varname, self.index = varname, index

    def render(self, context):
        categorias = context[self.varname]
        try:
            index = Variable(self.index).resolve(context)
        except VariableDoesNotExist:
            value = "0"
        context['cat']=categorias[int(index)-1]
        return u''

def get_list_index(parser, token):
    bits = token.split_contents()
    return GetListIndex(bits[1], bits[2])

class MonthBelongEvent(Node):
    def __init__(self,mes_inicio,anyo_inicio,mes_comparado,anyo_comparado,frecuencia_evento):
        self.mes_inicio = mes_inicio
        self.anyo_inicio = anyo_inicio
        self.mes_comparado = mes_comparado
        self.anyo_comparado = anyo_comparado
        self.frecuencia_evento = frecuencia_evento

    def render(self, context):
        try:
            mes_inicio = Variable(self.mes_inicio).resolve(context)
            anyo_inicio = Variable(self.anyo_inicio).resolve(context)
            mes_comparado = Variable(self.mes_comparado).resolve(context)
            anyo_comparado = Variable(self.anyo_comparado).resolve(context)
            frecuencia_evento = Variable(self.frecuencia_evento).resolve(context)
        except VariableDoesNotExist:
            mes_inicio = self.mes_inicio
            anyo_inicio = self.anyo_inicio
            mes_comparado = self.mes_comparado
            anyo_comparado = self.anyo_comparado
            frecuencia_evento = self.frecuencia_evento

        date_inicial=date(anyo_inicio,mes_inicio,1)
        date_final=date(anyo_comparado,mes_comparado,1)
        delta=relativedelta(date_final,date_inicial)
        delta_months=int(delta.years)* 12 + int(delta.months)
        modulo = delta_months % int(frecuencia_evento)
        if(modulo == 0):
            context['belong_to_month'] = True
        else:
            context['belong_to_month'] = False
        return u''

def month_belong_event(parser, token):
    bits = token.split_contents()
    return MonthBelongEvent(bits[1], bits[2],bits[3],bits[4],bits[5])
    
    
class IncrementVarNode(Node):

    def __init__(self, var_name):
        self.var_name = var_name

    def render(self,context):
        value = context[str(self.var_name)]
        context[str(self.var_name)] = value + 1
        return u""

def increment_var(parser, token):

    parts = token.split_contents()
    if len(parts) < 2:
        raise TemplateSyntaxError("'increment' tag must be of the form:  {% increment <var_name> %}")
    return IncrementVarNode(parts[1])


from django import template
 
register = template.Library()

register.tag('increment', increment_var)
register.tag('get_list_index',get_list_index)
register.tag('month_belong_event',month_belong_event)


