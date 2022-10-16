import React from 'react'
import "./topnavbar.css"

export default function topnavbar() {
  return (
    <div className="topnavbarContainer">
        <div className="topbarleft">
          <span className='logo'>medxmeet logo</span>
        </div>      

        <div className="topbarcenter">
          <div className="centerlinks">
            <span className="topbarlink">Newsfeed</span>
            <span className="topbarlink">Forum</span>
            <span className="topbarlink">Clinical Trials</span>
          </div>
        </div>

        <div className="topbaright">
          <img src="/assets/persons/1.jpg" alt="" className='topbarImg'/>
          <div className="topbarIcons">
             <span className="topbarlink">Logout</span>
          </div>
        </div>
    </div>
  )
}
