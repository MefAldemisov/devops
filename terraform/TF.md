# Terraform best practices
1. Format and check the `.tf` files with `terraform fix` and `terraform validate` commands
2. Always destroy the created instances
3. Always set up a shared state location.
4. Use separate state locations based on logical environment boundaries.
5. Decompose and abstract your terraform code to maximize reuse.
6. Be wary of programmatically generating resource names.
7. Keep your modules, and your environment implementation code separate.
8. Maintain a strict policy of reviewing terraform validate and plan outputs before allowing terraform changes to be applied to an environment.
9. Use an automated testing framework to write unit and functional tests that validate your terraform modules.
10. Require a uniform authentication scheme and auditing mechanism that clearly tracks which principal triggered a terraform operation, particularly in production environments.
11. Use a Continuous Delivery / Continuous Integration or shared orchestration tool to execute your terraform operations from a single common location.
12. Consider using a separate abstraction layer to facilitate reuse and abstraction.
13. Don’t commit the `.tfstate` file
14. Back up your state files
15. Keep your backends small

Resources:
- [Top Ten Best Practices for Terraform Implementations](https://www.xtivia.com/blog/cloud/terraform-best-practices/)
- [10 TERRAFORM BEST PRACTICES: FOR SECURE & FAST INFRASTRUCTURE.](https://openupthecloud.com/terraform-best-practices/)