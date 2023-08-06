from setuptools import setup, find_packages

VERSION = '1.0.0'
SHORT_DESC = 'A simple CLI program to add lyrics to your mp3 files.'

def long_description():
    LONG_DESC = ''
    with open('README.md', encoding='utf-8') as f:
        LONG_DESC += f.read()
    with open('CHANGELOG.txt', encoding='utf-8') as f:
        LONG_DESC += '\n\n' + f.read()
    return LONG_DESC

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
        
    return requirements

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: End Users/Desktop',
    'Programming Language :: Python :: 3',
    'Operating System :: Microsoft :: Windows',
    'License :: OSI Approved :: MIT License',
    'Topic :: Multimedia :: Sound/Audio'
]

setup(
    name='lyrify',
    version=VERSION,
    description=SHORT_DESC,
    long_description=long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    license='MIT',
    classifiers=classifiers,
    author='Benedikt Mielke',
    author_email='xbenmmusicx@gmail.com',
    keywords=['music', 'tagger', 'tag', 'genius', 'lyrics', 'mp3', 'mutagen', 'song', 'sing'],
    entry_points='''
        [console_scripts]
        lyrify=lyrify.lyrify:lyrify_cli
    '''
)