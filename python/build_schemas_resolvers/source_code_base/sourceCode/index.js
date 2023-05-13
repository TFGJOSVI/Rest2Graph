import {ApolloServer} from '@apollo/server';
import {startStandaloneServer} from '@apollo/server/standalone';
import fetch from 'node-fetch';
import gql from 'graphql-tag';

// Base URL

const typeDefs = gql`#graphql

/* TYPES */  

/* ex - TYPES */  
    
/* Queries */

/* Mutations */

`;

const resolvers = {
    Query: {
/* Resolvers Queries */
    },
    Mutation: {
/* Resolvers Mutations */
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