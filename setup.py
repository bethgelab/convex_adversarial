from setuptools import find_packages, setup

setup(
    name='convex_adversarial',
    version='0.3.2',
    description="A library implementing robust loss functions for ReLU based neural networks. ",
    author='Eric Wong',
    author_email='ericwong@cs.cmu.edu',
    platforms=['any'],
    license="MIT",
    url='https://github.com/locuslab/convex_adversarial',
    packages=['convex_adversarial'],
    install_requires=[
        'torch==0.4',
        'foolbox==1.6.2'
    ]
)
