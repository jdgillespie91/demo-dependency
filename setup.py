from setuptools import setup, find_packages

setup(
    name='demo-dependency',
    version='1.0.0',
    packages=find_packages(),
    description='An HTTP API with unpredictable behaviour!',
    author='Jake Gillespie',
    author_email='jdgillepsie91@gmail.com',
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'flask',
        'gunicorn',
    ],
)
