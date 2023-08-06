import time

from stdnum.es import dni
from stdnum.es import nie
from odoo import models, fields, api
from odoo.tools.translate import _

class sm_member(models.Model):
  _inherit = 'res.partner'
  _name = 'res.partner'

  id_document_type = fields.Selection([
    ('dni', 'DNI'),
    ('nie', 'NIE'),
  ], string=_("ID Document"), compute="_set_id_document_type", store=True)
  driving_license_expiration_date = fields.Char(string=_("Driving license expiration date"))
  image_dni = fields.Char(string=_("DNI image"))
  image_driving_license = fields.Char(string=_("Driving license image"))
  related_representative_member_id = fields.Many2one('res.partner',string=_("Related represented member"),compute="_get_related_representative_member_id",store=False)

  # for email templates
  member_email_date = fields.Char(string=_("Current date"), compute='get_current_date', store=False)

  #_order = "cooperator_register_number desc"

  def get_current_date(self):
    for record in self:
      record.member_email_date = time.strftime("%d/%m/%Y")

  # Simple way to override and skip VAT validation that was causing trouble when setting a country
  @api.constrains('vat', 'country_id')
  def check_vat(self):
    return True

  @api.depends('vat')
  def _set_id_document_type(self):
    for record in self:
      if record.company_type == 'person':
        dni_nie = record.vat
        if dni_nie:
          if dni.is_valid(dni_nie):
            record.id_document_type = "dni"
          elif nie.is_valid(dni_nie):
            record.id_document_type = "nie"

  # Simple way to override and skip VAT validation that was causing trouble when setting a country
  @api.constrains('vat', 'country_id')
  def check_vat(self):
    return True

  def _get_related_representative_member_id(self):
    for record in self:
      related_representative = record.get_representative()
      if related_representative:
        record.related_representative_member_id = related_representative.id
