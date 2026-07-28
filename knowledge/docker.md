# Docker Troubleshooting Guide

This document contains common Docker issues and troubleshooting steps.

---

## Issue: Container Exited

### Description

A container exits immediately after starting.

### Common Causes

- Application crash
- Missing configuration
- Startup command failure

### Symptoms

- `Exited (1)`
- `Container stopped`

### Recommended Actions

1. Inspect container logs.
2. Verify the startup command.
3. Check application configuration.

### Keywords

docker, exited, container stopped

### References

- https://docs.docker.com/

---

## Issue: Out of Memory (OOMKilled)

### Description

The container exceeded its memory allocation.

### Common Causes

- Memory leak
- Insufficient memory limit
- High workload

### Symptoms

- `OOMKilled`
- `Exit Code 137`

### Recommended Actions

1. Inspect memory usage.
2. Increase memory limit if appropriate.
3. Optimize the application.

### Keywords

docker, oomkilled, exit code 137, out of memory

### References

- https://docs.docker.com/

---

## Issue: Port Already Allocated

### Description

Docker cannot bind to the requested host port.

### Common Causes

- Another process using the port
- Existing container already bound

### Symptoms

- `bind: address already in use`

### Recommended Actions

1. Identify the process using the port.
2. Stop the conflicting process or container.
3. Use a different port if necessary.

### Keywords

docker, address already in use, port conflict

### References

- https://docs.docker.com/