from distutils.core import setup
setup(
  name = 'LowPowerEstimators',         
  packages = ['LowPowerEstimators'],   
  version = '1.0',      
  license='MIT',        
  description = 'resource efficient estimators',   
  author = 'Kaveh Kavianpour',                   
  author_email = 'Kaveh1@live.com',      
  url = 'https://github.com/Kevinmcsd/LowPowerEstimators',   
  download_url = 'https://github.com/Kevinmcsd/LowPowerEstimators/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  keywords = ['SEFR', 'Low Power Estimators', 'Low Memory Estimators', 'Fast Estimators'],   
  install_requires=[            
          'numpy',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Science/Research',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)