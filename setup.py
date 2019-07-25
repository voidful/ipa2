from setuptools import setup, find_packages


setup(
    name='ipa2',
    version='0.6.0',
    description='Tools for convert Text to IPA in python',
    long_description="Github : https://github.com/voidful/ipa2",
    url='https://github.com/voidful/ipa2',
    author='voidful',
    author_email='voidful.stack@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='nlp file io string text mining ipa voice',
    packages=find_packages()
)
