<template>
    <div class="flex flex-col items-center text-white group cursor-pointer">
        <div :class="[
            'flex items-center justify-center w-12 h-12 rounded-xl transition',
        ]" :style="{
            backgroundColor: active
                ? color + '40'
                : 'transparent',
            boxShadow: active
                ? `0 0px 20px ${hexToRgba(color, 0.25)}`
                : 'none'
        }">
            <!-- ícone -->
            <component :is="icon" class="w-6 h-6 transition" :style="{
                color: active ? color : '#fff'
            }" />
        </div>

        <!-- renderiza só se houver label -->
        <span v-if="label" class="text-[13px] mt-1 text-gray-300 transition" :style="{
            color: active ? color : '#d1d5db'
        }">
            {{ label }}
        </span>
    </div>
</template>

<script setup lang="ts">
const { icon, label, color, active } = defineProps<{
    icon: any
    label?: string
    color: string
    active?: boolean
}>()

function hexToRgba(hex: string, alpha: number) {
    const r = parseInt(hex.slice(1, 3), 16)
    const g = parseInt(hex.slice(3, 5), 16)
    const b = parseInt(hex.slice(5, 7), 16)
    return `rgba(${r},${g},${b},${alpha})`
}
</script>
