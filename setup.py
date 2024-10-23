import setuptools

with open("README.md", "r" , encoding = "utf-8") as fh:
    description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME = "bhattad-ankur"
SRC_REPO = "https://github.com/bhattad-ankur/Text-Summarization"
AUTHOR_EMAIL = "ankurbhattad04@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="An advanced Natural Language Processing (NLP) model for text summarization.",
    long_description=description,
    long_description_content_type="text/markdown",
    url=SRC_REPO,
    project_urls={
        "Bug Tracker": "https://github.com/bhattad-ankur/Text-Summarization/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(),
)