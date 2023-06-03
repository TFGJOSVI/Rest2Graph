import {ApolloServer} from '@apollo/server';
import {startStandaloneServer} from '@apollo/server/standalone';
import fetch from 'node-fetch';
import gql from 'graphql-tag';

// Base URL

const typeDefs = gql`#graphql

	type User {
		id: Int
		username: String
		firstName: String
		lastName: String
		email: String
		password: String
		phone: String
		userStatus: Int
	}

	type Pet {
		id: Int
		name: String!
		category: Category
		photoUrls: [String]!
		tags: [Tag]
		status: String
	}

	type Order {
		id: Int
		petId: Int
		quantity: Int
		shipDate: String
		status: String
		complete: Boolean
	}

	type ApiResponse {
		code: Int
		type: String
		message: String
	}

	type ObjectObject {
		additionalProperties: Int
	}

	input InputOrder {
		id: Int
		petId: Int
		quantity: Int
		shipDate: String
		status: String
		complete: Boolean
	}

	input InputUser {
		id: Int
		username: String
		firstName: String
		lastName: String
		email: String
		password: String
		phone: String
		userStatus: Int
	}

	input InputPet {
		id: Int
		name: String!
		category: InputCategory
		photoUrls: [String]!
		tags: [InputTag]
		status: String
	}

  

	type Pet {
		id: Int
		name: String!
		category: InputCategory
		photoUrls: [String]!
		tags: [InputTag]
		status: String
	}

	type Tag {
		id: Int
		name: String
	}

	input InputPet {
		id: Int
		name: String!
		category: InputInputCategory
		photoUrls: [String]!
		tags: [InputInputTag]
		status: String
	}

	input InputTag {
		id: Int
		name: String
	}

  
    
type Query {
		 findPetsByStatus(status: String): [Pet],

		 findPetsByTags(tags: [String]): [Pet],

		 getPetById(petId: Int!): Pet,

		 getInventory: ObjectObject,

		 getOrderById(orderId: Int!): Order,

		 loginUser(username: String, password: String): String,

		 logoutUser: String,

		 getUserByName(username: String!): User,

}

type Mutation {
		 updatePet(input: InputPet): Pet,

		 addPet(input: InputPet): Pet,

		 updatePetWithForm(petId: Int!, name: String, status: String): String,

		 deletePet(api_key: String, petId: Int!): String,

		 uploadFile(petId: Int!, additionalMetadata: String, input: InputString): ApiResponse,

		 placeOrder(input: InputOrder): Order,

		 deleteOrder(orderId: Int!): String,

		 createUser(input: InputUser): User,

		 createUsersWithListInput(input: [InputUser]): User,

		 updateUser(username: String!, input: InputUser): String,

		 deleteUser(username: String!): String,

}

`;

const resolvers = {
    Query: {
	 findPetsByStatus: (root, args) => get(`https://petstore3.swagger.io/api/v3/pet/findByStatus?${'status='+ args.status ? args.status : ''}`),
	 findPetsByTags: (root, args) => get(`https://petstore3.swagger.io/api/v3/pet/findByTags?${'tags='+ args.tags ? args.tags : ''}`),
	 getPetById: (root, args) => get(`https://petstore3.swagger.io/api/v3/pet/${args.petId}?`),
	 getInventory: (root, args) => get(`https://petstore3.swagger.io/api/v3/store/inventory?`),
	 getOrderById: (root, args) => get(`https://petstore3.swagger.io/api/v3/store/order/${args.orderId}?`),
	 loginUser: (root, args) => get(`https://petstore3.swagger.io/api/v3/user/login?${'username='+ args.username ? args.username : ''} +'&'+${'password='+ args.password ? args.password : ''}`),
	 logoutUser: (root, args) => get(`https://petstore3.swagger.io/api/v3/user/logout?`),
	 getUserByName: (root, args) => get(`https://petstore3.swagger.io/api/v3/user/${args.username}?`),

    },
    Mutation: {
	 updatePet: (root, args) => put(`https://petstore3.swagger.io/api/v3/pet?`,args),
	 addPet: (root, args) => post(`https://petstore3.swagger.io/api/v3/pet?`,args),
	 updatePetWithForm: (root, args) => post(`https://petstore3.swagger.io/api/v3/pet/${args.petId}? +'&'+${'name='+ args.name ? args.name : ''} +'&'+${'status='+ args.status ? args.status : ''}`,args),
	 deletePet: (root, args) => deleteData(`https://petstore3.swagger.io/api/v3/pet/${args.petId}? +'&'+`,args),
	 uploadFile: (root, args) => post(`https://petstore3.swagger.io/api/v3/pet/${args.petId}/uploadImage? +'&'+${'additionalMetadata='+ args.additionalMetadata ? args.additionalMetadata : ''}`,args),
	 placeOrder: (root, args) => post(`https://petstore3.swagger.io/api/v3/store/order?`,args),
	 deleteOrder: (root, args) => deleteData(`https://petstore3.swagger.io/api/v3/store/order/${args.orderId}?`,args),
	 createUser: (root, args) => post(`https://petstore3.swagger.io/api/v3/user?`,args),
	 createUsersWithListInput: (root, args) => post(`https://petstore3.swagger.io/api/v3/user/createWithList?`,args),
	 updateUser: (root, args) => put(`https://petstore3.swagger.io/api/v3/user/${args.username}?`,args),
	 deleteUser: (root, args) => deleteData(`https://petstore3.swagger.io/api/v3/user/${args.username}?`,args),

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