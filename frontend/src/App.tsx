import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";

function Placeholder({ title }: { title: string }) {
  return <h1>{title} (Coming Soon)</h1>;
}

export default function App() {
  return (
    <>
      <Navbar />
      <div className="app-container">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/campaigns" element={<Placeholder title="Campaigns" />} />
          <Route path="/audiences" element={<Placeholder title="Audiences" />} />
          <Route path="/reports" element={<Placeholder title="Reports" />} />
        </Routes>
      </div>
    </>
  );
}
