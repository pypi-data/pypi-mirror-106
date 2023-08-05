from setuptools import setup
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.txt").read_text() + "\n\n" + (HERE / "CHANGELOG.txt").read_text()

setup(
  name='cowinapi_by_ishaan',
  version='0.0.3',
  description='Vaccine availability',
  long_description=README,
  long_description_content_type="text/markdown",  
  url='https://in.linkedin.com/in/ishaangupta1201',  
  author='Ishaan Gupta',
  author_email='solotechfeedback@gmail.com',
  license='Apache License 2.0', 
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Topic :: Internet',
  ],
  keywords='cowin,covid,vaccine,vaccine booking,cowin registrarion,python cowin,cowin pip', 
  packages=['cowinapi_by_ishaan'],
  python_requires='>=3.6,<4', 
  install_requires=[
        'fake-useragent',
        'datetime',
        'pytest',
        'requests',
        'pandas',
  ],
)