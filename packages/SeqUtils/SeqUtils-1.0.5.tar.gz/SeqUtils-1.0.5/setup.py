import setuptools.command.build_py
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

#custom post-installation steps go here:
class Install(_install):
    def run(self):
        _install.do_egg_install(self)
        #nothing else to do

setup(
    cmdclass={
        'install': Install,
    },
    name='SeqUtils',
    description='SeqUtils - general utilities to aid in system administration and analysis tasks',
    url='https://github.com/sequencecentral/SeqUtils.git',
    # git+https://github.com/sequencecentral/SeqUtils.git@main#egg=twitterbot
    author='Steve Ayers, Ph.D.',
    author_email='steve@sequenccecentral.com',
    # install_requires=[],
    version='1.0.5',
    license='MIT',
    # packages=['synchronicity','synchronicity.quotewidget'],
    # packages = find_packages(),
    packages = [
        'sequtils'
    ],
    include_package_data = True,
    # package_data={'': ['config.json','sources.json']},
    # Needed to actually package something
    # Needed for dependencies
    # install_requires=[''],
    # *strongly* suggested for sharing
    long_description=open('README.md').read(),
    install_requires=['bleach==3.3.0', 'certifi==2020.12.5', 'chardet==4.0.0', 'colorama==0.4.4', 'docutils==0.17.1', 'idna==2.10', 'importlib-metadata==4.0.1', 'keyring==23.0.1', 'packaging==20.9', 'pkginfo==1.7.0', 'Pygments==2.9.0', 'pyparsing==2.4.7', 'readme-renderer==29.0', 'requests==2.25.1', 'requests-toolbelt==0.9.1', 'rfc3986==1.5.0', 'SeqUtils==1.0.1', 'six==1.16.0', 'tqdm==4.60.0', 'twine==3.4.1', 'urllib3==1.26.4', 'webencodings==0.5.1', 'zipp==3.4.1'],
    # install_requires=open('requirements.txt').read(), #['click==7.1.2','joblib==1.0.1','nltk==3.6.1','regex==2021.4.4','tqdm==4.60.0'],
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

#to make an egg:
#python setup.py bdist_egg
#egg-info added