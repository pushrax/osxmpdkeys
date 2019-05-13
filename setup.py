from setuptools import setup

setup(
    name='osxmpdkeys',
    version='1.0.2',
    description='Control mpd with the OS X media keys.',
    long_description=open('README.rst').read(),
    author='Justin Li',
    author_email='jli@j-li.net',
    url='https://github.com/pushrax/osxmpdkeys',
    license='MIT',
    packages=[
        'osxmpdkeys'
    ],
    scripts=[
        'mpdkeys'
    ],
    install_requires=[
        'osxmmkeys>=1.0.0',
        'python-mpd2>=0.5',
        'argparse',
    ],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ]
)

