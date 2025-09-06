<template>
  <div class="grid grid-cols-1 md:grid-cols-2 h-screen">
    <!-- Coluna Esquerda -->
    <div class="flex flex-col items-center justify-center px-6 py-5 bg-white">
      <!-- Logo -->
      <img src="../../assets/img/LogoZentavos.png" alt="Icone" class="w-14 mb-4" />

      <!-- Inputs -->
      <div class="w-full max-w-sm space-y-4">
        <InputComponent v-model="nome" tipo="text" label="Nome" icon="badge" required/>
        <InputComponent v-model="email" tipo="email" label="E-mail" icon="mail" required/>
        <div class="w-full">
          <InputComponent v-model="senha" tipo="password" label="Senha" icon="password" required />
          <InputComponent v-model="confirmarSenha" tipo="password" label="Confirmar senha" icon="password" class="mt-4" required />
        </div>
      </div>

      <!-- Botões -->
      <div class="w-full max-w-sm mt-6 space-y-3">
        <button
          class="cursor-pointer w-full py-2 bg-primary-light text-white font-semibold rounded-lg shadow-md hover:bg-primary transition"
          @click="cadastrar()">
          Cadastrar-se
        </button>

        <button
          class="w-full cursor-pointer flex items-center justify-center gap-2 border border-gray-300 bg-white py-2 rounded-lg text-gray-700 font-medium hover:bg-gray-100 transition">
          <svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6">
            <path
              d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"
              fill="#FFC107"></path>
            <path
              d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"
              fill="#FF3D00"></path>
            <path
              d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"
              fill="#4CAF50"></path>
            <path
              d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"
              fill="#1976D2"></path>
          </svg>
          Continuar com Google
        </button>
      </div>

      <!-- Link Cadastro -->
      <p class="mt-6 text-sm text-gray-700">
        Já possui uma conta?
        <RouterLink to="/" class="text-primary-light font-medium hover:underline">Login</RouterLink>
      </p>
    </div>

    
    <!-- Coluna Esquerda -->
    <div class="bg-primary-light text-white flex-col justify-center items-center p-10 text-center hidden md:flex">
      <img src="../../assets/img/CasalFinanceiro2.png" class="w-[20em] md:w-[28em] lg:w-[35em] mb-6" alt="Imagem 1" />
      <h2 class="text-2xl font-semibold">Olá, meu amigo!</h2>
      <p class="mt-2 text-gray-200 max-w-md">
        Organize suas finanças de um jeito simples e sem dor de cabeça.
      </p>
    </div>
  </div>

  
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import InputComponent from '../../components/InputComponent.vue';
import { ref } from 'vue'

const nome = ref('')
const email = ref('')
const senha = ref('')
const confirmarSenha = ref('')

function cadastrar() {
  if (email.value && senha.value && confirmarSenha.value && nome.value ) {
    if(senha.value === confirmarSenha.value){
      alert("Belezinha irmão! Tu criou tua continha")
      nome.value = ""
      email.value = ""
      senha.value = ""
      confirmarSenha.value = ""
    } else {
      alert("SENHA DIFERENTE CARALHO")
    }
  } else {
    alert('Por favor, preencha todos os campos.')
  }
}
</script>