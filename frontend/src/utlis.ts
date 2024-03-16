import type { LoginResponseData } from "./typing";
import moment from "moment-timezone";
export function setAccessToken(data: LoginResponseData): void {
	localStorage.setItem("accessToken", JSON.stringify(data));
}
export function getAccessToken(): LoginResponseData | null {
	const data = localStorage.getItem("accessToken");
	if (data) {
		return JSON.parse(data);
	} else {
		return null;
	}
}
export function getLocalDatetime(dateString: string): Date {
	const localizedMoment = moment.utc(dateString).local();
	return localizedMoment.toDate();
}

export function dateFormatter(date: Date, format?: string): string {
	const dateFormat = format || "YYYY-MM-DD  hh:mm  A";
	return moment(date).format(dateFormat);
}
export function getAuthorization(): string {
	const tokenData = getAccessToken();
	return tokenData?.tokenType + " " + tokenData?.accessToken;
}

export function usernameCondition_1(value: string): boolean {
	const reg = new RegExp("^[a-z0-9_]+$");
	return reg.test(value);
}
export function usernameCondition_2(value: string): boolean {
	const reg = new RegExp("^[a-z]");
	return reg.test(value);
}
export function usernameCondition_3(value: string): boolean {
	return value.length > 2 && value.length < 100;
}
export function passwordCondition_1(value: string): boolean {
	return value.length > 5;
}
export function passwordCondition_2(value: string): boolean {
	const reg = new RegExp("^(?=.*[a-zA-Z])(?=.*\\d).+$");
	return reg.test(value);
}
