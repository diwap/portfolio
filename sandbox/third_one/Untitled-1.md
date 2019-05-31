# To get list of packages installed and generate files

```bash
pip freeze > requirements.txt
```  
where freeze is the command to get installed packages  
\> is for direccting list into next argument
requirements.txt is the file where we save list of installed packages


# To install packages from stored file

```bash
pip install -r requirements.txt
```

where install is simply a command to install any packages  
-r is for getting recursive requirement from file  
requirements.txt is the name of the file where packages name and version are stored.