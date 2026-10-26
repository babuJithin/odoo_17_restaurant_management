{
    'name': "Android Mobile App for Restaurant Food Ordering Application",
    'category': 'Generic Modules',
    'sequence': 10,
    'version': '17.0.1.0',
    'license': 'Other proprietary',
    'author': "Infintor Solutions",
    "price": 150,
    "currency": 'USD',
    'website': "https://www.infintor.com",
    'summary': """
    
              Restaurant e-commerce app builder enables businesses to effortlessly create and customize mobile or web storefronts. With an intuitive interface, a wide range of design options, and built-in tools for product, inventory, and order management, it streamlines the process of launching online stores quickly and efficiently.

    """,
    'description': """
    
               Restaurant  e-commerce app builder enables businesses to effortlessly create and customize mobile or web storefronts. With an intuitive interface, a wide range of design options, and built-in tools for product, inventory, and order management, it streamlines the process of launching online stores quickly and efficiently.

    """,
    'website': 'infintor.in',
    'demo': [],
    'images': [],
    'depends': ['base', 'sale_management', 'product', 'website_sale','website_sale_wishlist','delivery','stock'],
    'images': ['static/description/banner.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/otp_signup_templates_email.xml',
        'store_front_views/banner_views.xml',
        'store_front_views/deal_views.xml',
        'brand_views/brand_views.xml'
    ],
    'installable': True,
    'application': True,
}
