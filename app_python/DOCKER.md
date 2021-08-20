# Docker best practices
## Practices, common for any type of files

1. Use comments
2. Reduce the size of a line e.g. using `/\` for complex `RUN` statements

## Reduce the size of the build context 

It is necessary to speed up the building process.

1. Locate the Dockerfile in a proper directory

Example (for Dockerfile in this repo):

| Location of the `Dockerfile` | The size of the build context |
|------------------------------|-------------------------------|
| `devops/`                    | 949B                          |
| `devops/app_python`          | 467B                          |

It means that the build context was reduced twice with relocation.

2. Use `.dockerignire`

If we ignore the `*.md` files and `__pycache__`, the build context size will be reduced as follows:

| `.dockerignore` | The size of the build context |
|-----------------|-------------------------------|
| Not used        | 467B                          |
| Used            | 328B                          |

## Reduce the size of the actual container

1. Install only required libs
2. Copy only required files
3. Use horizontal scaling instead of vertical for a large app
4. Reduce the number of "layers" (`COPY`, `RUN` and `ADD` statements)
- use pipelines for `RUN` statements
5. Use small base images

## Use instructions properly
1. Remember tie difference between [`RUN` and `CMD`](https://stackoverflow.com/questions/37461868/difference-between-run-and-cmd-in-a-dockerfile)
2. Remember tie difference between [`ADD` and `COPY`](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy)