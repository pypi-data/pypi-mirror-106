import setuptools
from pathlib import Path

thisName    = "ConfigFileHelper"

baseURL     = f"https://github.com/theflyingbadger/{thisName}"

setuptools.setup  (name                          =  thisName
                  ,version                       =  Path('.\\src\\configFileHelper\\VERSION').read_text()
                  ,author                        =  "Jonathan Mills"
                  ,author_email                  =  "jon@badger.shoes"
                  ,description                   =  "Helper for config files"
                  ,long_description              =  Path("README.md").read_text()
                  ,long_description_content_type =  "text/markdown"
                  ,url                           =  baseURL
                  ,project_urls                  =  {"Bug Tracker"      :   f"{baseURL}/issues"
                                                    ,"Source"           :   baseURL
                                                    ,"Documentation"    :   f"{baseURL}/wiki"
                                                    }
                  ,classifiers                   =  ["Programming Language :: Python :: 3"
                                                    ,"License :: OSI Approved :: MIT License"
                                                    ,"Operating System :: OS Independent"
                                                    ]
                  ,package_dir                   =  {"": "src"}
                  ,packages                      =  setuptools.find_packages(where="src")
                  ,install_requires              =  Path("requirements.txt").read_text()
                  ,python_requires               =  '>=3.9'
                  )
