#!/bin/bash
# A simple script to run repetitive tasks.

test() {
  echo "Running tests"
  python -m pytest
}

testw() {
  echo "Running tests in watch mode"
  ptw
}

changelog() {
  # NOTE: This requires github_changelog_generator to be installed.
  # https://github.com/skywinder/github-changelog-generator

  if [ -z "$NEXT" ]; then
      NEXT="Next"
  fi

  echo "Generating changelog upto version: $NEXT"
  github_changelog_generator --pr-label "**Improvements:**" --issue-line-labels=ALL --future-release="$NEXT"
}

publish() {
  echo "Publishing to PyPi"
  python setup.py sdist upload -r pypi
}

# Run command received from args.
$1
