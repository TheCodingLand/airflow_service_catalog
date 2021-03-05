import logo from './logo.svg';
import './App.css';
///import Stats from './components/stats'
import {Suspense, lazy, memo} from "react";


const Spinner = memo(() => <div>🌀</div>);
const Stats = lazy(async () => {
  
  return import("./components/stats");
});

function App() {
  return (
    <div className="App">
      
        <Suspense fallback={<Spinner />} maxDuration={1000}>
          <Stats />
        </Suspense>
        
    
      
    </div>
  );
}

export default App;
