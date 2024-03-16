<script setup lang="ts">
	import { RouterLink, useRouter } from "vue-router";
	import UserAvatar from "./icons/UserAvatar.vue";
	import SiteLogo from "./icons/SiteLogo.vue";
	import { reactive, watch, type Ref, ref } from "vue";
	import { updateSignal } from "@/store";
	import type { User } from "@/typing";
	const currentUser: Ref<null | User> = ref(null);
	const router = useRouter();
	watch(updateSignal, () => {
		loadUserData();
	});
	function loadUserData(): void {
		const data = sessionStorage.getItem("userData");
		if (data) {
			currentUser.value = JSON.parse(data);
		}
	}
	function signOut(): void {
		sessionStorage.clear();
		localStorage.removeItem("accessToken");
		updateSignal.value = !updateSignal.value;
		currentUser.value = null;
		router.push({
			name: "Login",
		});
	}
</script>
<template>
	<div class="parent-N1f5-onTJx">
		<div class="parent-NytAQi3T1g">
			<RouterLink to="/">
				<SiteLogo class="parent-E1ezLsnp1x" />
			</RouterLink>
			<RouterLink class="parent-NJvpvi261g" to="/">
				My website
			</RouterLink>
		</div>
		<div class="parent-EkRAQo2Tke">
			<div class="parent-4yJ-KT36Jg" v-if="currentUser">
				<div class="parent-EkXcKahTkg">
					<button class="parent-NJifq636yx" @click="signOut">
						Sign out
					</button>

					<div class="parent-EJniFph6ke">
						<UserAvatar />
					</div>
				</div>
			</div>
			<div class="parent-412UMan6kg" v-if="!currentUser">
				<div class="child-VJUPzT26kl">
					<RouterLink
						class="child-EJ75za3ayl"
						:to="{ name: 'Register' }"
					>
						Sign up
					</RouterLink>
				</div>
				<div class="child-VJUPzT26kl">
					<RouterLink
						class="child-EJ75za3ayl"
						:to="{ name: 'Login' }"
					>
						Sign in
					</RouterLink>
				</div>
			</div>
		</div>
	</div>
</template>
<style>
	.parent-NJifq636yx {
		margin: 0 10px;
	}
</style>
