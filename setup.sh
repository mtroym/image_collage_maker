echo "rm -rf old dist"
rm -rf dist
echo "run: python3 setup.py sdist bdist_wheel"
python3 setup.py sdist bdist_wheel
twine upload dist/*
echo "run: upload!"