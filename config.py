"""
    the configs.
"""

# storage
AWS_ACCESS_ID = ''
AWS_ACCESS_KEY = ''

# web


try:
    from local_settings import *  # noqa
except ImportError:
    pass
