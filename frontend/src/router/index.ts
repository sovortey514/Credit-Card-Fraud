import { createRouter, createWebHistory } from 'vue-router';
import DashboardLayout from '../layouts/DashboardLayout.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [{
    path: '/',
    component: DashboardLayout,
    children: [
      { path: '', component: () => import('../views/DashboardView.vue') },
      { path: 'transactions', component: () => import('../views/TransactionsView.vue') },
      { path: 'analytics', component: () => import('../views/FraudAnalyticsView.vue') },
      { path: 'models', component: () => import('../views/ModelPerformanceView.vue') },
      { path: 'settings', component: () => import('../views/SettingsView.vue') },
    ],
  }],
});

export default router;
