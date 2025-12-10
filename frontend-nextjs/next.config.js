/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  trailingSlash: true,
  reactStrictMode: true,
  images: {
    unoptimized: true,
  },
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'https://api.caiodev.me',
  },
}

module.exports = nextConfig
// Deploy trigger: Wed Dec 10 00:13:58 -03 2025
