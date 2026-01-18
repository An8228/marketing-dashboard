type KpiCardProps = {
  title: string;
  value: string | number;
  subtitle?: string;
};

export default function KpiCard({ title, value, subtitle }: KpiCardProps) {
  return (
    <div className="kpi-card">
      <p className="kpi-title">{title}</p>
      <h2 className="kpi-value">{value}</h2>
      {subtitle && <span className="kpi-subtitle">{subtitle}</span>}
    </div>
  );
}
