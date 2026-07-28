1. Exit Code 137 (OOM Killed)

Description: The container stops abruptly because it used more memory than allowed.
 
Cause: The host or container ran out of memory, often due to missing memory limits or a memory leak in the application.
 
Resolution: Increase the memory limit using the -m flag (e.g., docker run -m 512m) or optimize app memory usage.

Reference: Docker Error Codes Reference https://github.com/moby/moby/issues/49097
 

2. Invalid Reference Format

Description: Docker fails to parse an image name or tag provided in the command line.
 
Cause: Using uppercase letters in repository names, or having unintended whitespace or syntax errors.

Resolution: Ensure all characters in the repository name are lowercase and remove trailing spaces or typos.

Reference: ⁠Stack Overflow Discussion https://stackoverflow.com/questions/48522615/docker-error-invalid-reference-format-repository-name-must-be-lowercase

3. Cannot Connect to the Docker Daemon

Description: The Docker client cannot talk to the background service that runs containers.
 
Cause: The Docker daemon service is not running or the current user lacks socket permissions.
 
Resolution: Start the service using sudo systemctl start docker and add your user to the docker group.
 
Reference: ⁠Troubleshooting Common Docker Errors Video https://www.youtube.com/watch?v=nH5wrKsznjg

4. Temporary Failure in Name Resolution (DNS)

Description: Containers cannot reach external sites, packages, or other host addresses.

Cause: Misconfigured host DNS settings, blocked firewall rules, or disabled IP forwarding.

Resolution: Specify a working external DNS server (like 8.8.8.8) in /etc/docker/daemon.json and restart the service.

Reference: ⁠Stack Overflow Network Fix https://stackoverflow.com/questions/44761246/temporary-failure-in-name-resolution-errno-3-with-docker




