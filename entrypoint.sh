#!/bin/bash

TEST_PATH=$1

python -m pytest $TEST_PATH > $HOME/black.patch

# If pytest terminated with a nonzero exit code, fail the GitHub workflow job
# using the special '::error' directive
# https://docs.github.com/en/actions/reference/workflow-commands-for-github-actions#setting-an-error-message
if [ $? -ne 0 ]
then
    echo '::error::Tests failed. Refer to the "Checks" tab for details.'
fi
