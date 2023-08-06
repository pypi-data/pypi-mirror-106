from distutils.core import setup

setup(
    name='pyepipolicy',
    packages=['pyepipolicy'],
    version='0.1',
    license='MIT',
    description='EpiPolicy Python Connector',
    author='HudaLab NYUAD',
    author_email='hudalab.nyuad@gmail.com',
    url='https://github.com/miromannino/pyepipolicy',
    download_url='https://github.com/miromannino/pyepipolicy/archive/refs/tags/0.1.tar.gz',
    keywords=['Epidemic', 'EpidemicSimulator', 'EpiPolicy', 'Connector'],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
