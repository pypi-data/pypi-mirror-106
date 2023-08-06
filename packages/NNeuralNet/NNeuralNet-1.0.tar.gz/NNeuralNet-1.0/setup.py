import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='NNeuralNet',  
     version='1.0',
     author="Praveen Gorre,Viswanath Tadi",
     author_email="cs18b047@smail.iitm.ac.in",
     description="Implementation of a Feed Forward Neural Network",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/dl-thops/NeuralNet",
     python_requires='>=3.6',
     packages=setuptools.find_packages(),
     install_requires=[ 'numpy>=1.18',
                        'tqdm>=4.1.0'],
     platforms=['Windows', 'Linux', 'Mac OS X'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]
 )
