from setuptools import setup,find_packages

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
]
setup(
   name='pyBaseN',
   version='0.0.1',
   description='A simple tool based on Luhn Algorithm)',
   long_description=open('README.txt').read(),
   long_description_content_type='text/markdown',
   url='',
   author='C Lokesh Kumar Reddy',
   author_email='lokeshkumarreddy.c@gmail.com',
   license='MIT',
   classifiers=classifiers,
   keywords='pyBaseN',
   packages=find_packages(),
   install_requires=[] #external packages as dependencies
)
