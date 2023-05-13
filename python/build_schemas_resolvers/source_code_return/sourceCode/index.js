import {ApolloServer} from '@apollo/server';
import {startStandaloneServer} from '@apollo/server/standalone';
import fetch from 'node-fetch';
import gql from 'graphql-tag';

// Base URL

const typeDefs = gql`#graphql

	type Categoria {
		id: Int
		nombre: String
	}

	type Director {
		id: Int
		nombre: String
		apellido: String
		edad: Int
	}

	type Pelicula {
		id: Int
		nombre: String
		descripcion: String
		anyo: Int
		director: Int
		categoria: Int
	}

	input InputCategoria {
		id: Int
		nombre: String
	}

	input InputDirector {
		id: Int
		nombre: String
		apellido: String
		edad: Int
	}

	input InputPelicula {
		id: Int
		nombre: String
		descripcion: String
		anyo: Int
		director: Int
		categoria: Int
	}

  


    
type Query {
		 getDirectores: [Director],

		 getDirectoresById(id: Int!): Director,

		 getCategorias: [Categoria],

		 getCategoriasById(id: Int!): Categoria,

		 getPeliculas: [Pelicula],

		 getPeliculasById(id: Int!): Pelicula,

		 getPeliculasCategoriaById(id: Int!): [Pelicula],

		 getPeliculasDirectorById(id: Int!): [Pelicula],

}

type Mutation {
		 postDirectores(input: InputDirector): Director,

		 putDirectoresById(id: Int!, input: InputDirector): Director,

		 deleteDirectoresById(id: Int!): Director,

		 postCategorias(input: InputCategoria): Categoria,

		 putCategoriasById(id: Int!, input: InputCategoria): Categoria,

		 deleteCategoriasById(id: Int!): Categoria,

		 postPeliculas(input: InputPelicula): Pelicula,

		 putPeliculasById(id: Int!, input: InputPelicula): Pelicula,

		 deletePeliculasById(id: Int!): Pelicula,

		 deletePeliculasByIdCategoriaByCat(id: Int!, cat: Int!): Pelicula,

}

`;

const resolvers = {
    Query: {
	 getDirectores: (root, args) => get(`http://localhost:8000/directores?`),
	 getDirectoresById: (root, args) => get(`http://localhost:8000/directores/${args.id}?`),
	 getCategorias: (root, args) => get(`http://localhost:8000/categorias?`),
	 getCategoriasById: (root, args) => get(`http://localhost:8000/categorias/${args.id}?`),
	 getPeliculas: (root, args) => get(`http://localhost:8000/peliculas?`),
	 getPeliculasById: (root, args) => get(`http://localhost:8000/peliculas/${args.id}?`),
	 getPeliculasCategoriaById: (root, args) => get(`http://localhost:8000/peliculas/categoria/${args.id}?`),
	 getPeliculasDirectorById: (root, args) => get(`http://localhost:8000/peliculas/director/${args.id}?`),

    },
    Mutation: {
	 postDirectores: (root, args) => post(`http://localhost:8000/directores?`,args),
	 putDirectoresById: (root, args) => put(`http://localhost:8000/directores/${args.id}?`,args),
	 deleteDirectoresById: (root, args) => deleteData(`http://localhost:8000/directores/${args.id}?`,args),
	 postCategorias: (root, args) => post(`http://localhost:8000/categorias?`,args),
	 putCategoriasById: (root, args) => put(`http://localhost:8000/categorias/${args.id}?`,args),
	 deleteCategoriasById: (root, args) => deleteData(`http://localhost:8000/categorias/${args.id}?`,args),
	 postPeliculas: (root, args) => post(`http://localhost:8000/peliculas?`,args),
	 putPeliculasById: (root, args) => put(`http://localhost:8000/peliculas/${args.id}?`,args),
	 deletePeliculasById: (root, args) => deleteData(`http://localhost:8000/peliculas/${args.id}?`,args),
	 deletePeliculasByIdCategoriaByCat: (root, args) => deleteData(`http://localhost:8000/peliculas/${args.id}/categoria/${args.cat}? +'&'+`,args),

    }
};


async function get(url) {

    let result;

    await fetch(url, {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => {
            result = data;
        });



    return result;

}



async function post(url, data) {

    let result;

    await fetch(url, {
        method: 'POST',
        body: JSON.stringify(data.input) ? data.input : '',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            result = data;
        });

    return result;

}

// async function put(url, data) {
//
//     let result;
//
//     await fetch(url, {
//         method: 'PUT',
//         body: JSON.stringify(data.input) ? data.input : '',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//     })
//         .then(response => response.json())
//         .then(data => {
//             result = data;
//         });
//
//     return result;
//
// }

async function put(url, data) {

    let result;

    await fetch(url, {
        method: 'PUT',
        body: JSON.stringify(data.input) ? data.input : '',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            result = data;
        });

    return result;

}

async function deleteData(url, args) {

    let result;

    await fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => response.json())
        .then(data => {
            result = data;
        });

    return result;

}


const server = new ApolloServer({
    typeDefs, resolvers,
});

const {url} = await startStandaloneServer(server, {
    listen: {port: 4000},
});

console.log(`🚀  Server ready at: ${url}`);