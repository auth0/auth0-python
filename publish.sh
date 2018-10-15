# Deploy to https://pypi.org/project/auth0-python/
# Requires a ~/.pypirc file in the developer machine with proper credentials

#!/usr/bin/env bash
docker build -t auth0-python-sdk-publish .
docker run -it auth0-python-sdk-publish
