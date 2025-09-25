<template>
  <!-- SIDEBAR DESKTOP -->
  <aside class="hidden md:flex fixed top-0 left-0 h-screen w-24 flex-col
         justify-between items-center bg-primary-second backdrop-blur-xl
         border-r border-white/8 z-40 pt-5">
    <!-- logo -->
    <div>
      <img :src="logo" alt="Logo Nexus" class="w-12 h-12 object-contain" />
    </div>

    <!-- nav items (centralizados) -->
    <div class="flex flex-col gap-7 flex-1 justify-center">
      <button v-for="(item, idx) in navItems" :key="item.label" @click="activeIndex = idx"
        class="flex items-center justify-center" :aria-pressed="activeIndex === idx">
        <NavItem :icon="item.icon" :label="item.label" :color="item.color" :active="activeIndex === idx" />
      </button>
    </div>

    <!-- avatar -->
    <div class="relative mb-6" ref="menuRef">
      <button @click.stop="toggleDropdown" class="w-11 h-11 rounded-full overflow-hidden border-2 border-white/10
             hover:border-blue-400/30 transition" aria-haspopup="true" :aria-expanded="showDropdown">
        <img :src="avatar" alt="User" class="w-full h-full object-cover" />
      </button>

      <!-- dropdown -->
      <transition name="dropdown">
        <div v-if="showDropdown" class="absolute left-full ml-4 bottom-0 z-50 w-44 bg-black/60
               backdrop-blur-md border border-white/10 rounded-lg
               overflow-hidden shadow-2xl">
          <button class="w-full text-left px-4 py-2 text-white hover:bg-white/6 transition">
            Perfil
          </button>
          <button class="w-full text-left px-4 py-2 text-white hover:bg-white/6 transition">
            Configurações
          </button>
          <button class="w-full text-left px-4 py-2 text-[15px] font-medium" :class="sairClass" @click="onSignOut">
            Sair
          </button>
        </div>
      </transition>
    </div>
  </aside>

  <!-- BOTTOM NAV MOBILE -->
  <nav class="md:hidden fixed bottom-5 left-1/2 -translate-x-1/2 flex justify-between items-center
           w-[94%] max-w-lg bg-black/40 backdrop-blur-lg border border-white/8 rounded-3xl py-3 px-4 z-50 shadow-lg">
    <button v-for="(item, idx) in navItems" :key="item.label" @click="activeIndex = idx"
      class="flex-1 flex justify-center">
      <NavItem :icon="item.icon" :color="item.color" :active="activeIndex === idx" />
    </button>
  </nav>

  <!-- AVATAR MOBILE (top-right) -->
  <div class="md:hidden fixed top-4 right-4 z-50" ref="menuRefMobile">
    <div class="relative">
      <button @click.stop="toggleDropdown"
        class="w-10 h-10 rounded-full overflow-hidden border-2 border-white/10 hover:border-blue-400/30 transition">
        <img :src="avatar" alt="User" class="w-full h-full object-cover" />
      </button>

      <transition name="dropdown">
        <div v-if="showDropdown"
          class="absolute right-0 mt-2 z-50 w-44 bg-black/60 backdrop-blur-md border border-white/10 rounded-lg overflow-hidden shadow-2xl">
          <button class="w-full text-left px-4 py-2 text-white hover:bg-white/6 transition">Perfil</button>
          <button class="w-full text-left px-4 py-2 text-white hover:bg-white/6 transition">Configurações</button>
          <button class="w-full text-left px-4 py-2 text-[15px] font-medium" :class="sairClass" @click="onSignOut">
            Sair
          </button>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import NavItem from './NavItem.vue'
import logoImg from '@/assets/img/logoNexus.png'
import { Home, Wallet, BarChart3, Goal } from 'lucide-vue-next'

/* ---------- data ---------- */
const navItems = [
  { icon: Home, label: 'Início', color: '#00d1ff' },       // cyan
  { icon: Wallet, label: 'Lançamentos', color: '#ff7a2d' }, // orange
  { icon: BarChart3, label: 'Relatórios', color: '#8a5cff' }, // purple
  { icon: Goal, label: 'Metas', color: '#ff4d9a' },       // pink
]

const activeIndex = ref(0)
const showDropdown = ref(false)
const menuRef = ref<HTMLElement | null>(null)
const menuRefMobile = ref<HTMLElement | null>(null)

/* demo assets (troque pelo avatar real) */
const logo = logoImg
const avatar = 'https://static.vecteezy.com/system/resources/previews/023/465/688/non_2x/contact-dark-mode-glyph-ui-icon-address-book-profile-page-user-interface-design-white-silhouette-symbol-on-black-space-solid-pictogram-for-web-mobile-isolated-illustration-vector.jpg'

/* ---------- dropdown handlers ---------- */
function toggleDropdown() {
  showDropdown.value = !showDropdown.value
}
function onSignOut() {
  // placeholder — substitua sua lógica de logout
  alert('Sair clicado')
  showDropdown.value = false
}
function handleClickOutside(ev: Event) {
  const target = ev.target as Node
  if (menuRef.value && !menuRef.value.contains(target) && menuRefMobile.value && !menuRefMobile.value.contains(target)) {
    showDropdown.value = false
  }
}

onMounted(() => document.addEventListener('click', handleClickOutside))
onUnmounted(() => document.removeEventListener('click', handleClickOutside))

/* estilo para o botão sair (vermelho amarronzado com fundo escuro e hover mais claro) */
const sairClass = 'text-[#c0655a] bg-[#3a0f0f]/30 hover:bg-[#5a1b1b]/40 transition'
</script>

<style scoped>
/* dropdown animation: scale + fade */
.dropdown-enter-active,
.dropdown-leave-active {
  transition: opacity 0.16s ease, transform 0.16s ease;
}

.dropdown-enter-from,
.dropdown-leave-to {
  opacity: 0;
  transform: translateY(6px) scale(0.98);
}

.dropdown-enter-to,
.dropdown-leave-from {
  opacity: 1;
  transform: translateY(0) scale(1);
}
</style>
