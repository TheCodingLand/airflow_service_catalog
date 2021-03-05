// posts will be populated at build time by getStaticProps()

  

import useAxios from 'use-axios';

import SuccessFailures from './stats_chart'
import React from "react";


const Stats = ({ dagid }) => {
  const { data } = useAxios(`http://localhost:8000/emails`);
  
  return (
    <React.Fragment>

        {data.total_entries}
        <div style={{height:500}}>
            <SuccessFailures data={[{name : "success", value : data.total_entries}, {name : "failures", value : data.total_entries}]}></SuccessFailures>
        </div>
    </React.Fragment>
  );
};

export default Stats;