# -*- coding: utf-8 -*-

from ajax_select import LookupChannel
from  .models import *
from django.utils.html import escape
from django.contrib.auth.models import *

class PersonalLookup(LookupChannel):

    model = User

    def get_query(self,q,request):
        return Group.objects.get(name="personal").user_set.filter(username__icontains=q)
        
    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.username
        
    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return u"<div><i>%s</i></div>" % (escape(obj.username))
        # return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"<div><i>%s</i></div>" % (escape(obj.username))
        
class SupervisorLookup(LookupChannel):

    model = User

    def get_query(self,q,request):
        return Group.objects.get(name="supervisores").user_set.filter(username__icontains=q)
        
    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.username
        
    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return u"<div><i>%s</i></div>" % (escape(obj.username))
        # return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"<div><i>%s</i></div>" % (escape(obj.username))
        
class ParteDeRepuestoLookup(LookupChannel):

    model = ParteDeRepuesto

    def get_query(self,q,request):
        return ParteDeRepuesto.objects.filter(m_Articulo__icontains=q)
        
    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the person typed """
        return obj.m_Articulo
        
    def format_match(self, obj):
        """ (HTML) formatted item for display in the dropdown """
        return u"<div><i>%s</i></div>" % (escape(obj.m_Articulo))
        # return self.format_item_display(obj)

    def format_item_display(self, obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        return u"<div><i>%s</i></div>" % (escape(obj.m_Articulo))



