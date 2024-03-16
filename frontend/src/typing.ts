export type User = {
	id: number;
	username: string;
	registeredAt: string;
	tokenValidityPeriod: number;
};

export type LoginResponseData = {
	accessToken: string;
	tokenType: string;
};

export type APIError = {
	message: string;
	code: number;
	target: string;
};
export type InputStatus = "normal" | "error" | "success";
export type AuthAction = "login" | "register";
export type AuthStatus = "normal" | "loading" | "fail" | "success";
export type InputElement = {
	status: InputStatus;
	value: string;
	conditions: { [key: string]: boolean };
};
export type RegisterStatus = {
	username: InputElement;
	password: InputElement;
	passwordConfirmation: InputElement;
};
export type LoginStatus = {
	username: InputElement;
	password: InputElement;
};
