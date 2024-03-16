<script setup lang="ts">
	import Fail from "./icons/Fail.vue";
	const props = defineProps<{
		status: boolean;
	}>();
</script>
<template>
	<div class="parent-EkQQhPEokl" v-if="props.status">
		<div class="parent-Nk7VmcBjJg">
			<component :is="Fail" class="parent-NkrI7g6aJg" />
		</div>
		<span class="parent-Vk-U6DVsJe">
			<slot></slot>
		</span>
	</div>
</template>
