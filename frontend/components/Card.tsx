import Link from 'next/link';
import { News } from '../types';

type Props = {
  news: News
}

export default function Card({ news }: Props) {
  return (
    <>
      <div className='rounded overflow-hidden shadow-lg'>
        <Link href={news.pageLink} passHref>
          <a className='rounded overflow-hidden shadow-lg' target='_blank' rel='noreferrer nofollow noopener'>
            <img src={news.pageImg !== 'false' ? news.pageImg : '/noimage.png'} alt='' className='w-full object-cover' />
            <div className='px-6 py-4'>
              {news.pageTitle}
            </div>
          </a>
        </Link>
      </div>
    </>
  )
}