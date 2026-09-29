<script setup lang="ts">
import { useNav } from '@slidev/client'
const { currentPage, total } = useNav()
</script>
<template><footer class="deck-footer"><span>TRANSFORMER · 交互技术讲义</span><span>{{ currentPage }} / {{ total }}</span></footer></template>
