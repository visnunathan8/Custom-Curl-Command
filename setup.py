from setuptools import setup, find_packages

setup(
    name='httpc',
    packages=find_packages(),
    email='gmartins@fancywhale.ca',
    author='Gui Martins',
    install_requires=[
        'click',
        'requests'
    ],
    version='0.0.1',
    entry_points='''
    [console_scripts]
    httpc=httpc:httpc
    '''
)