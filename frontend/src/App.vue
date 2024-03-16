<script setup lang="ts">
	import { RouterLink, RouterView } from "vue-router";
	import SiteHeader from "@/components/SiteHeader.vue";
	import SiteFooter from "./components/SiteFooter.vue";
</script>

<template>
	<header class="parent-416R-on6Jl">
		<SiteHeader />
	</header>
	<section class="parent-Nk21Gi2pkl">
		<RouterView />
	</section>
	<footer>
		<SiteFooter />
	</footer>
</template>

<style>
	.parent-416R-on6Jl {
		height: var(--header-height);
	}
	.parent-Nk21Gi2pkl {
		min-height: calc(100vh - var(--header-height) - var(--footer-height));
	}
</style>
