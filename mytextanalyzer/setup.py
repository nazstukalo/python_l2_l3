from setuptools import setup, find_packages

setup(
    name='mytextanalyzer',
    version='0.1',
    description='text analyzer',
    url='https://github.com/nazstukalo/python_l2_l3/tree/main/textanalyzer',
    author='naz',
    author_email='nazar.stukalo@gmail.com',
    packages=find_packages(),
    install_requires=[
        'validators',
        'nltk'
    ],
    zip_safe=False
)
