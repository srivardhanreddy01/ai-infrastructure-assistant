# MongoDB Troubleshooting Guide

This document contains common MongoDB issues, their causes, and recommended troubleshooting steps.

---

## Issue: MongoDB Connection Refused

### Description
The application cannot establish a connection to the MongoDB server.

### Common Causes

- MongoDB service is not running
- Incorrect hostname or port
- Firewall blocking the connection
- Incorrect connection string
- Docker networking issues

### Symptoms

- `connection refused`
- `ECONNREFUSED`
- `failed to connect to MongoDB`

### Recommended Actions

1. Verify MongoDB is running.
2. Confirm the connection string.
3. Verify port **27017** is open.
4. Check firewall and network configuration.
5. Validate Docker networking if applicable.

### Keywords

mongodb, connection refused, ECONNREFUSED, port 27017, failed to connect

### References

- https://www.mongodb.com/docs/

---

## Issue: MongoDB Error E11000 (Duplicate Key)

### Description

An insert or update violates a unique index.

### Common Causes

- Duplicate `_id`
- Duplicate value in a unique index
- Incorrect upsert logic

### Symptoms

- `E11000 duplicate key`
- `duplicate key error`

### Recommended Actions

1. Check the unique index.
2. Verify incoming data.
3. Remove duplicates if appropriate.
4. Review upsert logic.

### Keywords

mongodb, e11000, duplicate key, unique index

### References

- https://www.mongodb.com/docs/

---

## Issue: MongoDB Authentication Failed

### Description

The client cannot authenticate with the database.

### Common Causes

- Invalid username
- Invalid password
- Incorrect authentication database
- Missing user permissions

### Symptoms

- `Authentication failed`
- `Unauthorized`

### Recommended Actions

1. Verify credentials.
2. Check authentication database.
3. Confirm user permissions.

### Keywords

mongodb, authentication failed, unauthorized, login

### References

- https://www.mongodb.com/docs/