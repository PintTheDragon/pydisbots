import setuptools

with open('README.md', 'r') as rm:
    long_desc = rm.read()
    
with open('requirements.txt', 'r') as rq:
    requirements = rq.readlines()

setuptools.setup(
    name='pydisbots',
    version='1.3.4',
    author='disbots.gg',
    description='An asynchronous wrapper for the disbots.gg API made in Python',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/disbots-gg/pydisbots',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements,
    python_requires='>=3.6'
)
