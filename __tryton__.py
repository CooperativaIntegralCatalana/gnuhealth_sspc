# -*- coding: utf-8 -*-
##############################################################################
#
#    sspc - A holomedical health form that connects via web service with a client.
#    Copyright (C) 2012-2013  ale fernandez <ale@alefernandez.org.uk>
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
{
    'name': 'Cooperative public health system - holomedical diagram',
    'version': '2.4.0',
    'author': 'CIC',
    'email': 'informatica@aureasocial.org',
    'website': 'http://cac.cooperativaintegral.cat',
    'depends': [
        'health',
    ],
    'name_es_ES': 'Sistema de salúd pública cooperativista - diagrama holomedico',
    'translation': ['locale/es_ES.po', 'locale/es_CA.po', 'locale/el.po',
        'locale/fa.po','locale/it.po'],
    
    'description': '''

This module takes care of the input of all the holomedical factors that influence the health of the individual / family, neighbourhood, collective and society.

Among others, we include the following factors :

- Time / Space relationships (when are they free, where are they, how can they meet other people)
- Social (what groups you/it belongs to: family, neighbourhood etc)
- Economics (CES / Triodos account info)
- Personal
- Spaces and environments (access, resources)

''',
    'description_es_ES': '''
Este módulo se encarge de ingresar y procesar los factores holomedicos que influyen en la salud del individuo, su familia, barrio, colectivo y sociedad.

Algunos aspectos que abarca :

- Relaciones espacio tiempo (a que hora está libre / donde está / cuando encaja con otra persona)
- Social (a que grupos pertenece y tipo: familia, barrio, colectivo etc)
- Economia (cuenta CES / Triodos)
- Personal
- Espacios y entornos (acesos, recursos)

''',

    'xml': [
        'health_sspc_view.xml',
    ],
    'active': False,
}
