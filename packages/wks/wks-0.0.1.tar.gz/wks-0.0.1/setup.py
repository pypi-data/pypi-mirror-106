import setuptools

setuptools.setup(
    name="wks",
    version="0.0.1",
    author="Rhoban team",
    author_email="team@rhoban.com",
    description="Simple dependencies manager for cmake projects in your workspace",
    url="https://github.com/rhoban/wks/",
    packages=setuptools.find_packages(),
    scripts=['wks'],
    keywords="wks workspace deps",
    install_requires=[
        "colorama", "yaml"
    ],
    include_package_data=True,
    python_requires='>=3.6',
)
