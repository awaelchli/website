import os

# SECURITY WARNING: don't run with debug turned on in production!
DJANGO_SERVER_TYPE = os.environ.get("DJANGO_SERVER_TYPE", "production")

if DJANGO_SERVER_TYPE == "production":
    from .prod import *
elif DJANGO_SERVER_TYPE == "development":
    from .dev import *
else:
    raise ImportError(
        """
        Could not read server type from environment variable DJANGO_SERVER_TYPE: 
        value must be one of ["production", "development"]. 
        """
    )
