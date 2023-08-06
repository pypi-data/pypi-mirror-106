from setuptools import setup, find_packages
 
 
 
setup(
    name='mytreepy',
    version='0.1',
    url='https://github.com/NoelBird/pytree',
    license='MIT',
    author='NoelBird',
    author_email='lduldu00228@gmail.com',
    description='tree command in cross platform',
    packages=find_packages(),
    long_description=open('README.md').read(),
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "treepy = treepy.main:main"
        ]
    },
)