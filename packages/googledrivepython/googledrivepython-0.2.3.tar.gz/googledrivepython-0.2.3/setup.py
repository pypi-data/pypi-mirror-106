from distutils.core import setup
version = '0.2.3'
setup(
  name = 'googledrivepython',         
  packages = ['googledrivepython'],   
  version = version,      
  license='MIT',        
  description = 'A python Google Drive API v3 wrapper',   
  author = 'Luyanda Dhlamini',                   
  author_email = 'luyanda.dhlamini@gmail.com',  
  url = 'https://github.com/luyandadhlamini',   
  download_url = 'https://github.com/luyandadhlamini/googledrivepython/archive/refs/tags/v{}.tar.gz'.format(version), 
  keywords = ['Python', 'Google Drive', 'drive', 'API', 'wrapper' ],   
  install_requires=[            
          'oauth2-client',
          'google-api-python-client'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
    long_description = """# googledrivepython
    A python Google Drive API v3 wrapper that enables:
    * Uploading of files to Google Drive
    * Listing of all files & folders available to a service account.
    * Sharing of files with a list of email addresses""",
    long_description_content_type = 'text/markdown',
)
