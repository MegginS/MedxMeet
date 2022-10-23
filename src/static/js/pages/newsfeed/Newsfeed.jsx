import React from 'react'
import Topnavbar from '../../components/topnavbar/Topnavbar'
import Feed from '../../components/feed/Feed'
import Feedsidebar from '../../components/feedsidebar/Feedsidebar'
import "./newsfeed.css"

export default function Newsfeed() {
  return (
  <> 
    <Topnavbar/>
    <div className="newsfeedContainer">
      <Feed/>
      <Feedsidebar/>
    </div>
  </>    
  )

}
