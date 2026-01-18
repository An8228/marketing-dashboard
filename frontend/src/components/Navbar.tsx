import { NavLink } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar">
      <span className="logo">SMARTREACH</span>
      <div className="nav-links">
        <NavLink to="/" end>Dashboard</NavLink>
        <NavLink to="/campaigns">Campaigns</NavLink>
        <NavLink to="/audiences">Audiences</NavLink>
        <NavLink to="/reports">Reports</NavLink>
      </div>
    </nav>
  );
}
