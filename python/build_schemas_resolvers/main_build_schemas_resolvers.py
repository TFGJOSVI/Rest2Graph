from build_schemas_resolvers.read_mutations_config_file import read_mutations_config_file
from build_schemas_resolvers.read_schemas_config_file import read_schemas

if __name__ == '__main__':
    mutations = read_mutations_config_file('../config_file/copies_templates/copy.txt')
    schemas = read_schemas('../config_file/copies_templates/copy.txt')
    for mutation in mutations:
        print(mutation.name)
        print(mutation.url)
        print(mutation.parameters)
        print(mutation.response)
        print()
