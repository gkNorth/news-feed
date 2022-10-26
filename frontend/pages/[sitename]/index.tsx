import type { NextPage } from 'next'
// import Head from 'next/head'
// import Image from 'next/image'
import fetchProjects from 'utils/client'
import Card from 'components/Card'
import { News } from 'types'

type Props = {
  newsList: News[]
}

const Home: NextPage<Props> = ({ newsList }) => {
  return (
    <>
      <div className="list container mx-auto p-10 grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-5">
        {newsList && newsList.map(news => <Card news={news} key={news.id} />)}
      </div>
    </>
  )
}

export default Home

export const getServerSideProps = async () => {
  const newsList: News[] = await fetchProjects()
  return { props: { newsList } }
}