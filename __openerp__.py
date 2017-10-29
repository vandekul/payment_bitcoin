{
    'name': "Bitcoin Payment Acquirer",
    'version': '1.0',
    'category' : 'Payment',
    'website': 'https://github.com/mumaker',
    'summary': 'Payment Acquirer: Bitcoin Implementation',
    'description': """Bitcoin Payment Acquirer""",
    'author': 'mumaker',
    'depends': ['payment'],
    'data': [
        'views/bitcoin.xml',
        'views/payment_acquirer.xml',
        'views/res_config_view.xml',
        'data/bitcoin.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
}