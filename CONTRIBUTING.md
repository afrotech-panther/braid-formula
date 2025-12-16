## Releasing a New Version

1. Update version in `pyproject.toml` and `__init__.py`
2. Update CHANGELOG.md
3. Commit: `git commit -am "Release vX.Y.Z"`
4. Tag: `git tag vX.Y.Z`
5. Build: `python -m build`
6. Upload: `python -m twine upload dist/*`
7. Push: `git push && git push --tags`