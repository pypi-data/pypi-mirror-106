from setuptools import setup

setup(name='similar_words_vz',
      version='0.1',
      description='Looking for similar words in Bible.',
      packages=['similar_words_vz'],
      author_email='vl.sergiiy@gmail.com',
      install_requires=[
          'transformers', 'python-docx'
      ],
      include_package_data=True,
      zip_safe=False)
