import React from 'react'
import "./feedsidebar.css"
import SearchIcon from '@mui/icons-material/Search';

export default function Feedsidebar() {
  return (
    <div>
      <div className="feedsidebar">
      <div className="searchbar">
        <input
                placeholder="Search for friend, post or video"
                className="searchInput"
            />
          <SearchIcon className="searchIcon" />
       </div>
      </div>

    </div>
  )
}
