import type { LoginResponseData, User } from "./typing";
import { getAuthorization } from "./utlis";

const rootUrl = "http://127.0.0.1:5000";

export async function postUser(
	username: string,
	password: string
): Promise<User> {
	const response = await fetch(rootUrl + "/account/users", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({ username: username, password: password }),
	});
	const responseData = await response.json();
	if (response.status === 200) {
		return responseData;
	} else {
		throw responseData.error;
	}
}

export async function postToken(
	username: string,
	password: string
): Promise<LoginResponseData> {
	const response = await fetch(rootUrl + "/account/token", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			username: username,
			password: password,
			grantType: "password",
		}),
	});
	const responseData = await response.json();
	if (response.status === 200) {
		return responseData;
	} else {
		throw responseData.error;
	}
}
export async function verifyUser(): Promise<boolean> {
	const response = await fetch(rootUrl + "/account/verify", {
		headers: { Authorization: getAuthorization() },
	});
	if (response.status === 200) {
		return true;
	} else {
		return false;
	}
}
export async function getUser(username: string): Promise<User> {
	const response = await fetch(rootUrl + "/account/user/" + username);
	const responseData = await response.json();
	if (response.status === 200) {
		return responseData;
	} else {
		throw responseData.error;
	}
}
export async function getHomeVisits(): Promise<number> {
	const response = await fetch(rootUrl + "/home-visits");
	const responseData = await response.json();
	if (response.status === 200) {
		return responseData;
	} else {
		throw responseData.error;
	}
}
