# Logging
## Logging with Grafana

### Process

### Results
#### Grafana + Loki:
![Grafana dashboard with logs](./media/loki__grafana.png)
#### Requirements:
- docker plugin to log with loki:
```bash
>  docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```
### Grafana + Loki + Promtail (lab 7)
![Grafana dashboard with logs](./media/loki__grafana__promtail.png)
![Grafana dashboard with logs](./media/loki.png)

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

## Logging with Prometheus
### Output:
http://localhost:9090/targets.
![The loki and prometheus targets are up](./media/prometheus_start.png)
### Some examples from "status" part
![](./media/status1.png)
![](./media/status2.png)
## References
- [Loki label best practices](https://grafana.com/docs/loki/latest/best-practices/)