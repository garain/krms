from setuptools import setup 
#python setup.py sdist upload -r pypi

# reading long description from file 
with open('krms/DESCRIPTION.rst') as file: 
	long_description = file.read() 


# specify requirements of your package here 
REQUIREMENTS = ['plotly','sklearn','pandas'] 

# some more details 
CLASSIFIERS = [ 
	'Development Status :: 4 - Beta', 
	'Intended Audience :: Developers', 
	'Topic :: Internet', 
	'License :: OSI Approved :: MIT License', 
	'Programming Language :: Python', 
	'Programming Language :: Python :: 2', 
	'Programming Language :: Python :: 2.6', 
	'Programming Language :: Python :: 2.7', 
	'Programming Language :: Python :: 3', 
	'Programming Language :: Python :: 3.3', 
	'Programming Language :: Python :: 3.4', 
	'Programming Language :: Python :: 3.5'
	] 

# calling the setup function 
setup(name='krms', 
	version='0.0.2', 
	description='K-RMS unsupervised clustering algorithm.', 
	long_description=long_description,
	url='https://github.com/garain/krms', 
	author='Avishek Garain', 
	author_email='avishekgarain@gmail.com', 
	license='MIT', 
	packages=['krms'],
	package_data={'krms': ['DESCRIPTION.rst']},
	classifiers=CLASSIFIERS, 
	install_requires=REQUIREMENTS, 
	keywords='clustering visualize semisupervised'
	) 
