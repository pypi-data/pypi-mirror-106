# -*- coding: utf-8 -*-

from cpskin.locales import CPSkinMessageFactory as _
from plone.dexterity.content import Container
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.interface import implementer


class IProcedure(model.Schema, IDexterityContent):
    """ Marker interface and Dexterity Python Schema for Procedure
    """

    e_guichet = schema.TextLine(title=_(u"E-Guichet"), required=False)


@implementer(IProcedure)
class Procedure(Container):
    """
    """
