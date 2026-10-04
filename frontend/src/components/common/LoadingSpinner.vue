<template>
  <span class="loading-spinner" role="status" aria-label="Loading" />
</template>

<style scoped>
.loading-spinner { display: inline-block; width: 1.25rem; aspect-ratio: 1; border: 2px solid currentColor; border-right-color: transparent; border-radius: 50%; animation: spin 0.7s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }
</style>
