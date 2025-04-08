from setuptools import setup, find_packages


setup(
    name='django-weird-calcu',
    version='1.0.0',
    author='fe7h',
    packages=find_packages(),
    url='https://github.com/fe7h/Django-Weird-Calcu',
    platform='OS Independent',
    install_requires = [
        'Django',
        'Pillow',
    ],
    include_package_data=True,
)