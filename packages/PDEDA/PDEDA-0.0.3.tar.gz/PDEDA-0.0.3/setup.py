from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
  

]
 
setup(
  name='PDEDA',
  version='0.0.3',
  description='Automate Exploratory Data Analysis',
  long_description=open('README.md').read()+'\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/vishalbpatil1/plotly-dash-eda',  
  author='Vishal Patil',
  author_email='vishalbpatil1@gmail.com',
  license='MIT', 
  classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"],
  keywords='Exploratory Data Analysis', 
  packages=find_packages(),
  install_requires=['pandas','scipy','plotly','numpy','sklearn','dash','jupyter_dash','dash_table','statsmodels','dash_core_components',
  'dash_html_components','dash_bootstrap_components', 'pybase64'],
# #external packages as dependencies
 #include_package_data=True,
 #package_data={'':['result1.png','result2.png','result3.png']}

)



#open('README.txt').read() + '\n\n'+