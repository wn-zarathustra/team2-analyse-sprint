from setuptools import setup, find_packages

setup(
    name='team2-analyse',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package to calculate metrics using Eskom data.',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/wn-zarathustra/team2-analyse-sprint.git',
    author='Ahmed Jaffer, Nkosana Luvuyo, Wright Nyoka, Zintle Faltein-Maqubela',
    author_email='ahmedjaffer007@gmail.com, nkosanaluvuyo@gmail.com, wright.nyoka.ct@gmail.com, zintlefaltein.zf@gmail.com'
)