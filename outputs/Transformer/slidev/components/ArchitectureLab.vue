<script setup lang="ts">
import LabShell from './LabShell.vue'
import ArchitectureMap from './ArchitectureMap.vue'
const steps=['源句进入编码器','自注意力交换信息','残差与标准化','逐位置 FFN','得到源句表示','目标前缀输入','只看已知目标','整理目标表示','跨序列读取源句','逐位置加工','输出词表概率']
</script>
<template><LabShell :steps="steps" label="完整数据流 · 逐步高亮" v-slot="{ step }"><ArchitectureMap :active="step" compact/></LabShell></template>
