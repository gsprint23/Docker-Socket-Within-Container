import docker # https://docker-py.readthedocs.io/en/stable/

# need to mount volume for /var/run/docker.sock:/var/run/docker.sock
# in docker-compose.yml to have access to the docker socket
client = docker.from_env()

# https://docker-py.readthedocs.io/en/stable/containers.html
for container in client.containers.list():
    print("\n\n", container.name, container.status, container.ports)
    stats_dict = container.stats(stream=False)
    for key, value in stats_dict.items():
        print(key, ":", value)
print("\n\n")

# https://docker-py.readthedocs.io/en/stable/networks.html
for network in client.networks.list():
    print("\n\n", network.name, network.containers)
print("\n\n")