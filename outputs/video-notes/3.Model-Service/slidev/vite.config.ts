import { defineConfig, loadEnv } from 'vite'
import { modelProxy } from './server/model-proxy'

export default defineConfig(({ mode }) => ({
  plugins: [modelProxy({ ...loadEnv(mode, process.cwd(), 'MODEL_'), ...Object.fromEntries(Object.entries(process.env).filter(([key, value]) => key.startsWith('MODEL_') && value !== undefined)) } as Record<string, string>)],
  server: { host: '127.0.0.1' },
}))
