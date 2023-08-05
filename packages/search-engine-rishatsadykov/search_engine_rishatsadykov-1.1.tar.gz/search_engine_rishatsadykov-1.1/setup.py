from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'DAWG-Python==0.7.2',
    'docopt==0.6.2',
    'psycopg2==2.8.6',
    'pymorphy2==0.9.1',
    'pymorphy2-dicts-ru==2.4.417127.4579844'
]

setup(
    name='search_engine_rishatsadykov',
    version='1.1',
    packages=['lemmatization'],
    url='https://github.com/rishat11/information-retrieval',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    author='Rishat Sadykov',
    author_email='r.sadickov2010@yandex.ru',
    description='Calculates TF-IDF for data set',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    python_requires='>=3.6',
)
