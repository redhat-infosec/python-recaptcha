try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(name='recaptcha-client',
      version='2.0.0',
      url = "https://github.com/redhat-infosec/python-recaptcha",
      author = "Ben Maurer, Richard Monk",
      author_email = "rmonk@redhat.com",
      description = "A plugin for reCAPTCHA and reCAPTCHA Mailhide",
      long_description = """\
Provides a CAPTCHA for Python using the reCAPTCHA service. Does not require
any imaging libraries because the CAPTCHA is served directly from reCAPTCHA.
Also allows you to securely obfuscate emails with Mailhide. This functionality
requires pycrypto. This library requires two types of API keys. If you'd like
to use the CAPTCHA, you'll need a key from https://www.google.com/recaptcha/admin/create.
For Mailhide, you'll need a key from http://www.google.com/recaptcha/mailhide/apikey.

There is also a Google Group at http://groups.google.com/group/recaptcha/.
Please use the associated mailing list for any questions or comments:
recaptcha@googlegroups.com. Like the Google Code project, the Google Group
mailing list is also shared among the several reCAPTCHA client implementations.

reCAPTCHA is written by Ben Maurer and maintained by Josh Bronson and Richard Monk. It is
licensed under an MIT/X11 license.
""",

      license = "MIT/X11",
      classifiers = [
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        ],


      packages = find_packages(),

      extras_require = {
        'mailhide' : ['pycrypto'],
        },
      namespace_packages = ['recaptcha'],
      )