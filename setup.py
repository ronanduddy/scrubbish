import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='scrubbish-ronanduddy',
    version='0.0.1',
    author='Rónán Duddy',
    author_email='ronanduddy@live.ie',
    description='A pretty messy scraping package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ronanduddy/scrubbish',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
