# Docker best practices
## Practices, common for any type of files

1. Use comments
   
2. Reduce the size of a line. For example, use `/\` for complex `RUN` statements

3. Use Dockerfile liners.
- This [linter](https://www.dockerfilelint.com/#/) is used in this project

4. Show, who is responsible for maintenance with `MAINTAINER` instruction

## Reduce the size of the build context 

It is necessary to speed up the building process.

1. Locate the Dockerfile in a proper directory

Example (for Dockerfile in this repo):

| Location of the `Dockerfile` | The size of the build context |
|------------------------------|-------------------------------|
| `devops/`                    | 949B                          |
| `devops/app_python`          | 467B                          |

It means that the build context reduced twice with relocation.

2. Use `.dockerignire`

If we ignore the `*.md` files and `__pycache__`, the build context size will be reduced as follows:

| `.dockerignore` | The size of the build context |
|-----------------|-------------------------------|
| Not used        | 467B                          |
| Used            | 328B                          |

3. From official [documentation](https://docs.docker.com/engine/reference/builder/#usage)
> In most cases, it’s best to start with an empty directory as context and keep your Dockerfile in that directory. 
> Add only the files needed for building the Dockerfile.

## Reduce the size of the actual container

1. Install only required libs
   - the lib size for python pip may be reduced with `--no-cache-dir` prefix. 
     It removes the source and installation files of the libraries
2. Copy only required files
3. Use horizontal scaling instead of vertical for a large app
4. Reduce the number of "layers" (`COPY`, `RUN` and `ADD` statements)
- use pipelines for `RUN` statements
5. Use small base images
   - e.g. `python:v-alpine` versions
6. Use `VOLUME` to connect the local version of the big file to the container. 
   It may be also useful for files, which should be updated (foe instance, during debugging process)

## Use instructions properly

1. Remember tie difference between 
   [`RUN` and `CMD`](https://stackoverflow.com/questions/37461868/difference-between-run-and-cmd-in-a-dockerfile)
2. Remember tie difference between 
   [`ADD` and `COPY`](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy)

## Special practices
1. Use `docker-compose` to prevent constant repetition of `docker build` and `docker run` during testing
2. The commands should be sorted in ascending of change probability 
   (e.g. the `COPY` should be located below the `requirement.txt` installation)
   
3. Use tags for versioning
> To tag the image into multiple repositories after the build, add multiple -t parameters when you run the build command: