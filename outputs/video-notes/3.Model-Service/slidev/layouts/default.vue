<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
const { $frontmatter, $page } = useSlideContext()
</script>
<template>
  <div class="slidev-layout lesson-layout">
    <header class="lesson-header"><span>AI 基础 / 03</span><span>MODEL SERVICE</span></header>
    <main><slot /></main>
    <footer class="lesson-footer"><a :href="`/reference/完整教程.html#section-${String($frontmatter.source ?? 1).padStart(2, '0')}`" target="_blank" rel="noopener" @click.stop>阅读完整教程 ↗</a><span>{{ String($page).padStart(2,'0') }} / 25</span></footer>
  </div>
</template>
