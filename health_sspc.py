# -*- coding: utf-8 -*-
##############################################################################
#
#    SSPC - A holomedical health form that connects via web service with a client.
#    Created for the Cooperative Public Health System Holomedical Form
#     Copyright (C) 2012-2013  ale fernandez <ale@alefernandez.org.uk>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from trytond.model import ModelView, ModelSQL, fields


class Medicalperson(ModelSQL, ModelView):
    _name = 'gnuhealth.person'
    _description = __doc__

    ses = fields.Selection([
        ('0', 'Masculino'),
        ('1', 'Femenino'),
        ('2', 'Androgino'),
        ('3', 'Transsexual'),
        ('4', 'Intersex'),
        ('5', 'Transexual'),
        ], 'Sexo', help="Sexo - orientación", sort=False)

    education = fields.Selection([
        ('0', 'None'),
        ('1', 'Incomplete Primary School'),
        ('2', 'Primary School'),
        ('3', 'Incomplete Secondary School'),
        ('4', 'Secondary School'),
        ('5', 'University'),
        ], 'Education Level', help="Education Level", sort=False)

    housing = fields.Selection([
        ('0', 'Shanty, deficient sanitary conditions'),
        ('1', 'Small, crowded but with good sanitary conditions'),
        ('2', 'Comfortable and good sanitary conditions'),
        ('3', 'Roomy and excellent sanitary conditions'),
        ('4', 'Luxury and excellent sanitary conditions'),
        ], 'Housing conditions', help="Housing and sanitary living conditions", sort=False)

    hostile_area = fields.Boolean('Hostile Area',
        help="Check if person lives in a zone of high hostility (eg, war)")

    sewers = fields.Boolean('Sanitary Sewers')
    water = fields.Boolean('Running Water')
    trash = fields.Boolean('Trash recollection')
    electricity = fields.Boolean('Electrical supply')
    gas = fields.Boolean('Gas supply')
    telephone = fields.Boolean('Telephone')
    television = fields.Boolean('Television')
    internet = fields.Boolean('Internet')
    single_parent = fields.Boolean('Single parent family')
    domestic_violence = fields.Boolean('Domestic violence')
    working_children = fields.Boolean('Working children')
    teenage_pregnancy = fields.Boolean('Teenage pregnancy')
    sexual_abuse = fields.Boolean('Sexual abuse')
    drug_addiction = fields.Boolean('Drug addiction')
    school_withdrawal = fields.Boolean('School withdrawal')
    prison_past = fields.Boolean('Has been in prison')
    prison_current = fields.Boolean('Is currently in prison')
    relative_in_prison = fields.Boolean('Relative in prison',
        help="Check if someone from the nuclear family - parents / " \
        "sibblings  is or has been in prison")

    ses_notes = fields.Text('Nombre')

    ses_hora = fields.Text('A que hora está usted libre?')

    ses_lugar = fields.Text('Donde se le puede encontrar?')

	ses_grupos = fields.Text('Grupos a los que pertenece?')
	 
	ses_grupotipo = fields.Text('Tipo de grupo')

    fam_apgar_help = fields.Selection([
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Help from family',
        help="Is the person satisfied with the level of help coming from " \
        "the family when there is a problem ?", sort=False)

    fam_apgar_discussion = fields.Selection([
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Problems discussion',
        help="Is the person satisfied with the level talking over the " \
        "problems as family ?", sort=False)

    fam_apgar_decisions = fields.Selection([
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Decision making',
        help="Is the person satisfied with the level of making important " \
        "decisions as a group ?", sort=False)

    fam_apgar_timesharing = fields.Selection([
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Time sharing',
        help="Is the person satisfied with the level of time that they " \
        "spend together ?", sort=False)

    fam_apgar_affection = fields.Selection([
        ('0', 'None'),
        ('1', 'Moderately'),
        ('2', 'Very much'),
        ], 'Family affection',
        help="Is the person satisfied with the level of affection coming " \
        "from the family ?", sort=False)

    fam_apgar_score = fields.Integer('Score',
        help="Total Family APGAR \n" \
        "7 - 10 : Functional Family \n" \
        "4 - 6  : Some level of disfunction \n" \
        "0 - 3  : Severe disfunctional family \n",
        on_change_with=['fam_apgar_help', 'fam_apgar_timesharing',
        'fam_apgar_discussion', 'fam_apgar_decisions', 'fam_apgar_affection'])

    income = fields.Selection([
        ('h', 'High'),
        ('m', 'Medium / Average'),
        ('l', 'Low'),
        ], 'Income', sort=False)

    occupation = fields.Many2One('gnuhealth.occupation', 'Occupation')
    works_at_home = fields.Boolean('Works at home',
        help="Check if the person works at his / her house")
    hours_outside = fields.Integer('Hours outside home',
        help="Number of hours a day the person spend outside the house")

    def default_sewers(self):
        return 1

    def default_water(self):
        return 1

    def defaul_trash(self):
        return 1

    def default_electricity(self):
        return 1

    def default_gas(self):
        return 1

    def default_telephone(self):
        return 1

    def default_television(self):
        return 1

    def on_change_with_fam_apgar_score(self, vals):
        fam_apgar_help = int(vals.get('fam_apgar_help'))
        fam_apgar_timesharing = int(vals.get('fam_apgar_timesharing') or '0')
        fam_apgar_discussion = int(vals.get('fam_apgar_discussion') or '0')
        fam_apgar_decisions = int(vals.get('fam_apgar_decisions') or '0')
        fam_apgar_affection = int(vals.get('fam_apgar_affection') or '0')
        total = (fam_apgar_help + fam_apgar_timesharing +
            fam_apgar_discussion + fam_apgar_decisions +
            fam_apgar_affection)

        return total

Medicalperson()
