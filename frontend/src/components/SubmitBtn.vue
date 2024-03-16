<script setup lang="ts">
	import { computed } from "vue";
	import Login from "./icons/Login.vue";
	import Register from "./icons/Register.vue";
	import Success from "./icons/Success.vue";
	import Fail from "./icons/Fail.vue";
	import Loading from "./icons/Loading.vue";
	import type { AuthAction, AuthStatus } from "@/typing";
	const props = defineProps<{
		btnType: AuthAction;
		btnStatus: AuthStatus;
	}>();
	const btnItems = {
		login: {
			normal: {
				text: "Login",
				icon: Login,
			},
			fail: {
				text: "Fail",
				icon: Fail,
			},
			loading: {
				text: "Logining",
				icon: Loading,
			},
			success: {
				text: "Success",
				icon: Success,
			},
		},
		register: {
			normal: {
				text: "Register",
				icon: Register,
			},
			fail: {
				text: "Fail",
				icon: Fail,
			},
			loading: {
				text: "Registering",
				icon: Loading,
			},
			success: {
				text: "Success",
				icon: Success,
			},
		},
	};
	const btnContent = computed(() => {
		return btnItems[props.btnType][props.btnStatus];
	});
</script>
<template>
	<button
		type="submit"
		:class="[btnType, btnStatus]"
		class="parent-V1It-lT61x"
	>
		<div class="parent-V1rJzxaT1g">
			<span class="parent-NyjT-eapye">{{ btnContent.text }}</span>
			<component class="parent-EJTlzga61x" :is="btnContent.icon" />
		</div>
	</button>
</template>
<style scoped>
	.parent-V1It-lT61x {
		width: 260px;
		height: 54px;
		display: flex;
		justify-content: center;
		align-items: center;
		border: none;
		cursor: pointer;
		border-radius: 50px;
	}
	.login.normal {
		background-color: var(--second-color);
	}
	.login.loading {
		background-color: var(--second-color);
		opacity: 0.7;
	}
	.register.normal {
		background-color: var(--first-color);
	}
	.register.loading {
		background-color: var(--first-color);
		opacity: 0.7;
		cursor: not-allowed;
	}
	.fail {
		background-color: var(--error-color);
		cursor: not-allowed;
	}
	.success {
		background-color: var(--success-color);
		cursor: not-allowed;
	}
	.parent-V1rJzxaT1g {
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	.parent-NyjT-eapye {
		margin-right: 10px;
		font-size: 1rem;
		font-weight: 400;
	}
    .parent-EJTlzga61x {
        width: 24px;
        height: 24px;
    }
</style>
