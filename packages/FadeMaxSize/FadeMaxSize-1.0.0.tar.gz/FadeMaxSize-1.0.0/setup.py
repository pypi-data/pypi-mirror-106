import setuptools
import FadeMaxSize


with open('readme.md') as fr:
    long_description = fr.read()


setuptools.setup(
    name='FadeMaxSize',
    version=FadeMaxSize.__version__,
    author='Petrov D.S.',
    author_email='pvrple.drank.xvi@gmail.com',
    description='Search for file with maximum size',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/whyfade/FadeMaxSize',
    packages=setuptools.find_packages(),
    install_requires=[
        
    ],
    test_suite='tests',
    python_requires='>=3.7',
    platforms=["any"]
)