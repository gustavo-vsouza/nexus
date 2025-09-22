<script setup lang="ts">
import { computed } from "vue"

const props = defineProps<{
  modelValue?: string
  tipo?: string
  label?: string
  placeholder?: string
  icon?: string
  required?: boolean
  id?: string
  error?: string // mensagem de erro opcional
}>()

const emit = defineEmits<{
  (e: "update:modelValue", value: string): void
}>()

// ID único caso não seja passado
const inputId = computed(
  () => props.id ?? `input-${Math.random().toString(36).substring(2, 9)}`
)
</script>

<template>
  <div class="w-full">
    <!-- Label acima -->
    <label
      :for="inputId"
      class="block text-sm font-medium text-neutral-gray mb-1"
    >
      {{ label }}
      <span v-if="required" class="text-red-500">*</span>
    </label>

    <!-- Wrapper -->
    <div class="relative flex items-center">
      <!-- Input -->
      <input
        :id="inputId"
        :type="tipo || 'text'"
        :placeholder="placeholder"
        :required="required"
        :value="modelValue"
        :aria-invalid="!!error"
        @input="emit('update:modelValue', ($event.target as HTMLInputElement).value)"
        class="peer w-full rounded-lg border bg-gray-50 px-4 py-2 pr-12 text-gray-900 
               placeholder-transparent focus:outline-none transition
               focus:border-blue-600 focus:ring-2 focus:ring-blue-500
               border-gray-300
               aria-[invalid='true']:border-red-500 aria-[invalid='true']:focus:ring-red-500"
      />

      <!-- Label flutuante animada dentro do input -->
      <span
        class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 text-sm pointer-events-none transition-all
               peer-placeholder-shown:top-1/2 peer-placeholder-shown:text-base peer-placeholder-shown:text-gray-400
               peer-focus:top-0 peer-focus:text-xs peer-focus:text-blue-600"
      >
        {{ placeholder }}
      </span>

      <!-- Ícone (Google Material Symbols) -->
      <span
        v-if="icon"
        class="material-symbols-outlined absolute right-3 text-gray-400 transition
               peer-focus:text-blue-600 peer-aria-[invalid='true']:text-red-500"
      >
        {{ icon }}
      </span>
    </div>

    <!-- Mensagem de erro -->
    <p v-if="props.error" class="mt-1 text-sm text-red-600 flex items-center gap-1">
      <span class="material-symbols-outlined text-sm">error</span>
      {{ props.error }}
    </p>
  </div>
</template>
