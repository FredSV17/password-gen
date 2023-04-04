import Head from 'next/head'
import Image from 'next/image'
import { Inter } from '@next/font/google'
import Header from 'src/components/header'
import GeneratorBody from 'src/components/generatorBody'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Header />
      <GeneratorBody />
    </>
  )
}
