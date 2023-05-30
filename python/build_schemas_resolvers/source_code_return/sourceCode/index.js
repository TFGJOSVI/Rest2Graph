import {ApolloServer} from '@apollo/server';
import {startStandaloneServer} from '@apollo/server/standalone';
import fetch from 'node-fetch';
import gql from 'graphql-tag';

// Base URL

const typeDefs = gql`#graphql

	type BalanceSweepConfigurationsResponse {
		hasNext: Boolean!
		hasPrevious: Boolean!
		sweeps: [SweepConfigurationV2]!
	}

	type PaymentInstrument {
		balanceAccountId: String!
		bankAccount: BankAccount
		card: Card
		description: String
		id: String!
		issuingCountryCode: String!
		paymentInstrumentGroupId: String
		reference: String
		status: String
		statusReason: String
		type: String!
	}

	type PaginatedAccountHoldersResponse {
		accountHolders: [AccountHolder]!
		hasNext: Boolean!
		hasPrevious: Boolean!
	}

	type SweepConfigurationV2 {
		counterparty: SweepCounterparty!
		currency: String!
		description: String
		id: String!
		status: String
		sweepAmount: Amount
		targetAmount: Amount
		triggerAmount: Amount
		type: String
	}

	type TransactionRule {
		aggregationLevel: String
		description: String!
		endDate: String
		entityKey: TransactionRuleEntityKey!
		id: String
		interval: TransactionRuleInterval!
		outcomeType: String
		reference: String!
		ruleRestrictions: TransactionRuleRestrictions!
		score: Int
		startDate: String
		status: String
		type: String!
	}

	type PaymentInstrumentGroup {
		balancePlatform: String!
		description: String
		id: String
		properties: object
		reference: String
		txVariant: String!
	}

	type BalanceAccount {
		accountHolderId: String!
		balances: [Balance]
		defaultCurrencyCode: String
		description: String
		id: String!
		reference: String
		status: String
		timeZone: String
	}

	type TransactionRuleResponse {
		transactionRule: TransactionRule
	}

	type AccountHolder {
		balancePlatform: String
		capabilities: object
		contactDetails: ContactDetails
		description: String
		id: String!
		legalEntityId: String!
		primaryBalanceAccount: String
		reference: String
		status: String
		timeZone: String
	}

	type TransactionRulesResponse {
		transactionRules: [TransactionRule]
	}

	type PaginatedBalanceAccountsResponse {
		balanceAccounts: [BalanceAccount]!
		hasNext: Boolean!
		hasPrevious: Boolean!
	}

	type BalancePlatform {
		description: String
		id: String!
		status: String
	}

	type PaginatedPaymentInstrumentsResponse {
		hasNext: Boolean!
		hasPrevious: Boolean!
		paymentInstruments: [PaymentInstrument]!
	}

	input InputTransactionRuleInfo {
		aggregationLevel: String
		description: String!
		endDate: String
		entityKey: InputInputTransactionRuleEntityKey!
		interval: InputInputTransactionRuleInterval!
		outcomeType: String
		reference: String!
		ruleRestrictions: InputInputTransactionRuleRestrictions!
		score: Int
		startDate: String
		status: String
		type: String!
	}

	input InputSweepConfigurationV2 {
		counterparty: InputSweepCounterparty!
		currency: String!
		description: String
		id: String!
		status: String
		sweepAmount: InputAmount
		targetAmount: InputAmount
		triggerAmount: InputAmount
		type: String
	}

	input InputPaymentInstrumentInfo {
		balanceAccountId: String!
		card: InputInputCardInfo
		description: String
		issuingCountryCode: String!
		paymentInstrumentGroupId: String
		reference: String
		status: String
		statusReason: String
		type: String!
	}

	input InputBalanceAccountInfo {
		accountHolderId: String!
		defaultCurrencyCode: String
		description: String
		reference: String
		timeZone: String
	}

	input InputAccountHolderInfo {
		balancePlatform: String
		capabilities: InputInputobject
		contactDetails: InputInputContactDetails
		description: String
		legalEntityId: String!
		reference: String
		timeZone: String
	}

	input InputPaymentInstrumentGroupInfo {
		balancePlatform: String!
		description: String
		properties: InputInputobject
		reference: String
		txVariant: String!
	}

  

	type SweepConfigurationV2 {
		counterparty: InputSweepCounterparty!
		currency: String!
		description: String
		id: String!
		status: String
		sweepAmount: InputAmount
		targetAmount: InputAmount
		triggerAmount: InputAmount
		type: String
	}

	type SweepCounterparty {
		balanceAccountId: String
		merchantAccount: String
		transferInstrumentId: String
	}

	type Amount {
		currency: String!
		value: Int!
	}

	type Balance {
		available: Int!
		balance: Int!
		currency: String!
		reserved: Int!
	}

	type TransactionRuleInterval {
		dayOfMonth: Int
		dayOfWeek: String
		duration: Duration
		timeOfDay: String
		timeZone: String
		type: String!
	}

	type TransactionRuleEntityKey {
		entityReference: String
		entityType: String
	}

	type TransactionRuleRestrictions {
		activeNetworkTokens: ActiveNetworkTokensRestriction
		brandVariants: BrandVariantsRestriction
		countries: CountriesRestriction
		differentCurrencies: DifferentCurrenciesRestriction
		entryModes: EntryModesRestriction
		internationalTransaction: InternationalTransactionRestriction
		matchingTransactions: MatchingTransactionsRestriction
		mccs: MccsRestriction
		merchants: MerchantsRestriction
		processingTypes: ProcessingTypesRestriction
		timeOfDay: TimeOfDayRestriction
		totalAmount: TotalAmountRestriction
	}

	type ContactDetails {
		address: Address!
		email: String!
		phone: Phone!
		webAddress: String
	}

	type BankAccount {
		iban: String!
	}

	type Card {
		authentication: Authentication
		bin: String
		brand: String!
		brandVariant: String!
		cardholderName: String!
		configuration: CardConfiguration
		cvc: String
		deliveryContact: DeliveryContact
		expiration: Expiry
		formFactor: String!
		lastFour: String
		number: String!
	}

	type CardInfo {
		authentication: Authentication
		brand: String!
		brandVariant: String!
		cardholderName: String!
		configuration: CardConfiguration
		deliveryContact: DeliveryContact
		formFactor: String!
	}

	type Balance {
		available: Int!
		balance: Int!
		currency: String!
		reserved: Int!
	}

	type ContactDetails {
		address: Address!
		email: String!
		phone: Phone!
		webAddress: String
	}

	type BankAccount {
		iban: String!
	}

	type Card {
		authentication: Authentication
		bin: String
		brand: String!
		brandVariant: String!
		cardholderName: String!
		configuration: CardConfiguration
		cvc: String
		deliveryContact: DeliveryContact
		expiration: Expiry
		formFactor: String!
		lastFour: String
		number: String!
	}

	type TransactionRuleEntityKey {
		entityReference: String
		entityType: String
	}

	type TransactionRuleInterval {
		dayOfMonth: Int
		dayOfWeek: String
		duration: Duration
		timeOfDay: String
		timeZone: String
		type: String!
	}

	type TransactionRuleRestrictions {
		activeNetworkTokens: ActiveNetworkTokensRestriction
		brandVariants: BrandVariantsRestriction
		countries: CountriesRestriction
		differentCurrencies: DifferentCurrenciesRestriction
		entryModes: EntryModesRestriction
		internationalTransaction: InternationalTransactionRestriction
		matchingTransactions: MatchingTransactionsRestriction
		mccs: MccsRestriction
		merchants: MerchantsRestriction
		processingTypes: ProcessingTypesRestriction
		timeOfDay: TimeOfDayRestriction
		totalAmount: TotalAmountRestriction
	}

	type Authentication {
		email: String
		password: String
		phone: Phone
	}

	type CardConfiguration {
		activation: String
		activationUrl: String
		bulkAddress: BulkAddress
		cardImageId: String
		carrier: String
		carrierImageId: String
		configurationProfileId: String!
		currency: String
		envelope: String
		insert: String
		language: String
		logoImageId: String
		pinMailer: String
		shipmentMethod: String
	}

	input InputSweepConfigurationV2 {
		counterparty: InputInputSweepCounterparty!
		currency: String!
		description: String
		id: String!
		status: String
		sweepAmount: InputInputAmount
		targetAmount: InputInputAmount
		triggerAmount: InputInputAmount
		type: String
	}

	input InputSweepCounterparty {
		balanceAccountId: String
		merchantAccount: String
		transferInstrumentId: String
	}

	input InputAmount {
		currency: String!
		value: Int!
	}

	input InputBalance {
		available: Int!
		balance: Int!
		currency: String!
		reserved: Int!
	}

	input InputTransactionRuleInterval {
		dayOfMonth: Int
		dayOfWeek: String
		duration: InputDuration
		timeOfDay: String
		timeZone: String
		type: String!
	}

	input InputTransactionRuleEntityKey {
		entityReference: String
		entityType: String
	}

	input InputTransactionRuleRestrictions {
		activeNetworkTokens: InputActiveNetworkTokensRestriction
		brandVariants: InputBrandVariantsRestriction
		countries: InputCountriesRestriction
		differentCurrencies: InputDifferentCurrenciesRestriction
		entryModes: InputEntryModesRestriction
		internationalTransaction: InputInternationalTransactionRestriction
		matchingTransactions: InputMatchingTransactionsRestriction
		mccs: InputMccsRestriction
		merchants: InputMerchantsRestriction
		processingTypes: InputProcessingTypesRestriction
		timeOfDay: InputTimeOfDayRestriction
		totalAmount: InputTotalAmountRestriction
	}

	input InputContactDetails {
		address: InputAddress!
		email: String!
		phone: InputPhone!
		webAddress: String
	}

	input InputBankAccount {
		iban: String!
	}

	input InputCard {
		authentication: InputAuthentication
		bin: String
		brand: String!
		brandVariant: String!
		cardholderName: String!
		configuration: InputCardConfiguration
		cvc: String
		deliveryContact: InputDeliveryContact
		expiration: InputExpiry
		formFactor: String!
		lastFour: String
		number: String!
	}

	input InputCardInfo {
		authentication: InputAuthentication
		brand: String!
		brandVariant: String!
		cardholderName: String!
		configuration: InputCardConfiguration
		deliveryContact: InputDeliveryContact
		formFactor: String!
	}

	input InputBalance {
		available: Int!
		balance: Int!
		currency: String!
		reserved: Int!
	}

	input InputContactDetails {
		address: InputAddress!
		email: String!
		phone: InputPhone!
		webAddress: String
	}

	input InputBankAccount {
		iban: String!
	}

	input InputCard {
		authentication: InputAuthentication
		bin: String
		brand: String!
		brandVariant: String!
		cardholderName: String!
		configuration: InputCardConfiguration
		cvc: String
		deliveryContact: InputDeliveryContact
		expiration: InputExpiry
		formFactor: String!
		lastFour: String
		number: String!
	}

	input InputTransactionRuleEntityKey {
		entityReference: String
		entityType: String
	}

	input InputTransactionRuleInterval {
		dayOfMonth: Int
		dayOfWeek: String
		duration: InputDuration
		timeOfDay: String
		timeZone: String
		type: String!
	}

	input InputTransactionRuleRestrictions {
		activeNetworkTokens: InputActiveNetworkTokensRestriction
		brandVariants: InputBrandVariantsRestriction
		countries: InputCountriesRestriction
		differentCurrencies: InputDifferentCurrenciesRestriction
		entryModes: InputEntryModesRestriction
		internationalTransaction: InputInternationalTransactionRestriction
		matchingTransactions: InputMatchingTransactionsRestriction
		mccs: InputMccsRestriction
		merchants: InputMerchantsRestriction
		processingTypes: InputProcessingTypesRestriction
		timeOfDay: InputTimeOfDayRestriction
		totalAmount: InputTotalAmountRestriction
	}

	input InputAuthentication {
		email: String
		password: String
		phone: InputPhone
	}

	input InputCardConfiguration {
		activation: String
		activationUrl: String
		bulkAddress: InputBulkAddress
		cardImageId: String
		carrier: String
		carrierImageId: String
		configurationProfileId: String!
		currency: String
		envelope: String
		insert: String
		language: String
		logoImageId: String
		pinMailer: String
		shipmentMethod: String
	}

  
    
type Query {
		 get-accountHolders-id(id: String!): AccountHolder,

		 get-accountHolders-id-balanceAccounts(id: String!, offset: Int, limit: Int): PaginatedBalanceAccountsResponse,

		 get-balanceAccounts-balanceAccountId-sweeps(balanceAccountId: String!, offset: Int, limit: Int): BalanceSweepConfigurationsResponse,

		 get-balanceAccounts-balanceAccountId-sweeps-sweepId(balanceAccountId: String!, sweepId: String!): SweepConfigurationV2,

		 get-balanceAccounts-id(id: String!): BalanceAccount,

		 get-balanceAccounts-id-paymentInstruments(id: String!, offset: Int, limit: Int): PaginatedPaymentInstrumentsResponse,

		 get-balancePlatforms-id(id: String!): BalancePlatform,

		 get-balancePlatforms-id-accountHolders(id: String!, offset: Int, limit: Int): PaginatedAccountHoldersResponse,

		 get-paymentInstrumentGroups-id(id: String!): PaymentInstrumentGroup,

		 get-paymentInstrumentGroups-id-transactionRules(id: String!): TransactionRulesResponse,

		 get-paymentInstruments-id(id: String!): PaymentInstrument,

		 get-paymentInstruments-id-transactionRules(id: String!): TransactionRulesResponse,

		 get-transactionRules-transactionRuleId(transactionRuleId: String!): TransactionRuleResponse,

}

type Mutation {
		 post-accountHolders(input: InputAccountHolderInfo): AccountHolder,

		 post-balanceAccounts(input: InputBalanceAccountInfo): BalanceAccount,

		 post-balanceAccounts-balanceAccountId-sweeps(balanceAccountId: String!, input: InputSweepConfigurationV2): SweepConfigurationV2,

		 delete-balanceAccounts-balanceAccountId-sweeps-sweepId(balanceAccountId: String!, sweepId: String!): String,

		 post-paymentInstrumentGroups(input: InputPaymentInstrumentGroupInfo): PaymentInstrumentGroup,

		 post-paymentInstruments(input: InputPaymentInstrumentInfo): PaymentInstrument,

		 post-transactionRules(input: InputTransactionRuleInfo): TransactionRule,

		 delete-transactionRules-transactionRuleId(transactionRuleId: String!): TransactionRule,

}

`;

const resolvers = {
    Query: {
	 get-accountHolders-id: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders/${args.id}?`),
	 get-accountHolders-id-balanceAccounts: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders/${args.id}/balanceAccounts? +'&'+${'offset='+ args.offset ? args.offset : ''} +'&'+${'limit='+ args.limit ? args.limit : ''}`),
	 get-balanceAccounts-balanceAccountId-sweeps: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/balanceAccounts/${args.balanceAccountId}/sweeps? +'&'+${'offset='+ args.offset ? args.offset : ''} +'&'+${'limit='+ args.limit ? args.limit : ''}`),
	 get-balanceAccounts-balanceAccountId-sweeps-sweepId: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/balanceAccounts/${args.balanceAccountId}/sweeps/${args.sweepId}? +'&'+`),
	 get-balanceAccounts-id: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/balanceAccounts/${args.id}?`),
	 get-balanceAccounts-id-paymentInstruments: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/balanceAccounts/${args.id}/paymentInstruments? +'&'+${'offset='+ args.offset ? args.offset : ''} +'&'+${'limit='+ args.limit ? args.limit : ''}`),
	 get-balancePlatforms-id: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/balancePlatforms/${args.id}?`),
	 get-balancePlatforms-id-accountHolders: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/balancePlatforms/${args.id}/accountHolders? +'&'+${'offset='+ args.offset ? args.offset : ''} +'&'+${'limit='+ args.limit ? args.limit : ''}`),
	 get-paymentInstrumentGroups-id: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/paymentInstrumentGroups/${args.id}?`),
	 get-paymentInstrumentGroups-id-transactionRules: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/paymentInstrumentGroups/${args.id}/transactionRules?`),
	 get-paymentInstruments-id: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/paymentInstruments/${args.id}?`),
	 get-paymentInstruments-id-transactionRules: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/paymentInstruments/${args.id}/transactionRules?`),
	 get-transactionRules-transactionRuleId: (root, args) => get(`https://balanceplatform-api-test.adyen.com/bcl/v2/transactionRules/${args.transactionRuleId}?`),

    },
    Mutation: {
	 post-accountHolders: (root, args) => post(`https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders?`,args),
	 post-balanceAccounts: (root, args) => post(`https://balanceplatform-api-test.adyen.com/bcl/v2/balanceAccounts?`,args),
	 post-balanceAccounts-balanceAccountId-sweeps: (root, args) => post(`https://balanceplatform-api-test.adyen.com/bcl/v2/balanceAccounts/${args.balanceAccountId}/sweeps?`,args),
	 delete-balanceAccounts-balanceAccountId-sweeps-sweepId: (root, args) => deleteData(`https://balanceplatform-api-test.adyen.com/bcl/v2/balanceAccounts/${args.balanceAccountId}/sweeps/${args.sweepId}? +'&'+`,args),
	 post-paymentInstrumentGroups: (root, args) => post(`https://balanceplatform-api-test.adyen.com/bcl/v2/paymentInstrumentGroups?`,args),
	 post-paymentInstruments: (root, args) => post(`https://balanceplatform-api-test.adyen.com/bcl/v2/paymentInstruments?`,args),
	 post-transactionRules: (root, args) => post(`https://balanceplatform-api-test.adyen.com/bcl/v2/transactionRules?`,args),
	 delete-transactionRules-transactionRuleId: (root, args) => deleteData(`https://balanceplatform-api-test.adyen.com/bcl/v2/transactionRules/${args.transactionRuleId}?`,args),

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