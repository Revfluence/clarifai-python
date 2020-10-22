#!/bin/bash

FIND_SOURCE_FILES='find clarifai tests -name "*.py" -not -path "clarifai/rest/grpc/proto/*"'

function run_autoflake {
  echo "- autoflake: Make sure there are no unused imports and unused variables"
  FIND_SOURCE_FILES_FOR_AUTOFLAKE="${FIND_SOURCE_FILES} -not -iwholename '*/__init__.py'"
  autoflake --remove-all-unused-imports --remove-unused-variables \
          $(eval ${FIND_SOURCE_FILES_FOR_AUTOFLAKE}) \
          | tee autoflake-output.tmp

  if [ $(cat autoflake-output.tmp | wc -c) != 0 ]; then
    echo ""
    echo "  Here are affected files: "
    grep "+++" autoflake-output.tmp
    rm autoflake-output.tmp
    echo "  autoflake failed"
    exit 1
  fi

  rm autoflake-output.tmp
  echo "  Done autoflake"
}

function run_isort() {
  echo ""
  echo "- isort: Make sure all imports are sorted"

  if [ "$1" == "isort" ]; then
    isort -sp .isort.cfg -ws $(eval ${FIND_SOURCE_FILES})
  fi
  # This ignores whitespace which is crucial because yapf defines the formatting.
  isort -sp .isort.cfg -ws --diff -c $(eval ${FIND_SOURCE_FILES})

  if [ $? != 0 ]; then
    echo ""
    echo "  isort failed. Run './assert-code-quality.sh isort' to automatically sort the imports correctly."
    echo "    Note: The import code style itself (besides the order) must still comply to yapf"
    exit 1
  fi

  echo "  Done isort"
}

function run_yapf {
  echo ""
  echo "- yapf: Make sure there are no code style issues"

  if [ "$1" == "yapf" ]; then
    yapf --style=.style.yapf -p -i $(eval ${FIND_SOURCE_FILES})
  fi
  yapf --style=.style.yapf -p -d $(eval ${FIND_SOURCE_FILES})

  if [ $? != 0 ]; then
    echo ""
    echo "  yapf failed. Run './assert-code-quality.sh yapf' to automatically apply yapf rules."
    exit 1
  fi
}


echo "START assert-code-quality.sh"

run_autoflake
run_isort "$1"
run_yapf "$1"

echo "  Done yapf"
echo "SUCCESSFUL FINISH OF assert-code-quality.sh"
