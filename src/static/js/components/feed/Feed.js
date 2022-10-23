import "./feed.css"
import React from 'react'
//import axios from "axios";
//import {useEffect} from 'react'



export default function Feed() {
    /*useEffect (()=> {
        const url = "https://localhost:5000/";
        axios.get (${url})
        .then(response => console.log(response.data) )
        .catch (error => console.log(err))

    }, [])
       */
  return (
    <div className="feed">
          <div className="title">
              <h1> Top Health News </h1>
          </div>
        
          
          <hr className="hr" />

          <div className="main">

            <div className="introtext">
            <p>
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ea aspernatur rerum vel autem quidem numquam debitis excepturi unde? Obcaecati iusto adipisci repudiandae suscipit iure magnam minima odit facilis facere optio?
            </p>
            </div>
            

            <article class="design">
                    <div class="text1">
                        <h3> COVID-19 rapid tests can breed confusion – here’s how to make sense of the results and what to do, according to 3 testing experts </h3>
                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nobis officiis aliquid adipisci veritatis, ad numquam et! In assumenda dolore quam, corrupti, dignissimos, soluta est praesentium vel eligendi quibusdam beatae at!</p>
                    </div>
                    <img src="/assets/newsfeedthumbnail/thumb1.jpg" alt="" />
                </article>
                
                <article class="design">
                    <div class="text1">
                        <h3> COVID-19 rapid tests can breed confusion – here’s how to make sense of the results and what to do, according to 3 testing experts </h3>
                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nobis officiis aliquid adipisci veritatis, ad numquam et! In assumenda dolore quam, corrupti, dignissimos, soluta est praesentium vel eligendi quibusdam beatae at!</p>
                    </div>
                    <img src="/assets/newsfeedthumbnail/thumb1.jpg" alt="" />
                </article><article class="design">
                    <div class="text1">
                        <h3> COVID-19 rapid tests can breed confusion – here’s how to make sense of the results and what to do, according to 3 testing experts </h3>
                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nobis officiis aliquid adipisci veritatis, ad numquam et! In assumenda dolore quam, corrupti, dignissimos, soluta est praesentium vel eligendi quibusdam beatae at!</p>
                    </div>
                    <img src="/assets/newsfeedthumbnail/thumb1.jpg" alt="" />
                </article>
      </div>


    </div>
    

        
  )
}
