#!/bin/bash
echo -e "Install test tools"
pip install -r requirements.txt
echo -e "Install pre-commit module ........"
pip install pre-commit
echo -e "Test pre-commit Start ............."
pre-commit run --all-files
echo -e "Test pre-commit finished ...."
echo -e "Thanks for using my tool :)"
