<template>
  <div class="dashboard-layout">
    <AppHeader />
    <div class="dashboard-layout__body"><AppSidebar /><RouterView /></div>
  </div>
</template>
<script setup lang="ts">
import AppHeader from '../components/common/AppHeader.vue';
import AppSidebar from '../components/common/AppSidebar.vue';
</script>
<style scoped>
.dashboard-layout__body { display: grid; grid-template-columns: 14rem minmax(0, 1fr); min-height: calc(100vh - 3rem); }
@media (max-width: 700px) { .dashboard-layout__body { grid-template-columns: 1fr; } }
</style>
