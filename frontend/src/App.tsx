import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import "./styles/theme.css";

export default function App() {
  return (
    <div className="app-container">
      <Navbar />
      <main className="page-container">
        <Dashboard />
      </main>
    </div>
  );
}

