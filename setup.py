from setuptools import setup, find_packages

setup(
    name='httpc',
    packages=find_packages(),
    email='visnu8898@gmail.com',
    author='Visnunathan',
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

#TO INSTALL THE HTTPC COMMAND ON YOUR LOCAL MACHINE
#pip install --editable .