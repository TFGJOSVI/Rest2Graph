def read_servers_config_file(file_path: str) -> list[str]:

    """
    Read the servers config file and return a list of servers.

    :param file_path:
        The path of the config file.
    :return:
        A list of servers.
    """

    servers = []
    with open(file_path, 'r') as file:
        lines = file.read()

        posicion_inicio = lines.find('servers:')
        posicion_fin = lines.find('queries:')

        contenido_deseado = lines[posicion_inicio + len('servers'):posicion_fin]

        for server in contenido_deseado.split('\n')[1:]:
            url = server.split('\t-')
            if len(url) > 1:
                url = url[1].strip()
                servers.append(url)
        return servers