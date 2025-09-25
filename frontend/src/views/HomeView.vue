<script setup lang="ts">
import Navbar from "@/components/NavBarComponent.vue"
</script>

<template>
  <div class="bg-[#050017] min-h-screen text-white flex">
    <!-- Navbar -->
    <Navbar />

    <!-- Conteúdo principal -->
    <main class="flex-1 md:ml-20 flex flex-col items-center justify-center p-6">
      <h1 class="text-4xl font-bold">🏠 Bem-vindo à Home</h1>
      <p class="mt-4 text-gray-400">Aqui vai o conteúdo da sua tela inicial...</p>
    </main>
  </div>
</template>
