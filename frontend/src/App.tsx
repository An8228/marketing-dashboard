import { Dashboard } from "./pages/Dashboard";
import Navbar from "./components/Navbar";
import "./styles/theme.css";

function App() {
  return (
    <>
      <Navbar />
      <main className="app-container">
        <Dashboard />
      </main>
    </>
  );
}

export default App;
