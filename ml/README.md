# Machine Learning

## windows

1. Install Python
2. Install [Scikit-learn](https://scikit-learn.org/stable/install.html)
    1. `pip install -U scikit-learn`
    2. check
       ```shell
       python -m pip show scikit-learn  # to see which version and where scikit-learn is installed
       python -m pip freeze  # to see all packages installed in the active virtualenv
       python -c "import sklearn; sklearn.show_versions()"
       ```
3. Install [Jupyter Notebook](https://pypi.org/project/jupyter/)
    1. `pip install jupyter`

## FAQ

```
Could not find platform independent libraries <prefix>
Could not find platform dependent libraries <exec_prefix>
Consider setting $PYTHONHOME to <prefix>[:<exec_prefix>]
```

edit environment

- user, `Path`, add `C:\your_path\Python\Python39\Scripts\` and `C:\your_path\Python\Python39\`
- sys, `Path`, add `C:\your_path\Python\Python39\Scripts\` and `C:\your_path\Python\Python39\`
