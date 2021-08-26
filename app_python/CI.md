# GitHub actions

## Best practices
1. Make actions small to run them in parallel
2. Use space carefully (as for the Docker)
3. Use Git Hub secrets
4. Make environment (`env`) scope minimal
5. Specify permissions
6. Test the CI/CD before pushing 
   (for instance, use the [act](https://yonatankra.com/how-to-test-github-actions-locally-using-act/) 
   tool for Git Hub actions)
7. Use the actions from the marketplace

## References

1. [GitHub Actions Best Practices](https://www.datree.io/resources/github-actions-best-practices)
2. [5 GitHub Actions CI/CD Best Practices](https://cloud.netapp.com/blog/cvo-blg-5-github-actions-cicd-best-practices)
