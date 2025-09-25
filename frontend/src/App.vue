<template>

  <head>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap">
  </head>
  <div class="flex">
    <!-- navbar só aparece em certas rotas -->
    <Navbar v-if="showNavbar" />

    <!-- conteúdo -->
    <div class="flex-1">
      <RouterView />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Navbar from './components/NavBarComponent.vue'

const route = useRoute()

// rotas que devem mostrar o navbar
const navbarRoutes = ['/home', '/lancamentos', '/relatorios', '/metas', '/perfil', '/configuracoes']

const showNavbar = computed(() =>
  navbarRoutes.some(r => route.path.startsWith(r))
)
</script>
