from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name = 'NNSAtool',
    version = '0.0.7',
    description = 'Neural Network Semantic Analysis tool',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = '',
    author = 'Dmitry Paniavin',
    author_email = 'pndmev@gmail.com',
    license = 'MIT',
    classifiers = classifiers,
    keywords = 'Neural Network Semantic Analysis',
    packages = find_packages(),
    install_requires = ['transformers', 
                        'torch', 
                        'numpy',
                        'pandas']
)