{
    'name': "Client Analysis Dashboard",
    'version': '0.1',
    'depends': ['base'],
    'author': "Power Partners",
    'company': "Power Partners",
    'category': 'Invoicing',
    'license': 'LGPL-3',
    'website': 'https://www.powerpartners.pro/',
    'images': ['static/description/cover.gif'],
    'description': """Connect your Odoo Data easily to this premade Power BI dashboard.""",
    'summary': """ This App allow to connect your Odoo invoicing data to a premade Power BI dashboard for Client Analysis.""",
    'live_test_url': "https://app.powerbi.com/view?r=eyJrIjoiMGU3ZDIyY2QtYTA1NC00ODA4LWI4MWItMDA4NWFjOGJlYWNjIiwidCI6IjNhYmFkYThkLWY1ZmUtNGVkNS1hMDNlLWU4ZGY2NzJlOTQ3MiIsImMiOjl9&pageName=ReportSection",
    'depends':['account'],
    'support': 'pwr@powerpartners.pro',
    'application': 'False',
    'assets': {
    'web.assets_frontend': [
        'static/src/xml/xml.xml',
        'static/src/css/odoo-website.webflow.css',
        'static/src/css/normalize.css',
        'static/src/css/webflow.css'
    ],
    'web.assets_common': [
        'static/src/xml/xml.xml',
        'static/src/css/normalize.css',
        'static/src/css/webflow.css'
    ],
},

}