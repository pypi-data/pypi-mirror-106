#!/usr/bin/env python
# coding: utf-8

# In[1]:


import setuptools

with open('C:/Users/Hindy/Desktop/Container_word_count_in_col/README.md', 'r') as fh:
    long_descripion = fh.read()
    
setuptools.setup(
    name='WordCountinColumn', 
    version='1.0.3',
    author='Hindy Yuen', 
    author_email='hindy888@hotmail.com',
    license='MIT',
    description='Count total number of appearance of words in a given pandas series', 
    long_description=long_descripion, 
    long_description_content_type='text/markdown', 
    url='https://github.com/HindyDS/Word-Count-in-Column', 
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
],
    keywords='Words word count counting pandas ',
    package_dir={"":"WordCountinColumn"},
    packages=['WordCountinColumn'],
    python_requires='>=3.6'
)

