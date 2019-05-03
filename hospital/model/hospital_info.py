# * - coding: utf - 8 -
from flectra import api, fields, models
from flectra.exceptions import ValidationError


class Hospitalinfo(models.Model):
    _name = "hospital.info"


    room_number = fields.Integer(string="Room Number", required=True)
    room_type = fields.Selection([('single', 'Single'), ('twin_sharing', 'twin sharing'), ('tripling', 'Tripling')],
                                 string="Room type", default='single')
    description = fields.Text(string="Description")
    operation_theater = fields.Integer(string="Operation theater", default=2, readonly='true')
    pharmacy = fields.Boolean(string="Pharmacy")
    start_date = fields.Date(string='Date')


    floor_id = fields.Many2one("hospital.floor", stirng="floor")

    @api.constrains('description')
    def check_description(self):
        if  len(self.description) < 10:
            raise ValidationError("must be written 10 characters.")

    @api.onchange('floor_id')
    def _onchange_floor_id(self):
        print("---------self------------------------",self.floor_id,self.room_type)
        self.room_type = self.floor_id.room_type


class Hospitalfloor(models.Model):
    _name = "hospital.floor"

    #@api.multi
    @api.depends('info_line')
    def _compute_total_rooms(self):
        for room in self:
            print ("-----------------------LEN-----------------",len(self.info_line))
            room.total_rooms = len(room.info_line)

    name = fields.Char(string="Floor no", required=True)
    code = fields.Char(string="Floor Code", size=3)
    room_type = fields.Selection([('single', 'Single'), ('twin_sharing', 'twin sharing'), ('tripling', 'Tripling')],
                                 string="Room type")
    info_line = fields.One2many("hospital.info", "floor_id", string="Room info")

    total_rooms = fields.Integer(string="Total Rooms",compute =_compute_total_rooms, store=True)

    facility_ids = fields.Many2many("hospital.facility", "floor_facility_rel","floor_id","facility_id", string="Facility")

class Hospitalfacility(models.Model):
    _name = "hospital.facility"

    name = fields.Char(string="Facility", required=True)
    ID = fields.Char(string="ID", required=True)
    floor_ids = fields.Many2many("hospital.floor", "floor_facility_rel", "facility_id", "floor_id",
                                    string="Floor")