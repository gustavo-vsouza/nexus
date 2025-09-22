// src/services/usuarios.ts
import api from "./api";

export interface Usuario {
  id: number;
  nome: string;
  email: string;
  status: string;
}

export interface UsuarioCreate {
  nome: string;
  email: string;
  senha_hash: string;
  status?: string;
}

// Criar usuário
export const criarUsuario = async (dados: UsuarioCreate) => {
  console.log(dados)
  const response = await api.post<Usuario>("/usuarios/", dados);
  return response.data;
};

// Listar todos usuários
export const listarUsuarios = async () => {
  const response = await api.get<Usuario[]>("/usuarios/");
  return response.data;
};

// Buscar usuário por ID
export const buscarUsuario = async (id: number) => {
  const response = await api.get<Usuario>(`/usuarios/${id}`);
  return response.data;
};

// Atualizar usuário
export const atualizarUsuario = async (id: number, dados: Partial<UsuarioCreate>) => {
  const response = await api.put<Usuario>(`/usuarios/${id}`, dados);
  return response.data;
};

// Deletar usuário
export const deletarUsuario = async (id: number) => {
  const response = await api.delete<Usuario>(`/usuarios/${id}`);
  return response.data;
};
