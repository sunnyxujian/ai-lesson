/// <reference types="vite/client" />
import '@slidev/client/shim-vue.d.ts'
import '@slidev/client/shim.d.ts'

// Slidev 运行时注入的编译常量，仅为依赖源码的静态类型检查提供声明。
declare global {
  const __DEV__: boolean
  const __SLIDEV_FEATURE_EDITOR__: boolean
  const __SLIDEV_HAS_SERVER__: boolean
  const __SLIDEV_HASH_ROUTE__: boolean
  const __SLIDEV_FEATURE_DRAWINGS_PERSIST__: boolean
}
