<script setup lang="ts">
import { ref } from "vue";
import { criarUsuario } from "@/services/usuarios";

const nome = ref("");
const email = ref("");
const senha = ref("");
const mensagem = ref("");

const registrar = async () => {
  try {
    const usuario = await criarUsuario({
      nome: nome.value,
      email: email.value,
      senha_hash: senha.value, // aqui ainda é senha simples
    });
    mensagem.value = `Usuário criado com sucesso! ID: ${usuario.id}`;
  } catch (error: any) {
    mensagem.value = error.response?.data?.detail || "Erro ao registrar usuário";
  }
};
</script>

<template>
  <div class="login">
    <h2>Cadastro de Usuário</h2>
    <input v-model="nome" placeholder="Nome" />
    <input v-model="email" placeholder="Email" type="email" />
    <input v-model="senha" placeholder="Senha" type="password" />
    <button @click="registrar">Registrar</button>

    <p>{{ mensagem }}</p>
  </div>
</template>

<style scoped>
.login {
  display: flex;
  flex-direction: column;
  max-width: 300px;
  margin: auto;
  gap: 10px;
}
</style>
