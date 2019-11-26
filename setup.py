import setuptools

with open("README.txt", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    license = fh.read()

setuptools.setup(
  name='RaaspberryPiMovementDetector',
  packages=['RaaspberryPiMovementDetector'],
  version='0.3',
  description='Raspberry Movement Detector',
  long_description=long_description,
  author='KK Santhanam',
  author_email='KK.Santhanam@gmail.com',
  url='https://github.com/KSanthanam/RaspberryPiMovementDetector',
  download_url='https://github.com/KSanthanam/RaspberryPiMovementDetector/archive/v_01.tar.gz',
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
  ],
  license=license,
  keywords=['RaspberryPi', 'RaspberryPi IoT']
)
  # long_description_content_type="text/markdown",
  # setup_requires=['wheel']
  # install_requires=[
  #   'numpy',
  #   'scrapeasy'
  #   ],  
