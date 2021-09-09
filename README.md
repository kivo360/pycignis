# PyCignus


<p align="center">
<a href="https://pypi.python.org/pypi/pycignus">
    <img src="https://img.shields.io/pypi/v/pycignus.svg"
        alt = "Release Status">
</a>

<a href="https://github.com/kivo360/pycignus/actions">
    <img src="https://github.com/kivo360/pycignus/actions/workflows/main.yml/badge.svg?branch=release" alt="CI Status">
</a>

<a href="https://pycignus.readthedocs.io/en/latest/?badge=latest">
    <img src="https://readthedocs.org/projects/pycignus/badge/?version=latest" alt="Documentation Status">
</a>

</p>


PyCignus is an open-source, end-to-end information retrieval framework that allows users to easily build and deploy natural language search applications. It includes a Natural Language Search Engine (NLS) for indexing documents and searching them using natural queries.

Using PyCignus, developers can quickly scaffold projects with the use of built-in libraries, including SQLAlchemy support for database interactions. The framework also supports Transformers which allow users to create custom processors that work directly with the NLS.

* Free software: MIT
* Documentation: <https://pycignus.readthedocs.io>


## Features

* Automatically index documents by extracting information from the words in text.
* Save time, effort, and money spent on manually creating an index.
* Create natural language search applications for specific industries or topics of interest.
* Easily build NLS indexes to suit specific domain using open-source framework.



# Images

> [inboard](https://inboard.bws.bio/docker) containers are used for the web piece.

TO run the image, either for development or for production you can run the following commands:

Build:

```bash
cd /path/to/repo
docker build . -t imagename:latest
```


```bash
cd /path/to/repo
docker run -d -p 80:80 \
  -e "LOG_LEVEL=debug" -e "PROCESS_MANAGER=uvicorn" -e "WITH_RELOAD=true" \
  -v $(pwd)/package:/app/package imagename
```

These are the details of the docker container images:

Details on the docker run command:

`-e "PROCESS_MANAGER=uvicorn" -e "WITH_RELOAD=true"` will instruct `start.py` to run Uvicorn with reloading and without Gunicorn. The Gunicorn configuration won't apply, but these environment variables will still work as described:
APP_MODULE
HOST
PORT
LOG_COLORS
LOG_FORMAT
LOG_LEVEL
RELOAD_DIRS
WITH_RELOAD
`-v $(pwd)/package:/app/package:` the specified directory (`/path/to/repo/package` in this example) will be [mounted as a volume](https://docs.docker.com/engine/reference/run/#volume-shared-filesystems) inside of the container at `/app/package`. When files in the working directory change, Docker and Uvicorn will sync the files to the running Docker container.




## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [zillionare/cookiecutter-pypackage](https://github.com/zillionare/cookiecutter-pypackage) project template.
