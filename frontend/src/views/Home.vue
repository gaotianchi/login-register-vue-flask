<script setup lang="ts">
	import { getHomeVisits } from "@/api";
	import type { User } from "@/typing";
	import { onMounted, ref, type Ref } from "vue";
	const currentVisits = ref(0);
	const currentUser: Ref<User | null> = ref(null);
	onMounted(() => {
		loadVisits();
		loadUserData();
	});
	function loadVisits(): void {
		getHomeVisits()
			.then((response) => {
				currentVisits.value = response;
			})
			.catch((error) => {
				console.error(error);
			});
	}
	function loadUserData(): void {
		const data = sessionStorage.getItem("userData");
		if (data) {
			currentUser.value = JSON.parse(data);
		}
	}
</script>
<template>
	<div class="parent-Vy23GQ6ayg">
		<div class="parent-NkivjyCake">
			<img
				class="child-N1NsokRayl"
				v-if="!currentUser"
				src="@/assets/lock.jpg"
				alt="lock"
			/>
			<img
				class="child-N1NsokRayl"
				v-else
				src="@/assets/open-lock.jpg"
				alt="open-lock"
			/>
		</div>
		<div class="parent-E1dLDRnTkg">
			<h1 v-if="!currentUser" class="parent-41Gk5Ahpkg">
				Hello, stranger!
			</h1>
			<h1 v-if="currentUser" class="parent-41Gk5Ahpkg">
				Hello, {{ currentUser.username }}!
			</h1>
			<p class="child-4kNlqA2akg">
				Welcome to <strong>HOME</strong> page.
			</p>
			<p class="child-4kNlqA2akg" v-if="!currentUser">
				You do not need to
				<RouterLink :to="{ name: 'Login' }">log in</RouterLink> to
				access this page.
			</p>
			<p v-if="currentUser">
				You have successfully logged in. Back to
				<RouterLink
					:to="{
						name: 'AfterLogin',
						params: { username: currentUser.username },
					}"
					>AfterLogin</RouterLink
				>
			</p>
		</div>
		<div class="parent-VkFAG7T61l">
			<div class="parent-4yLFXmTpJx">
				<div class="parent-Eypyc7aayl">VISITS</div>
				<div class="parent-41rl9QpTJl">{{ currentVisits }}</div>
			</div>
		</div>
	</div>
</template>
<style>
	.child-N1NsokRayl {
		width: 500px;
		height: auto;
		margin: 40px 20px;
	}
	.parent-N1LF2Caa1x {
		width: 500px;
		height: auto;
	}
	.parent-Eypyc7aayl {
		font-size: larger;
		color: lightgray;
	}
	.parent-41rl9QpTJl {
		font-size: 100px;
	}
	.parent-Vy23GQ6ayg {
		min-height: calc(100vh - var(--header-height) - var(--footer-height));
		display: grid;
		grid-template-columns: auto 1fr auto;
		gap: 20px;
	}
	.parent-4yLFXmTpJx {
		width: 150px;
		height: 150px;
		display: flex;
		flex-direction: column;
		align-items: center;
		background: white;
		box-shadow: var(--box-shadow);
		padding: 20px;
	}
	.parent-VkFAG7T61l {
		width: 300px;
		display: flex;
		justify-content: center;
		margin-top: 40px;
	}
</style>
