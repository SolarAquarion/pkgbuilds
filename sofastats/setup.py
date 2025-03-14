import io, sys
from setuptools import setup

setup(
name         = 'sofastats',
description  = 'Statistics Open For All',
version      = '1.5.6',
author       = 'Grant Paton-Simpson',
author_email = 'grant@sofastatistics.com',
package_dir  = {'sofastats':'sofa_main'},
packages     = ['sofastats', 
                'sofastats.boomslang', 
                'sofastats.dbe_plugins'], 
package_data = {'sofastats':['css/*', 
                             'images/*', 
                             '_internal/*', 
                             'locale/br/LC_MESSAGES/sofastats.mo', 
                             'locale/ca_ES/LC_MESSAGES/sofastats.mo', 
                             'locale/de_DE/LC_MESSAGES/sofastats.mo', 
                             'locale/en_GB/LC_MESSAGES/sofastats.mo', 
                             'locale/es_ES/LC_MESSAGES/sofastats.mo', 
                             'locale/fr_FR/LC_MESSAGES/sofastats.mo', 
                             'locale/gl_ES/LC_MESSAGES/sofastats.mo', 
                             'locale/hr_HR/LC_MESSAGES/sofastats.mo', 
                             'locale/it_IT/LC_MESSAGES/sofastats.mo', 
                             'locale/mn/LC_MESSAGES/sofastats.mo', 
                             'locale/pt_BR/LC_MESSAGES/sofastats.mo', 
                             'locale/ru_RU/LC_MESSAGES/sofastats.mo', 
                             'locale/sl_SL/LC_MESSAGES/sofastats.mo', 
                             'locale/tr_TR/LC_MESSAGES/sofastats.mo', 
                             'projs/*', 
                             'reports/sofastats_report_extras/*', 
                             'vdts/*']}
)
