<script setup lang="ts">
	import { useRoute, useRouter } from "vue-router";
	import type { AuthAction } from "@/typing";
	import Login from "@/components/icons/Login.vue";
	import Register from "@/components/icons/Register.vue";
	const route = useRoute();
	const router = useRouter();

	function changeAction(a: AuthAction): void {
		switch (a) {
			case "login":
				router.push({
					name: "Login",
				});
				break;
			case "register":
				router.push({
					name: "Register",
				});
				break;
		}
	}
</script>
<template>
	<div class="parent-N1WKCpLjyx">
		<div class="parent-VJ9DyR8skl">
			<div class="parent-NJPD3aUi1x">
				<button
					class="child-EJhsn6Is1l login"
					type="button"
					:class="[
						{ active: route.name === 'Login' },
						{ normal: route.name != 'Login' },
					]"
					@click="changeAction('login')"
				>
					<span class="child-VyG0hT8iyx" v-if="route.name === 'Login'"
						>Login</span
					>
					<component
						style="height: 36px; width: 36px"
						:is="Login"
						v-if="route.name != 'Login'"
					/>
				</button>
				<button
					class="child-EJhsn6Is1l register"
					type="button"
					:class="[
						{ active: route.name === 'Register' },
						{ normal: route.name != 'Register' },
					]"
					@click="changeAction('register')"
				>
					<component
						style="height: 36px; width: 36px"
						:is="Register"
						v-if="route.name != 'Register'"
					/>
					<span
						class="child-VyG0hT8iyx"
						v-if="route.name === 'Register'"
						>Register</span
					>
				</button>
			</div>
			<RouterView />
		</div>
	</div>
</template>
<style scoped>
	.parent-NJPD3aUi1x {
		width: 400px;
		height: 80px;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 10px;
	}
	.child-EJhsn6Is1l {
		height: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		border: none;
		transition: width 0.5s ease;
        cursor: pointer;
	}
	.child-EJhsn6Is1l.login {
		background-color: var(--second-color);
	}
	.child-EJhsn6Is1l.register {
		background-color: var(--first-color);
	}
	.child-EJhsn6Is1l.active {
		width: 340px;
	}
	.child-EJhsn6Is1l.normal {
		width: 60px;
	}
	.child-VyG0hT8iyx {
		font-size: 1.5rem;
		font-weight: 800;
		letter-spacing: 1px;
	}
	.parent-N1WKCpLjyx {
		display: flex;
		justify-content: center;
	}
	.parent-VJ9DyR8skl {
		margin-top: 50px;
        margin-bottom: 50px;
	}
</style>
