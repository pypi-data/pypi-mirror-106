# Import our newly installed setuptools package.
import setuptools

# Opens our README.md and assigns it to long_description.
with open("README.md", "r") as fh:
    long_description = fh.read()

# Defines requests as a requirement in order for this package to operate. The dependencies of the project.
requirements = [
    "Django>=2.0.13",
    "django-tempus-dominus==5.1.2.13",
    "django-bootstrap3==12.0.2",
    "django-select2==7.0.2",
    "django-datetime-widget2==0.9.5",
    "Babel==1.0",
    "python-dateutil==2.2",
    "django-classy-tags==0.5.1"
]

# Function that takes several arguments. It assigns these values to our package.
setuptools.setup(
    # Distribution name the package. Name must be unique so adding your username at the end is common.
    name="TPL_Accounting",
    # Version number of your package. Semantic versioning is commonly used.
    version="1.1",
    # Author name.
    author="Mohammad Rajib",
    # Author's email address.
    author_email="rajib.conf@gmail.com",
    # Short description that will show on the PyPi page.
    description="A TPL_Accounting pluggable package",
    # Long description that will display on the PyPi page. Uses the repo's README.md to populate this.
    long_description=long_description,
    # Defines the content type that the long_description is using.
    long_description_content_type="text/markdown",
    # The URL that represents the homepage of the project. Most projects link to the repo.
    url="https://github.com/github-rajib/TPL_Accounting",
    # Now you see a new release and under Assets, there is a link to Source Code (tar.gz).
    download_url="https://github.com/github-rajib/TPL_Accounting/archive/refs/tags/v1.0.tar.gz",
    # Keywords that define your package best
    keywords=['TPL Accounting', 'Django Accounting', 'Accounting'],
    # Finds all packages within in the project and combines them into the distribution together.
    # packages=setuptools.find_packages(),
    # Chose the same as "name"
    packages=['TPL_Accounting'],
    include_package_data=True,
    # requirements or dependencies that will be installed alongside your package when the user installs it via pip.
    install_requires=requirements,
    # Gives pip some metadata about the package. Also displays on the PyPi page.
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # The version of Python that is required.
    python_requires='>=3.6',
)
