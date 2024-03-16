<script setup lang="ts">
	import { getUser } from "@/api";
	import { defaultUser } from "@/defaults";
	import type { User } from "@/typing";
	import { onMounted, ref, type Ref } from "vue";
	import { dateFormatter, getLocalDatetime } from "@/utlis";
	const props = defineProps<{
		username: string;
	}>();
	const currentUser: Ref<User> = ref(defaultUser);
	onMounted(() => {
		initUserData();
	});
	function initUserData(): void {
		getUser(props.username)
			.then((response) => {
				currentUser.value = response;
			})
			.catch((error) => {
				console.error(error);
			});
	}
</script>
<template>
	<div class="parent-V1diRATTkx">
		<div class="parent-EyXwRAa6yg">
			<img
				class="parent-NJWtRC66kx"
				src="@/assets/open-lock.jpg"
				alt="open-lock"
			/>
		</div>
		<div class="parent-E1dLDRnTkg">
			<h1 class="parent-41Gk5Ahpkg">
				Hello, {{ currentUser.username }}!
			</h1>
			<p class="child-4kNlqA2akg">
				Congratulations on successfully logging into the website!
			</p>
			<p>
				Your account registered at
				<strong>
					{{
						dateFormatter(
							getLocalDatetime(currentUser.registeredAt),
							"ddd MMM DD YYYY"
						)
					}}.</strong
				>
			</p>
			<p class="child-4kNlqA2akg">
				Back to <RouterLink to="/">HOME</RouterLink>.
			</p>
		</div>
	</div>
</template>
<style>
	.parent-EyXwRAa6yg {
		padding: 40px 20px;
	}
	.parent-V1diRATTkx {
		display: grid;
		grid-template-columns: auto 1fr;
		gap: 20px;
	}
	.parent-NJWtRC66kx {
		width: 500px;
		height: auto;
	}
</style>
