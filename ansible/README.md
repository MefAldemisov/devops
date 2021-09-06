# Ansible-based deployment
1. Create instance with terraform
2. Update the `inventory\hosts` file with new:
- `host` (ip)
- `ansible_user`
- `ansible_host`
3. Create the environment:
```bash
> ansible-playbook ./playbooks/setup.yml
```
4. Go to `{ip}:5000/time/Europe/Moscow` :)