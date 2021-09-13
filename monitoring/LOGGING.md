# Logging
## Logging with Grafana

### Process
#### Requirements:
- docker plugin to log with loki:
```bash
>  docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```
### Results
#### Grafana + Loki (lab 7):
![Grafana dashboard with logs](./media/lab-7__query.png)

### Best practices
    
#### Loki
- Both static and dynamic labels should be used
- The values of dynamic labels should have some limits
- Use caching
- The time order should be increasing (thus, the time zone of the servers can make some impact)
- Limit the size of a chunk with `chunk_target_size`

#### Dashboards
- Don't produce many similar dashboards
- Reuse the dashboards with cross-referencing dashboards
- The dashboard should have some exact purpouse or answer some exact question
## References
- [Loki label best practices](https://grafana.com/docs/loki/latest/best-practices/)