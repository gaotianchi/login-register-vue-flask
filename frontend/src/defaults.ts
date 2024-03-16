import type { LoginStatus, RegisterStatus, User } from "./typing";

export const defaultRegisterStatus: RegisterStatus = {
	username: {
		value: "",
		status: "normal",
		conditions: {
			condition_1: true,
			condition_2: true,
			condition_3: true,
			condition_4: true,
		},
	},
	password: {
		value: "",
		status: "normal",
		conditions: {
			condition_1: true,
			condition_2: true,
		},
	},
	passwordConfirmation: {
		value: "",
		status: "normal",
		conditions: {
			condition_1: true,
			condition_2: true,
		},
	},
};
export const defaultLoginStatus: LoginStatus = {
	username: {
		value: "",
		status: "normal",
		conditions: {
			condition_1: true,
			condition_2: true,
			condition_3: true,
			condition_4: true,
		},
	},
	password: {
		value: "",
		status: "normal",
		conditions: {
			condition_1: true,
			condition_2: true,
			condition_3: true,
		},
	},
};
export const defaultUser: User = {
	id: 0,
	username: "",
	registeredAt: "2024-03-15T08:27:37+0000",
	tokenValidityPeriod: 0,
};
