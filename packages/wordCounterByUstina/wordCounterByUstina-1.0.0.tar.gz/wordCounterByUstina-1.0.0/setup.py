import setuptools
import wordCounter


with open('readme.md') as fr:
    long_description = fr.read()


setuptools.setup(
    name='wordCounterByUstina',
    version=wordCounter.__version__,
    author='Kuzminskaya U.A.',
    author_email='ustina.kuzminskaya@mail.ru',
    description='Search for the number of words in a directory',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kuzminskayaaa/wordCcounter',
    packages=setuptools.find_packages(),
    install_requires=[
        
    ],
    test_suite='tests',
    python_requires='>=3.7',
    platforms=["any"]
)