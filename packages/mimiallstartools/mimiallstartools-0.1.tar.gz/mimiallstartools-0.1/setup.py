from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='mimiallstartools',
      version='0.1',
      long_description=long_description,
      long_description_content_type="text/markdown",
      description='mimi first package',
      url='https://github.com/mimiallstar',
      author='mimi huang',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['mimiallstartools'],
      zip_safe=False)
