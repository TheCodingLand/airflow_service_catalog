import React, {useState} from "react";
import { pure } from 'recompose';
import { PieChart, Pie, Sector, Cell, XAxis, Label, ResponsiveContainer,Tooltip, Legend } from 'recharts';
import "./charts.css"

const COLORS = ['#0088FE',  '#FF0028', '#00C49F', '#FF8042'];

const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="custom-tooltip">
          <p className="label">{`${label} : ${payload[0].value}`}</p>
          <p className="intro">info</p>
          <p className="desc">Anything you want can be displayed here.</p>
        </div>
      );
    }
  
    return null;
  };

const SuccessFailures = React.memo(data => {
        console.log(data)
        const [activeIndex, setActiveIndex] = useState(0);
        const onPieEnter = (data, index) => {
            setActiveIndex(index);
        };
        return <PieChart width={800} height={400} >
         
        <Pie
            isAnimationActive={true}
            activeIndex={activeIndex}
            //activeShape={renderActiveShape}
            dataKey="duration"
            
           //onMouseEnter={onMouseEnter}

          data={data.data}
          cx={120}
          cy={200}
          innerRadius={60}
          outerRadius={80}
          fill="#8884d8"
          paddingAngle={5}
          dataKey="value"
          label
        >
          {data.data.map((entry, index) => (
            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
          ))}
        
        </Pie>
        <Legend iconSize={10} layout="vertical" verticalAlign="middle"/>
        <Tooltip content={<CustomTooltip />} />
      </PieChart>
    
      
})
  

export default SuccessFailures

