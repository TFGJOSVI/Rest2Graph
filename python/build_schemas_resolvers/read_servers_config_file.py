def read_servers_config_file(file_path):
    servers = []
    with open(file_path, 'r') as file:
        lines = file.read()

        posicion_inicio = lines.find('servers:')
        posicion_fin = lines.find('queries:')

        contenido_deseado = lines[posicion_inicio + len('servers'):posicion_fin]

        for server in contenido_deseado.split('\n')[1:]:
            url = server.split('-')
            if len(url) > 1:
                url = url[1].strip()
                servers.append(url)
        return servers