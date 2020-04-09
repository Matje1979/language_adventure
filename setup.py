try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'scena u igrici',
    'author': 'Damir Cicic',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'damircicic@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['bin'],
    'scripts': ['bin\game.py'],
    'name': 'game.py'
}

setup(**config)