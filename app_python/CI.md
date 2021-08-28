# CI

## GitHub actions Best practices
1. Make actions small to run them in parallel
2. Use space carefully (as for the Docker)
3. Use Git Hub secrets
4. Make environment (`env`) scope minimal
5. Specify permissions
6. Test the CI/CD before pushing 
   (for instance, use the [act](https://yonatankra.com/how-to-test-github-actions-locally-using-act/) 
   tool for Git Hub actions)
7. Use the actions from the marketplace
8. Use caching ([example](https://docs.docker.com/language/python/configure-ci-cd/#optimizing-the-workflow))

## Jenkins best practices

1. Security
- don't build on master
- manage passwords and secrets properly
2. Usage:
- make the project name simple to make it executable and readable in different configurations
- use the "file fingerprinting" to manage versions
- archive the unused jobs before removing
- prevent resource collision for parallel jobs
- avoid scheduled jobs run at the same time (use resources properly)
3. General
- backup
- generate reports
- lint the jenkins with some issue-tracking system
- use tagging/labeling of successful builds


## References

1. [GitHub Actions Best Practices](https://www.datree.io/resources/github-actions-best-practices)
2. [5 GitHub Actions CI/CD Best Practices](https://cloud.netapp.com/blog/cvo-blg-5-github-actions-cicd-best-practices)
3. [Jenkins Best Practices](https://wiki.jenkins.io/display/JENKINS/Jenkins+Best+Practices)