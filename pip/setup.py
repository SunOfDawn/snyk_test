from setuptools import setup

setup(
    name='my_package',
    version='1.0',
    description='A Python package',
    author='Your Name',
    author_email='your@email.com',
    packages=['my_package'],
    install_requires=[
        'requests>=2.22.0',
        'numpy>=1.19.4'
    ],
)
