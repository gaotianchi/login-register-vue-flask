import { createRouter, createWebHistory } from "vue-router";
import { verifyUser } from "./api";
import { updateSignal } from "./store";

const router = createRouter({
	history: createWebHistory(import.meta.env.BASE_URL),
	routes: [
		{
			path: "/",
			name: "Home",
			component: () => import("./views/Home.vue"),
			meta: { loginRequired: false },
		},
		{
			path: "/auth",
			component: () => import("@/views/AuthPanel.vue"),
			meta: { loginRequired: false },
			children: [
				{
					path: "register",
					component: () => import("@/components/RegisterForm.vue"),
					name: "Register",
				},
				{
					path: "login",
					component: () => import("@/components/LoginForm.vue"),
					name: "Login",
				},
			],
		},
		{
			path: "/after-login/:username",
			name: "AfterLogin",
			component: () => import("./views/AfterLogin.vue"),
			meta: { loginRequired: true },
			props: true,
		},
	],
});
router.beforeEach(async (to, from) => {
	updateSignal.value = !updateSignal.value;
	if (to.meta.loginRequired) {
		const isAuthenticated = await verifyUser();
		if (!isAuthenticated && to.name !== "Login") {
			return { name: "Login" };
		} else {
			if (to.name === "Login") {
				alert("You have logged in.");
			}
		}
	}
});
export default router;
