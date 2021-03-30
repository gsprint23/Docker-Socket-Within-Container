import docker # https://docker-py.readthedocs.io/en/stable/

# need to mount volume for /var/run/docker.sock:/var/run/docker.sock
# in docker-compose.yml to have access to the docker socket
client = docker.from_env()
outfile = open("temp.txt", "w")

# https://docker-py.readthedocs.io/en/stable/containers.html
for container in client.containers.list():
    outfile.write("\n" + str(container.name) + "\n")
    outfile.write(str(container.status) + "\n")
    outfile.write(str(container.ports) + "\n")
    stats_dict = container.stats(stream=False)
    for key, value in stats_dict.items():
        outfile.write(str(key) + ":" + str(value) + "\n")
    outfile.write("top: " + str(container.top()) + "\n")
outfile.write("\n")

# https://docker-py.readthedocs.io/en/stable/networks.html
for network in client.networks.list():
    outfile.write("\n" + str(network.name) + " " + str(network.containers))
outfile.close()