import setuptools

with open('README.md', 'r') as rm:
    long_desc = rm.read()

setuptools.setup(
    name='pydisbots',
    version='1.0.2',
    author='Iapetus-11',
    description='An async wrapper for the disbots.gg API made in Python',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/disbots-gg/pydisbots',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)
