# This role is based on the following [repo](https://github.com/geerlingguy/ansible-role-docker)
## Modifications:
- renaming of the files to clarify the structure
- removed `shell` and `command` modules
- added `become: yes` (`sudo`), when needed