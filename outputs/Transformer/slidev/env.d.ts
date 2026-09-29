/// <reference types="vite/client" />
/// <reference types="@slidev/types/client" />
/// <reference types="@slidev/client/shim-vue.d.ts" />
/// <reference types="@slidev/client/shim.d.ts" />

// Slidev/Vite 在运行时注入的编译期布尔常量；供独立 vue-tsc 检查客户端源码使用。
declare const __DEV__: boolean
declare const __SLIDEV_FEATURE_EDITOR__: boolean
declare const __SLIDEV_FEATURE_DRAWINGS_PERSIST__: boolean
declare const __SLIDEV_HAS_SERVER__: boolean
declare const __SLIDEV_HASH_ROUTE__: boolean
