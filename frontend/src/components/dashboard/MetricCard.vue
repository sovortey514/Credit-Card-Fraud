<template>
  <article class="metric-card"><h2>{{ label }}</h2><p>{{ value }}</p></article>
</template>
<script setup lang="ts">
defineProps<{ label: string; value: string | number }>();
</script>
