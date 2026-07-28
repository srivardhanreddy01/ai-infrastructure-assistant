# Kubernetes Troubleshooting Guide

This document contains common Kubernetes issues and troubleshooting steps.

---

## Issue: CrashLoopBackOff

### Description

A container repeatedly starts and crashes.

### Common Causes

- Application crash
- Missing configuration
- Invalid environment variables
- Dependency unavailable

### Symptoms

- `CrashLoopBackOff`
- `Back-off restarting failed container`

### Recommended Actions

1. Inspect pod logs.
2. Describe the pod.
3. Verify environment variables.
4. Confirm dependencies are available.

### Keywords

kubernetes, crashloopbackoff, pod restart, container restart

### References

- https://kubernetes.io/docs/

---

## Issue: ImagePullBackOff

### Description

Kubernetes cannot pull the requested container image.

### Common Causes

- Invalid image name
- Missing image tag
- Registry authentication failure
- Image does not exist

### Symptoms

- `ImagePullBackOff`
- `ErrImagePull`

### Recommended Actions

1. Verify image name.
2. Check registry credentials.
3. Confirm the image exists.
4. Verify image tag.

### Keywords

kubernetes, imagepullbackoff, errimagepull, docker image

### References

- https://kubernetes.io/docs/

---

## Issue: Pending Pod

### Description

A pod remains in the Pending state and is never scheduled.

### Common Causes

- Insufficient resources
- Node selector mismatch
- Taints and tolerations
- Persistent volume unavailable

### Symptoms

- `Pending`

### Recommended Actions

1. Describe the pod.
2. Check scheduler events.
3. Verify node capacity.
4. Validate storage availability.

### Keywords

kubernetes, pending pod, scheduler, node resources

### References

- https://kubernetes.io/docs/