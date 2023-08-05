from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Hi_Aviv',
    version='0.0.2',
    description='Hi Aviv is the personal assistant for your computer!',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.TXT').read(),
    url='',
    author='aviv05423',
    author_email='avivb60@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='assistant, Aviv, personal assistant, Voice assistant, Virtual Assistant',
    packages=find_packages(),
    install_requires=['']
)
