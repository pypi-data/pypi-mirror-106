import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "halloumi-ses-user",
    "version": "0.0.1",
    "description": "halloumi-ses",
    "license": "Apache-2.0",
    "url": "https://github.com/sentialabs/halloumi-ses-user.git",
    "long_description_content_type": "text/markdown",
    "author": "Sentia<support.mpc@sentia.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/sentialabs/halloumi-ses-user.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "halloumi_ses_user",
        "halloumi_ses_user._jsii"
    ],
    "package_data": {
        "halloumi_ses_user._jsii": [
            "halloumi-ses@0.0.1.jsii.tgz"
        ],
        "halloumi_ses_user": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-iam>=1.73.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.73.0, <2.0.0",
        "aws-cdk.core>=1.73.0, <2.0.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.29.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
