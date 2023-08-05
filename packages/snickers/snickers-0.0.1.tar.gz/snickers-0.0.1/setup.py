from setuptools import setup

__project__ = "snickers"
__version__ = "0.0.1"
__description__ = "a python module(in construction) used as a helping hand for Artificial Intelligence(ai) and Machine Learning(ml) developers. typically a quick and easy way to introduce ai and ml for complete beginners..."
__packages__ = ["snickers"]
__author__ = "Syntax"
__author_email__  = "outreach.syntax@gmail.com"
__keywords__ = ['snickers', 'artificial intelligence', 'ai', 'ml', 'machine learning', 'beginner', 'learning']
__requires__ = ["random"]

setup(
    name = __project__,
    version = __version__,
    description = __description__,
    packages = __packages__,
    author = __author__,
    author_email = __author_email__,
    keywords = __keywords__,
    requires = __requires__
)